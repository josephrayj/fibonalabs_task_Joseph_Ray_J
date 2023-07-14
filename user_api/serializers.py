from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'role', 'name']
        extra_kwargs = {'password': {'write_only': True}}
        
        
        
# serializers.py
from rest_framework import serializers
from .models import Question, TestCase

class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'input', 'output']
        

class TestCaseSerializerParticepent(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'input',]


class QuestionSerializer(serializers.ModelSerializer):
    test_cases = TestCaseSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'test_cases']

class QuestionSerializerParticepent(serializers.ModelSerializer):
    test_cases = TestCaseSerializerParticepent(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text','test_cases' ]