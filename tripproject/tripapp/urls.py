from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('team/', views.team_view, name='team'),
]
