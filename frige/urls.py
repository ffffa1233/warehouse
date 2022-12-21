from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:frige_id>/', views.delete, name='delete'),
    path('update/<int:frige_id>/', views.update, name='update'),
    path('update/<int:frige_id>/updaterecord/', views.updaterecord, name='updaterecord'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
]
