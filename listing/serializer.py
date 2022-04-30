from rest_framework import serializers
from .models import ListingModel


class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingModel
        fields =  '__all__'

    
