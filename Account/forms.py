from django import forms
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField()
    email=forms.EmailField()

