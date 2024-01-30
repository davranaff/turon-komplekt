from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug>/', views.detail, name='detail'),
    path('products/', views.all_products, name='products'),
    path('objects/', views.all_objects, name='objects'),
    path('feedback/', views.feedback, name='feedback')
]
