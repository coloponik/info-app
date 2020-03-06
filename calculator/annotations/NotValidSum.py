from django.core.exceptions import ValidationError
from django import forms
import re

def notValidSum(value):
    reg = r"\d+([.]\d{1,2})?"
    if value and re.match(reg, str(value)) is not None and 20000.00 <= value <= 3000000.00:
        pass
    else:
        raise ValidationError("Ожидается положительное число (до 2х знаков после '.') в диапозоне 20000.00 - 3000000.00")