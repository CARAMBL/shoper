from  django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from  django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={"class":"focus:outline-none","placeholder":"Email"}))
    username =forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"focus:outline-none","placeholder":"Usename"}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class":"focus:outline-none","placeholder":"Password"}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class":"focus:outline-none","placeholder":"Password"}))

    class Meta:
        model = User
        fields = ("email","username","password1","password2",)
#
# def save (self, commit = False):
#     user = super (NewUserForm, self).save(cammit=False)
#     user.email = self.cleaned_data('email')
#     if commit:
#         # user.save()