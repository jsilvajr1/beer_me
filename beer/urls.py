from django.urls import path
from . import views


urlpatterns = [
    path('', views.beer_list, name='beer_list'),
    path('new', views.new_beer, name='new_beer'),
    path('<int:beer_id>', views.beer_detail, name='beer_detail'),
    path('<int:beer_id>/edit', views.edit_beer, name='edit_beer'),
    path('<int:beer_id>/delete', views.delete_beer, name='delete_beer'),
]