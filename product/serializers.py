from rest_framework import serializers
from .models import Category, Product, Contact, Bucket, BucketProduct, Rating

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'

class BucketProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketProduct
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
