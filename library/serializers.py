from rest_framework import serializers
from .models import Author, Book
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_details = AuthorSerializer(read_only=True, source='author')
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True)
    class Meta:
        model = Book
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("The price should be greater than 0!!!")
        return value

    def validate_pages(self, value):
        if value ==0:
            raise serializers.ValidationError("The pages shouldnot be equal to 0!!!")
        return value    

    def validate_published_date(self, value):
        today = date.today()
        if value > today:
            raise serializers.ValidationError("The published date cannot be in future")
        return value

    def validate(self, attrs):
        if attrs['discount_price'] >= attrs['price']:
            raise serializers.ValidationError("Discount price must be less than the original price.")
        return attrs