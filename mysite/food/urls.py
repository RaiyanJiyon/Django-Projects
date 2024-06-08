from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    #food/
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name="detail"),
    #food/item
    path('item/', views.item, name='item'),
    # add item
    path('add/', views.create_item, name='create_item'),
    # update item
    path('update/<int:id>/', views.update_item, name='update_item')
]
