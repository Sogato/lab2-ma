from django.urls import path
from main import views

urlpatterns = [
    path('microservice1', views.bd_list),
]
