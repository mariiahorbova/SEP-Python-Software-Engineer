from django.db import models
from workers.models import Worker
from positions.models import Position


class PositionHistory(models.Model):
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    id_worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True, blank=True)
    id_position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Position history"
        verbose_name_plural = "Position histories"
