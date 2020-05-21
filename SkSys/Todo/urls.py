from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('overview', views.index, name='index'),
    path('<int:Todo_id>/', views.detail, name='detail'),
    path('<int:Todo_id>/edit/', views.edit, name='edit'),
    path('newtodo', views.new, name='new_Todo'),
    path('impressum', views.impressum, name='impressum'),
]
