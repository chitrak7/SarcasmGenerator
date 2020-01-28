from django.urls import path

from . import views

urlpatterns = [
    path('', views.query, name='query'),
    path('search', views.queryResults, name="results"),
]