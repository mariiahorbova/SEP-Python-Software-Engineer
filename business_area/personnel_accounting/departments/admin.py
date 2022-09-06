from django.contrib import admin
from departments.models import Department
from workers.models import Worker
from positions.models import Position
from position_history.models import PositionHistory
from vacations.models import Vacation


admin.site.register(Department)
admin.site.register(Worker)
admin.site.register(Position)
admin.site.register(PositionHistory)
admin.site.register(Vacation)
