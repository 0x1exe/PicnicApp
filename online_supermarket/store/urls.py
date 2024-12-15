from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('catalog/', views.catalog_page, name='catalog_page'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('download/',views.download_page,name='download_page')
]