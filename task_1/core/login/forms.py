from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label=('Email'), widget=forms.EmailInput({'class': 'form-control ','placeholder': 'Enter'}))
    password = forms.CharField(required=True, label=('Password'), widget=forms.PasswordInput({'class': 'form-control ','placeholder': 'Password'}))
