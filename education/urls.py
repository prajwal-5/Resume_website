from django.urls import path
from . import views

urlpatterns = [
    path('', views.education, name='education'),
]
