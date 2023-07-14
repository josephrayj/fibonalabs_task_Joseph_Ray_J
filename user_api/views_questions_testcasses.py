from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Question, TestCase
from .serializers import QuestionSerializer, TestCaseSerializer , QuestionSerializerParticepent ,TestCaseSerializerParticepent
from django.http import Http404

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def question_list_create_view(request): 
    if request.method == 'GET':
        if request.is_admin:
            questions = Question.objects.all()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        else:
            questions = Question.objects.all()
            serializer = QuestionSerializerParticepent(questions, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        if request.is_admin:
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({'error': 'Only admin can add questions'}, status=403)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def question_retrieve_update_delete_view(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")

    if request.method == 'GET':
        if request.is_admin:
            serializer = QuestionSerializer(question)
            return Response(serializer.data)
        else:
            serializer = QuestionSerializerParticepent(question)
            return Response(serializer.data)
    elif request.method == 'PUT':
        if request.is_admin:
            serializer = QuestionSerializer(question, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        else:
            return Response({'error': 'Only admin can edit questions'}, status=403)
    elif request.method == 'DELETE':
        if request.is_admin:
            question.delete()
            return Response({'deleted': 'True'},status=204)
        else:
            return Response({'error': 'Only admin can delete questions'}, status=403)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def test_case_create_view(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")

    if request.is_admin:
        serializer = TestCaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(question=question)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:
        return Response({'error': 'Only admin can add test cases'}, status=403)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def testcase_retrieve_update_delete_view(request, testcase_id):
    try:
        testcase = TestCase.objects.get(pk=testcase_id)
    except TestCase.DoesNotExist:
        raise Http404("Test case does not exist.")

    if request.method == 'GET':
        serializer = TestCaseSerializer(testcase)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if request.is_admin:
            serializer = TestCaseSerializer(testcase, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        else:
            return Response({'error': 'Only admin can edit test cases'}, status=403)
    elif request.method == 'DELETE':
        if request.is_admin:
            testcase.delete()
            return Response({'deleted': 'True'},status=204)
        else:
            return Response({'error': 'Only admin can delete test cases'}, status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_solution_view(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")

    user_solution = request.data.get('solution')

    try:
        expected_output = question.test_cases.first().output
        if user_solution == expected_output:
            result = 'success'
            message = 'Congratulations! Your solution is correct.'
        else:
            result = 'wrong'
            message = 'Sorry, your solution is incorrect.'
    except AttributeError:
        return Response({'error': 'Question does not have any test cases'}, status=400)
    except Exception as e:
        return Response({'error': 'An error occurred while evaluating the solution'}, status=500)

    response_data = {
        'result': result,
        'message': message
    }

    return Response(response_data)
