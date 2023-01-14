from django.urls import path

from . import views

app_name = 'notice'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:notice_id>/', views.delete, name='delete'),
    path('update/<int:notice_id>/', views.update, name='update'),
    path('update/<int:notice_id>/updaterecord/', views.updaterecord, name='updaterecord'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
]
