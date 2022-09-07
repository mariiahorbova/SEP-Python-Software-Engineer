from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=100, blank=True, unique=True, default="")
    abbreviation = models.CharField(max_length=10, blank=True, unique=True, default="")

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.title


class DepartmentManager(models.Model):
    """
    Table for one-to-one between Department and Worker
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    manager = models.ForeignKey('workers.Worker', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.department} -> {self.manager}'
