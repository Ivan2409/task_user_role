from django import forms
from django.forms import NumberInput

from app.models import UserModel, UserDetails



class UserDetailsForm(forms.ModelForm):
    address = forms.CharField(required=True, label='Adresa', widget=forms.TextInput(
        {'class': 'form-control', 'placeholder': 'Adresa '})
                              )

    phone_number = forms.CharField(required=True, label='Broj telefona', widget=forms.TextInput(
        {'class': 'form-control', 'placeholder': 'Broj telefona '})
                                   )

    postal_code = forms.IntegerField(required=False, label='Poštanski broj',
                                     widget=NumberInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Poštanski broj'})
                                     )

    date_of_birth = forms.DateField(required=True, label='Datum rođenja',
                                    widget=forms.DateInput(
                                        attrs={'class': 'form-control datepicker col-md-12 col-xs-12',
                                               'placeholder': 'YYYY/MM/DD'}, format="%Y/%m/%d"),
                                    input_formats=['%Y/%m/%d'])

    gender = forms.CharField(required=True, label='Spol', widget=forms.TextInput(
        {'class': 'form-control', 'placeholder': 'Spol '})
                             )

    avatar = forms.ImageField(required=False, label='Fotografija korisnika')

    active = forms.BooleanField(required=False, label='Aktivan', initial=False,
                                widget=forms.CheckboxInput({'class': ''})
                                )

    user = forms.ModelChoiceField(queryset=UserModel.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control selectpicker col-md-12 col-xs-12 ', 'id': 'usermodel'}),
                                  label='Korisnik', initial='---',
                                  )




    class Meta:
        model = UserDetails
        exclude = ('created_at', 'updated_at')
