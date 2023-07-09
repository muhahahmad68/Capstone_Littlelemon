from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='sayHello'),
    path('items', views.MenuItemView.as_view(), name='menu'),
    path('items/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu'),
]