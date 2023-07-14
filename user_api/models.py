from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('participant', 'Participant'),
    )
    
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLES)
    # USERNAME_FIELD = 'email'
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',  # Add a related_name argument
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Add a related_name argument
        related_query_name='custom_user'
    )


# models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    # Other fields for the question

class TestCase(models.Model):
    question = models.ForeignKey(Question, related_name='test_cases', on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()