from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import ProductListCreateView, ProductDetailView
# from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView
from .views import ProductViewSet

router = DefaultRouter()

router.register('products', ProductViewSet)


# urlpatterns = [
#     # path('products/', product_detail),
#     # path('products/', Product_List.as_view()),
#     # path('products/<int:pk>', Product_List.as_view()),
#     # path('products/create', Product_create.as_view()),
#     # path('products/<int:pk>', Product_Detail_view.as_view()),

#     # path('products/', ProductListCreateView.as_view()),
#     # path('products/<int:pk>', ProductUpdateView.as_view()),
#     # path('products/del/<int:pk>', ProductDeleteView.as_view()),

#     # path('products/', ProductListCreateView.as_view()),
#     # path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),

# ]

urlpatterns = router.urls