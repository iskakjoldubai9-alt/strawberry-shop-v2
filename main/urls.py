from django.urls import path
from . import views # views.py файлын чакырып жатабыз

urlpatterns = [
    path('', views.index, name='index'), # Башкы бетти (login баракчасын) көрсөтөт
]