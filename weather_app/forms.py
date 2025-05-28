from django import forms


class CityForm(forms.Form):
    city = forms.CharField(label='Город', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Введите название города',
        'autofocus': 'autofocus',
        'class': 'form-control',
        'autocomplete': 'off'
    }))
