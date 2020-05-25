from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('overview/', views.overview, name='overview'),
  path('edittodo/<int:pk>/', views.edittodo, name='edittodo'),
  path('newtodo/', views.newtodo, name='newtodo'),
  path('impressum/', views.impressum, name='impressum'),
]