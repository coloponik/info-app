from django import forms
from django.core.validators import RegexValidator
from .annotations.NotValidSum import notValidSum
from .annotations.NotValidRate import notValidRate
from .annotations.NotValidTerm import notValidTerm
from .annotations.NotValidStep import notValidStep
import re

class CalcForm(forms.Form):
    creditAmount = forms.FloatField(error_messages=
        {
            'required':'Este campo es requerido'
        },
        validators=[notValidSum],
        min_value=20000.00,
        max_value=3000000.00,
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control', 
            'id': 'creditAmount', 
            'name': 'creditAmount',
            'placeholder': 'Введите сумму'
        })
    )
    creditRate = forms.FloatField(
        validators=[notValidRate],
        min_value=0.50,
        max_value=25.00,
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control', 
            'id': 'creditRate', 
            'name': 'creditRate',
            'placeholder': 'Введите ставку'
        })
    )
    creditPeriod = forms.FloatField(
        validators=[notValidTerm],
        min_value=1,
        max_value=90,
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control', 
            'id': 'creditPeriod', 
            'name': 'creditPeriod',
            'placeholder': 'Введите срок'
        })
    )
    paymentStep = forms.FloatField(
        validators=[notValidStep],
        initial=1,
        min_value=1,
        max_value=30,
        widget=forms.TextInput(attrs=
        {
            'class': 'form-control', 
            'id': 'paymentStep', 
            'name': 'paymentStep',
            'placeholder': 'Введите шаг'
        })
    )
    radio = forms.ChoiceField(
        widget=forms.RadioSelect(attrs=
        {
            'id': 'radio',
            'class': 'form-check-input', 
            'name': 'radio'
        }),
        choices=[('true', 'в год'), ('false', 'в день')]
    )
