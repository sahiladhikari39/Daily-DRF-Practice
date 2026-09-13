from django.urls import path
from .views import CourseListView, CourseDetailListView, TeacherListView, TeacherDetailListview


urlpatterns = [
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>', CourseDetailListView.as_view()),
    # path('courses/', course_view),
    # path('courses/<int:pk>', course_detail_view),
    # path('teachers/', teacher_view),
    # path('teachers/<int:pk>', teacher_detail_view),
    path('teachers/', TeacherListView.as_view()),
    path('teachers/<int:pk>', TeacherDetailListview.as_view()),
]