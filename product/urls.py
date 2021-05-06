# Created
from django.urls import path
from product import views

urlpatterns = [
    # name parameter is for href linking
    path("product/", views.product, name="product"),
]
