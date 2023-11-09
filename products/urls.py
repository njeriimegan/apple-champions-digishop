from django.urls import path
from . import views as myviews

urlpatterns = [
    path('products/', myviews.products, name='products-url'),
    path('add-products/', myviews.add_products, name='add-products-url')
]
