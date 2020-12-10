from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setup', views.setup, name='setup'),
    path('live', views.live, name='live'),
    path('history', views.history, name='history'),
]