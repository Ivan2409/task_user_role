from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, label=('Email'),
                            widget=forms.EmailInput({'class': 'form-control ', 'placeholder': 'Enter'}))

    password = forms.CharField(required=True, label=('Password'),
                               widget=forms.PasswordInput({'class': 'form-control ', 'placeholder': 'Password'}))

    repeat_password = forms.CharField(required=True, label=('Password'),
                                      widget=forms.PasswordInput({'class': 'form-control ','placeholder': 'Password'}))

    first_name = forms.CharField(required=True, label='Ime i prezime', widget=forms.TextInput(
        {'class': 'form-control', 'placeholder': 'Ime '})
                                 )

    last_name = forms.CharField(required=True, label='Ime i prezime', widget=forms.TextInput(
        {'class': 'form-control', 'placeholder': 'Prezime'})
                                )
