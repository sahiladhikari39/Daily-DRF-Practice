from django.urls import path
from .views import ProductListCreateView, ProductDetailView


urlpatterns = [
    # path('products/', product_detail),
    # path('products/', Product_List.as_view()),
    # path('products/<int:pk>', Product_List.as_view()),
    # path('products/create', Product_create.as_view()),
    # path('products/<int:pk>', Product_Detail_view.as_view()),

    # path('products/', ProductListCreateView.as_view()),
    # path('products/<int:pk>', ProductUpdateView.as_view()),
    # path('products/del/<int:pk>', ProductDeleteView.as_view()),

    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
]