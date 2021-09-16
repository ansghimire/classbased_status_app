from django.forms import ModelForm
from .models import UserStatus


class UserStatusModelForm(ModelForm):
    class Meta:
        model = UserStatus
        fields = ['status']

