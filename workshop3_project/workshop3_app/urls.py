from django.urls import path
from . import views

urlpatterns = [
    path('calculate_serial_sum/<int:n>/', views.calculate_serial_sum, name='calculate_serial_sum'),
    path('calculate_serial_sum/<int:n>/<int:m>/', views.calculate_serial_sum, name='calculate_serial_sum'),
]
