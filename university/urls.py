from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CourseListView, CourseDetailListView, TeacherListView, TeacherDetailview


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>', CourseDetailListView.as_view()),
    # path('courses/', course_view),
    # path('courses/<int:pk>', course_detail_view),
    # path('teachers/', teacher_view),
    # path('teachers/<int:pk>', teacher_detail_view),
    path('teachers/', TeacherListView.as_view()),
    path('teachers/<int:pk>', TeacherDetailview.as_view()),
]