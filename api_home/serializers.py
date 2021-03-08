from rest_framework import serializers

from profiles.models import ads

class home_serial(serializers.ModelSerializer):


    class Meta:

        model=ads

        fields='__all__'
