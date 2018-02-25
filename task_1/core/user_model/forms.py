from django import forms
from django.forms import NumberInput

from app.models import UserModel

class UserModelForms(forms.ModelForm):
    first_name = forms.CharField(required=True, label='Ime i prezime', widget=forms.TextInput(
                                         {'class': 'form-control', 'placeholder': 'Ime '})
                               )

    last_name = forms.CharField(required=True, label='Ime i prezime', widget=forms.TextInput(
                                         {'class': 'form-control', 'placeholder': 'Prezime'})
                               )

    full_name = forms.CharField(required=True, label='Ime i prezime', widget=forms.TextInput(
                                         {'class': 'form-control', 'placeholder': 'Ime i prezime'})
                               )


    password = forms.CharField(required=False, label='Kontakt broj', widget=forms.TextInput(
                                         {'class': 'form-control', 'placeholder': 'Kontakt broj'})
                                )

    email = forms.EmailField(required=False, label='Email igrača', widget=forms.EmailInput(
                                         {'class': 'form-control', 'placeholder': 'Email'})
                                  )

    active = forms.BooleanField(required=False, label='Aktivan', initial=False,
                                widget=forms.CheckboxInput({'class': ''})
                                )

    class Meta:
        model = UserModel
        exclude = ('created_at', 'updated_at')
