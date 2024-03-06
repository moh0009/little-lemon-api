from rest_framework import serializers
from . import models

class BookingSerializer(serializers.ModelSerializer):
    model = models.Booking
    fields = "__all__"

class MenuSerializer(serializers.ModelSerializer):
    model = models.Menu
    fields = "__all__"