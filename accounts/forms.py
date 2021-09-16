from django.forms import ModelForm, forms
from django.contrib.auth import get_user_model
User = get_user_model()


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

