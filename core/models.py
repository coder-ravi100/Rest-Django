from django.db import models

#student table Structure (Database Schema)
class Student(models.Model):
    name = models.CharField(max_length=30)  # Student name
    email = models.CharField(max_length=30, unique=True)  # Unique email
    password = models.CharField(max_length=12)  # Password (plain text - not good practice)
    city = models.CharField(max_length=30)  # City name
    subject = models.CharField(max_length=30)  # Subject


    def __str__(self):
        return f"{self.name} {self.subject}" 