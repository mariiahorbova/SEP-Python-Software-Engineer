from django.urls import path
from workers import views


urlpatterns = [
    path("workers/", views.workers_list),
    path("workers/<int:pk>", views.workers_detail),
]
