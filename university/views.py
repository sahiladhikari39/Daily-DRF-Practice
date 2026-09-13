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


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def course_detail_view(request, pk):
     if request.method=='DELETE':
          try:
               course = Course.objects.get(pk=pk)
          except Course.DoesNotExist():
               return Response({"error": "Course doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
          course.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
     else:
          try:
               course = Course.objects.get(pk=pk)
          except Course.DoesNotExist:
               return Response({"error": "Course Not Found"}, status=status.HTTP_404_NOT_FOUND)
          serializers = CourseSerializer(course, data=request.data, partial=True)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data)
          return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def teacher_detail_view(request, pk):
     if request.method == 'DELETE':
          try:
               teacher = Teacher.objects.get(pk=pk)
          except Teacher.DoesNotExist:
               return Response({"error": "Teacher doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
          teacher.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
     else:
          try:
               teacher = Teacher.objects.get(pk=pk)
          except Teacher.DoesNotExist:
               return Response({"error": "Teacher doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
          serializer = TeacherSerializer(teacher, data=request.data, partial=True)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)