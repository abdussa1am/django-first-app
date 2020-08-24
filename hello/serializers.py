from rest_framework import serializers

from .models import Passenger , Flight

class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passenger
        fields = ('first', 'last' , 'flights')
class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ()