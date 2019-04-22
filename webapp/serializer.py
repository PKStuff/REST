from rest_framework import serializers
from .models import employee

class REST_DATA(serializers.ModelSerializer):

    class Meta:

        model = employee
        fields = '__all__'
