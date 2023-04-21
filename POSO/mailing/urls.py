from django.urls import path
from mailing import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('send_email/', views.send_email, name='send_email'),
]
