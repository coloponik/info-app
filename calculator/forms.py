from django import forms

class CalcForm(forms.Form):
    creditAmount = forms.FloatField(min_value=20000.00, max_value=50000.00, widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'creditAmount', 
            'placeholder': 'Введите сумму'
        }))
    creditRate = forms.FloatField(min_value=0.50, max_value=25.00, widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'creditRate', 
            'placeholder': 'Введите ставку'
        }))
    creditPeriod = forms.FloatField(min_value=1, max_value=60, widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'creditPeriod', 
            'placeholder': 'Введите срок'
        }))
    paymentStep = forms.FloatField(min_value=1, max_value=30, widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'paymentStep', 
            'placeholder': 'Введите шаг'
        }))

        #---------------------------------------------------------------------------------------

        # class Meta:
    #     fields = ['creditAmount', 'creditRate', 'creditPeriod', 'paymentStep']
    #     widgets = {'creditAmount' : TextInput(attrs={
    #         'class': 'form-control', 
    #         'id': 'creditAmount', 
    #         'placeholder': 'Введите сумму'
    #     }),
    #     'creditRate' : TextInput(attrs={
    #         'class': 'form-control', 
    #         'id': 'creditRate', 
    #         'placeholder': 'Введите ставку'
    #     }),
    #     'creditPeriod' : TextInput(attrs={
    #         'class': 'form-control', 
    #         'id': 'creditPeriod', 
    #         'placeholder': 'Введите срок'
    #     }),
    #     'paymentStep' : TextInput(attrs={
    #         'class': 'form-control', 
    #         'id': 'paymentStep', 
    #         'placeholder': 'Введите шаг'
    #     })}