from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('item/<int:id>', views.get_item, name='get_item'),
    path('items', views.items_list, name='items_list'),
]
