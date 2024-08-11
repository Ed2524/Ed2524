# from django.urls import path
# from .views import product_list, product_create, product_detail

# urlpatterns = [
#     path('', product_list, name='product_list'),
#     path('product/create/', product_create, name='product_create'),
#     path('product/<int:pk>/', product_detail, name='product_detail')
    
# ] 

from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name = "product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail")
]
