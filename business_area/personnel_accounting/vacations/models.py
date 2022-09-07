from django.db import models
from workers.models import Worker


class Vacation(models.Model):
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Vacation"
        verbose_name_plural = "Vacations"
