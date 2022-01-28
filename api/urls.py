from django.urls import path
from api import views

urlpatterns = [
    path('get_all_products', views.get_all_products, name="get_all_products"),
    path('get_product/<str:pk>', views.get_product, name="get_product"),
]
