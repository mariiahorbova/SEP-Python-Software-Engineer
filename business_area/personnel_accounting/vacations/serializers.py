from rest_framework import serializers
from vacations.models import Vacation


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ["id", "start_date", "end_date"]