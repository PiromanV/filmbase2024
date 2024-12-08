from django.core.mail import send_mail
from django.conf import settings


def send_email_notification(user, message):
    send_mail(
            'Уведомление из Каталога Фильмов',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.mail],
            fail_silently=False,
    )

