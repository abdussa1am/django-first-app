from rest_framework import serializers

from .models import Crop

class CropSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crop
        fields = ('elem' , 'item' , 'year')