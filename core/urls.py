from django.urls import path 
from .views import get_students,create_students

urlpatterns = [
    path('students/',get_students),
    path('create_students/',create_students)
]