from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run_tasks/', views.run_tasks, name='run_tasks'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line
    path('tablespace-usage/', views.tablespace_usage, name='tablespace_usage'),

    # URL for active sessions
    path('active-sessions/', views.active_sessions, name='active_sessions'),

    # URL for DBA users
    path('dba-users/', views.dba_users, name='dba_users'),
]
