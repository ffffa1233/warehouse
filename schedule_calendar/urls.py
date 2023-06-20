from django.urls import path

from . import views

app_name = 'schedule_calendar'

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.calendar_events, name='calendar_events'),
    path('callback/', views.callback, name='callback'),
]
