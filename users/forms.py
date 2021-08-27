from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Mets:
        model = User
        fields = ('username', "password")