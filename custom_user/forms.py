from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    #A form that creates the user, with no privilaedges, from the given email and password.
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    #A form for updating all the users. Includes all the fields on
    #the user, but replaces the password field with admin's password hash display field.
    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser