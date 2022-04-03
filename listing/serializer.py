from rest_framework import serializers
from .models import ListingModel


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingModel
        fields = [
            'title', 'slug', 'address',
            'city','state','zipcode','description','price','bedrooms',
            'bathrooms','sale_type','home_type','main_photo','photo1','photo2','photo3','is_published'
        ]

class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingModel
        fields =  '__all__'

    
