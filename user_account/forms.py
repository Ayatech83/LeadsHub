from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    #A form that creates the user, with no priviledges, from the given email and password.
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "contact_number",
                  "company_name",
                  "company_reg_number",
                  "company_address",
                  "area_code",
                  "commodities"
                  )
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.contact_number = self.cleaned_data['contact_number']
        user.company_name = self.cleaned_data['company_name']
        user.company_reg_number = self.cleaned_data['company_reg_number']
        user.area_code = self.cleaned_data['area_code']
        user.commodities = self.cleaned_data['commodities']

        if commit:
            user.save()

        return user

class CustomUserChangeForm(UserChangeForm):
    #A form for updating all the users. Includes all the fields on
    #the user, but replaces the password field with admin's password hash display field.
    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = "__all__"