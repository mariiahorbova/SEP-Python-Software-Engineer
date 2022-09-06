from django.db import models

from workers.models import Worker


class Department(models.Model):
    title = models.CharField(max_length=100, blank=True, unique=True, default="")
    abbreviation = models.CharField(max_length=10, blank=True, unique=True, default="")
    workers_count = models.IntegerField(blank=True, default=0)
    id_manager = models.OneToOneField(Worker, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.title
