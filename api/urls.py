from django.urls import path
from api import views

urlpatterns = [
    path('', views.get_all_products, name="get_all_products"),
]
