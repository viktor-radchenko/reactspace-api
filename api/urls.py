from django.urls import path
from api import views

urlpatterns = [
    path('get_all_products', views.get_all_products, name="get_all_products"),
]
