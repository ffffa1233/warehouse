from django.urls import path

from . import views

app_name = 'frige'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:frige_id>/', views.delete, name='delete'),
    path('update/<int:frige_id>/', views.update, name='update'),
    path('update/<int:frige_id>/updaterecord/', views.updaterecord, name='updaterecord'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('updateToFrige/<int:frige_id>/', views.updateToFrige, name='updateToFrige'),
    path('updateToIce/<int:frige_id>/', views.updateToIce, name='updateToTce'),
    path('updateToCupboard/<int:frige_id>/', views.updateToCupboard, name='updateToCupboard'),
]
