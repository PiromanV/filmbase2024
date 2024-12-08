from django import forms
from notifications.models import NotificationSetting


class NotificationSettingForm(forms.ModelForm):
    class Meta:
        model = NotificationSetting
        fields = [
                'notify_on_movie_update',
                'notify_on_new_movie',
                'notify_on_actor_update',
                'followed_actors',
                'frequency',
        ]
        widgets = {
            'followed_actors': forms.CheckboxSelectMultiple(),
        }
