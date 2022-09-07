from django.urls import path
from departments import views


urlpatterns = [
    path("departments/", views.department_list),
    path("departments/<int:pk>", views.department_detail),
]
