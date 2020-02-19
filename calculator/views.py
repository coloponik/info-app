import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalcForm

def calculator(request):

    if (request.method == 'POST'):
        calcform = CalcForm(request.POST)
        if calcform.is_valid():
            creditAmount = calcform.cleaned_data["creditAmount"]
            creditRate = calcform.cleaned_data["creditRate"]
            creditPeriod = calcform.cleaned_data["creditPeriod"]
            paymentStep = calcform.cleaned_data["paymentStep"]
            context = {'form': calcform}
            return render(request, 'calculator/calculator.html', {'form': calcform})
            # return HttpResponse("<h2>Hello, {0}</h2>".format(creditAmount))
    
    else:
        calcform = CalcForm()
        return render(request, 'calculator/calculator.html', {'form': calcform})