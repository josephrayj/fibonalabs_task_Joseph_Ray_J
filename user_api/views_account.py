# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed


from django.db import IntegrityError
from rest_framework import status

@api_view(['POST'])
def signup(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')

    if not name or not email or not password or not role:
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User(name=name, email=email, role=role,username=email)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
    except IntegrityError:
        return Response({'error': 'Email already exists'}, status=status.HTTP_409_CONFLICT)
    except Exception as e:
        return Response({'error': 'Error occurred during signup'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = UserSerializer(user)
    return Response({'email': user.email, 'access_token': access_token})

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()

    try:
        if user is None or not user.check_password(password):
            raise AuthenticationFailed('Invalid email or password')
    except AuthenticationFailed as e:
        return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    return Response({'email': user.email, 'access_token': access_token})
