# Serializers define the API representation.
from rest_framework import serializers
from restaurant.models import Booking, MenuItem


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'num_guests', 'booking_date']


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = MenuItem
    fields = ['id', 'title', 'price', 'inventory']

