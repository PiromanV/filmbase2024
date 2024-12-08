from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from notifications.models import Notification, NotificationSettings
from notifications.forms import NotificationSettingForm


def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by(
            'created_at')
    return render(
            request,
            'notifications/notifications.html',
            {'notifications': notifications}
            )


@login_required
def notification_settings_view(request):
    notification_settings, created = (
            NotificationSettings.objects.get_or_create(user=request.user)
            )

    if request.method == 'POST':
        form = NotificationSettingForm(
                request.POST,
                instance=notification_settings
               )
        if form.is_valid():
            form.save()
            return redirect('notification_settings/notification_settings')
    else:
        form = NotificationSettingForm(instance=notification_settings_view)

    return render(
            request,
            'notification_settings/notification_settings.html',
            {'form': form}
            )
