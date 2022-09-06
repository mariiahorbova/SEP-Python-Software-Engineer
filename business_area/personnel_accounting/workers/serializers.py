from rest_framework import serializers
from workers.models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = [
            "id",
            "identification_number",
            "surname",
            "name",
            "middle_name",
            "passport",
            "work_years",
            "birth_date",
            "birth_place",
            "address_country",
            "address_city",
            "address_street",
            "address_house_number",
            "address_house_letter",
            "vacation_days_left",
        ]
