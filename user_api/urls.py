
# urls.py
from django.urls import path
from .views_account import signup, login
from .views_questions_testcasses import (
    question_list_create_view,
    question_retrieve_update_delete_view,
    test_case_create_view,
    submit_solution_view,
    testcase_retrieve_update_delete_view
)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]




urlpatterns += [
    path('questions/', question_list_create_view, name='question-list-create'),
    path('questions/<int:question_id>/', question_retrieve_update_delete_view, name='question-retrieve-update-delete'),
    path('questions/<int:question_id>/testcases/', test_case_create_view, name='test-case-create'),
    path('questions/<int:question_id>/submit/', submit_solution_view, name='submit-solution'),
    path('testcase/<int:testcase_id>/', testcase_retrieve_update_delete_view, name='testcase-retrieve-update-delete'),
]

