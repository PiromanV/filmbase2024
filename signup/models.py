from django.db import models
from django.contrib.auth.models import User

from films.models import Actor


class NotificationSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notify_on_movie_update = models.BooleanField(default=False)
    notify_on_actor_update = models.BooleanField(default=False)
    notify_on_new_movie = models.BooleanField(default=False)
    frequency = models.CharField(max_length=20, choices=[
        ('immediate', 'Сразу после внесения данных'),
        ('weekly', 'Раз в неделю'),
        ('montly', 'Раз в месяц'),
    ])
    followed_actors = models.ManyToManyField(Actor, blank=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextFiels()
    created_at = models.DateTimeFIeld(auto_now_add=True)
    is_read = models.BooleanField(default=False)
