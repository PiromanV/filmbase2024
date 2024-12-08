from django.urls import path
from notifications import views

app_name = "notifications"
urlpatterns = [
    path('', views.notifications, name='notifications'),
    path('', views.notification_settings_view, name='notifications_settings')
]
