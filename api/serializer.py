from rest_framework import serializers
from .models import Mattle

class MattleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mattle
        fields='__all__'