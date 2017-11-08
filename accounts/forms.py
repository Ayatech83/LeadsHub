from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm

class SubscribeForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            #'cell_num',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(SubscribeForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        #user.cell_num = self.cleaned_data['cell_num']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
