from rest_framework import serializers
from positions.models import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ["id", "title", "salary", "vacation_days"]
