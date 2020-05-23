from django.contrib import admin
from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('overview', views.index, name='index'),
    path('<int:Todo_id>/', views.edit, name='edit'),
    path('<int:Todo_id>/edit/', views.edit, name='edit'),
    path('<int:Todo_id>/delete/', views.edit, name='delete'),
    path('newtodo', views.new, name='newtodo'),
    path('impressum', views.impressum, name='impressum'),
    path('admin/', admin.site.urls),
]
