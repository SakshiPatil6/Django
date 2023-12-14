from django.urls import path
from . import views

urlpatterns = [
    path('demoApp/', views.demoFun, name='demoFun'),
]