import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .forms import *
from .calc import *

def calculator(request):

    if (request.method == 'POST'):
        calcform = CalcForm(request.POST)
        if calcform.is_valid():
            payments = []
            creditAmount = calcform.cleaned_data["creditAmount"]
            creditRate = calcform.cleaned_data["creditRate"]
            creditPeriod = calcform.cleaned_data["creditPeriod"]
            paymentStep = calcform.cleaned_data["paymentStep"]
            radio = calcform.cleaned_data["radio"]
            if ((radio == "false") and (creditPeriod % paymentStep != 0)):
                raise ValidationError("Срок кредита должен быть кратен шагу платежа")
            # if ((radio == "false") and (creditPeriod % paymentStep != 0) and (paymentStep == 1)):
            #     raise ValidationError("Срок кредита должен быть кратен шагу платежа")
            if radio == "true":
                payments = PaymentScheduleForYearRate(creditAmount, creditRate, creditPeriod, paymentStep)
            elif radio == "false":
                payments = PaymentScheduleForDayRate(creditAmount, creditRate, creditPeriod, paymentStep)
            try:
                context = {'form': calcform, 'payments': payments["calc"], 'payPer': payments["payPer"], 'totalOverpay': payments["totalOverpay"]}
            except Exception as e:
                raise TypeError('Невозможно произвести вычисления')
            return render(request, 'calculator/calculator.html', context)
        else:
            return render(request, 'calculator/calculator.html', {'form': calcform})
    else:
        calcform = CalcForm()
        return render(request, 'calculator/calculator.html', {'form': calcform})