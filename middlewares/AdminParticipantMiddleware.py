from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser
from rest_framework.exceptions import AuthenticationFailed

class AdminParticipantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth = JWTAuthentication()
        try:
            user, _ = auth.authenticate(request)
            if user is not None:
                request.is_token_available = True
                if user.role == 'admin':
                    request.is_admin = True
                else:
                    request.is_admin = False
            else:
                request.is_token_available = False
                request.is_admin = False

        except AuthenticationFailed:
            request.is_token_available = False
            request.is_admin = False
        except Exception as e:
            print(e)

        response = self.get_response(request)
        return response
