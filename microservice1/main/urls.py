from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main import views

urlpatterns = [
    path('', views.bd_list),
    path('<int:pk>', views.bd_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
