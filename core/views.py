from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializers = StudentSerializer(students, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def create_students(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.error)

