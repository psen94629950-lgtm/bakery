from rest_framework import serializers
from .models import Team_d

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_d
        fields = '__all__'
