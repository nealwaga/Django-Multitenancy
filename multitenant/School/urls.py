from django.urls import path
from . import views

# Create here
urlpatterns = [
     path('', views.get_Students, name='index'),
]
