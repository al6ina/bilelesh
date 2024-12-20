from django.urls import path

from . import views

app_name = 'bilelesh'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.index, name='book')
]