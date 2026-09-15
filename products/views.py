from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
# Create your views here.

# @api_view(['GET'])
# def product_detail(request):
#     product = Product.objects.all()
#     serializer = ProductSerializer(product, many=True)
#     return Response(serializer.data)


class Product_View(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        product = self.get_queryset()
        serializer = self.get_serializer(product, many =True)
        return Response(serializer.data)


class Product_create(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Product_Detail_view(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer)