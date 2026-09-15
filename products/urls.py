from django.urls import path
from .views import Product_Detail_view, Product_List, Product_create


urlpatterns = [
    # path('products/', product_detail),
    path('products/', Product_List.as_view()),
    path('products/<int:pk>', Product_List.as_view()),
    path('products/create', Product_create.as_view()),
    path('products/<int:pk>', Product_Detail_view.as_view()),
    
]