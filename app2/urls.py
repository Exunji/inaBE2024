from django.urls import path
from . import views

urlpatterns = [
    path('index2/', views.index2),
    path('despacito/', views.despacito),
]