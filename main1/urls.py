from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_view, name='home'),  # Map the root URL to `info_view`
    path('info/', views.info_view, name='info_view'),
]
