from django.urls import path
from .views import course_view, course_detail_view, teacher_view, teacher_detail_view


urlpatterns = [
    path('courses/', course_view),
    path('courses/<int:pk>', course_detail_view),
    path('teachers/', teacher_view),
    path('teachers/<int:pk>', teacher_detail_view),
]