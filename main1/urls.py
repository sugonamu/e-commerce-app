from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_view, name='info_view'),
]
