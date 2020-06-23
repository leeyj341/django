from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class UserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']