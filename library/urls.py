from django.urls import path
from .views import author_view, book_view


urlpatterns = [
    path('authors/', author_view),
    path('books/', book_view),
]