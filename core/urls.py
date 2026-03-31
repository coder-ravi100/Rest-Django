from django.urls import path 
from . import views

urlpatterns = [
    path('students/',views.students), #GET All Student
    path('students/<int:pk>',views.studentget), #GET Single Student
    path('add_students/',views.add_students), #POST Create
    path('update_students/<int:pk>', views.update_students), #PUT Update
    path('delete_students/<int:pk>',views.delete_students) #DELETE 
]