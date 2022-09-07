from django.db import models

from departments.models import Department
from positions.models import Position


class Worker(models.Model):
    identification_number = models.IntegerField(unique=True, default="0")
    surname = models.CharField(max_length=100, blank=True, default="")
    name = models.CharField(max_length=100, blank=True, default="")
    middle_name = models.CharField(max_length=100, blank=True, default="")
    passport = models.CharField(unique=True, max_length=20, blank=True, default="")
    work_years = models.IntegerField(blank=True, default="0")
    birth_date = models.DateField(blank=True)
    birth_place = models.CharField(max_length=100, blank=True, default="")
    address_country = models.CharField(max_length=100, blank=True, default="")
    address_city = models.CharField(max_length=100, blank=True, default="")
    address_street = models.CharField(max_length=100, blank=True, default="")
    address_house_number = models.IntegerField(blank=True, default="0")
    address_house_letter = models.CharField(max_length=5, blank=True, default="")
    vacation_days_left = models.IntegerField(blank=True, default="0")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return self.surname + ' ' + self.name
