from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100, blank=True, default="")
    salary = models.IntegerField(blank=True)
    vacation_days = models.IntegerField(blank=True)

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.title
