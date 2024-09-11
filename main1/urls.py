from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_view, name='home'),
    path('info/', views.info_view, name='info_view'),
    path('add-product/', views.add_product, name='add_product'),
    path('json/', views.products_json, name='products_json'),
    path('json/<int:product_id>/', views.product_json_by_id, name='product_json_by_id'),
    path('xml/', views.show_xml, name='products_xml'),
    path('xml/<int:product_id>/', views.show_xml_by_id, name='product_xml_by_id'),
]
