from django.urls import path
from . import views

urlpatterns = [
    # Paths del contacto
    path('', views.contact, name='contact'),
]