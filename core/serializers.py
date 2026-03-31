from rest_framework import serializers
from .models import Student

#Convert Model<--->JSON
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields To Expose In API
        #Ppassword Hidden For Security
        fields = ['id','name','email','subject','city']
        