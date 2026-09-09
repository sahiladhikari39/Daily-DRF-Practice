from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TeacherSerializer, CourseSerializer
from .models import Course, Teacher

# Create your views here.

@api_view(['GET', 'POST'])
def course_view(request):
     if request.method == 'GET':
          course = Course.objects.all()
          serializers = CourseSerializer(course, many=True)
          return Response(serializers.data)
     if request.method == 'POST':
          serializers = CourseSerializer(data=request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def teacher_view(request):
     if request.method == 'GET':
          teacher = Teacher.objects.all()
          serializers = TeacherSerializer(teacher, many=True)
          return Response(serializers.data, status=status.HTTP_200_OK)
     if request.method == 'POST':
          serializers = TeacherSerializer(data=request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)