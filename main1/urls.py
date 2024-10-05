from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.info_view, name='home'),
    path('info/', views.info_view, name='info_view'),
    path('add-product/', views.add_product, name='add_product'),
    path('json/', views.products_json, name='products_json'),
    path('json/<int:product_id>/', views.product_json_by_id, name='product_json_by_id'),
    path('xml/', views.show_xml, name='products_xml'),
    path('xml/<int:product_id>/', views.show_xml_by_id, name='product_xml_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('edit-product/<uuid:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<uuid:product_id>', views.delete_product, name='delete_product'),
    path('error/', views.error, name='error'),
    path('create-ajax/', views.create_product_ajax, name='create_product_ajax'),

]
