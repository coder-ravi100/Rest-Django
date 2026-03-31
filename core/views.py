from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# ..................
# GET ALL STUDENTS
# ..................
@api_view(['GET'])
def students(request):
    students = Student.objects.all() #Fetch All Records
    serializer = StudentSerializer(students, many = True) #many = True For List
    return  Response(serializer.data, status=status.HTTP_200_OK)


# ...................
# GET SINGLE STUDENTS
# ...................
@api_view(['GET'])
def studentget(request,pk):
    try:
        students = Student.objects.get(id = pk)
    except Student.DoesNotExist:
        return Response({"error" : "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(students)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ......................
# CREATE STUDENTS (POST)
# ......................
@api_view(['POST'])
def  add_students(request):
    serializer = StudentSerializer(data=request.data)  #Incoming JSON

    if serializer.is_valid(): #validation Check
        serializer.save() #Insert Into DB
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ......................
# UPDATE STUDENTS (PUT)
# ......................
@api_view(['PUT'])
def update_students(request,pk):
    try:
        students = Student.objects.get(id = pk)
    except Student.DoesNotExist:
        return Response({"error": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(students,data=request.data) #Update Data

    if serializer.is_valid():
        serializer.save() #Update DB
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ................
# DELETE STUDENTS
# ................
@api_view(['DELETE'])
def delete_students(request,pk):
    try:
        students = Student.objects.get(id = pk)
    except Student.DoesNotExist:
        return Response({"error" : "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
    
    students.delete() #Delete Records
    return Response({"Message" : "Successfully Deleted!"},status=status.HTTP_202_ACCEPTED)


