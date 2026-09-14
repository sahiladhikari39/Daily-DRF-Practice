from django.urls import path
from .views import Product_Detail_view, Product_View


urlpatterns = [
    # path('products/', product_detail),
    path('products/', Product_View.as_view()),
    path('products/<int:pk>', Product_Detail_view.as_view()),
    
]