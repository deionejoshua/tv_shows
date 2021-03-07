
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('create_show', views.create_show),
    path('shows/<int:Shows_id>', views.display_show),
    path('shows/<int:Shows_id>/edit', views.edit_shows),
    path('shows/<int:Shows_id>/update', views.update_show),
    path('shows/<int:Shows_id>/delete', views.delete)


]
