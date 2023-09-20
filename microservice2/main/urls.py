from django.urls import path
from main import views

urlpatterns = [
    path('microservice2', views.bd_list),
]
