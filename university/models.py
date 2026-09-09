from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=35)
    email = models.EmailField(unique=True)
    joined_date = models.DateField()


class Course(models.Model):
    name = models.CharField(max_length=20)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    