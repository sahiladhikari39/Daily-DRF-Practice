from django.urls import path
from .views import course_view, teacher_view


urlpatterns = [
    path('courses/', course_view),
    path('teachers/', teacher_view),
    
]