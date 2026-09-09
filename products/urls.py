from django.urls import path
from .views import product_detail


urlpatterns = [
    path('products/', product_detail),
    
]