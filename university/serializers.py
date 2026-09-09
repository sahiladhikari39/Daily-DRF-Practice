from rest_framework import serializers
from .models import Teacher, Course

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), write_only=True)
    teacher_details = TeacherSerializer(source='teacher', read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

    def validate_credit(self, value):
        if value == 0:
            return serializers.ValidationError("The credit cannot be 0!!!")
        if value > 6:
            return serializers.ValidationError("The Credit cannot be greater than 6!!!")
        return value