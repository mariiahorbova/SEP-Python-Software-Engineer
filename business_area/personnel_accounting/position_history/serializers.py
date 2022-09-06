from rest_framework import serializers
from position_history.models import PositionHistory


class PositionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionHistory
        fields = ["id", "start_date", "end_date"]
