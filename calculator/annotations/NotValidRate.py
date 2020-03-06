from django.core.exceptions import ValidationError
from django import forms
import re

def notValidRate(value):
    reg = r"\d+([.]\d{1,2})?"
    if value and re.match(reg, str(value)) is not None and 0.50 <= value <= 25.00:
        pass
    else:
        raise ValidationError("Ожидается положительное число (до 2х знаков после '.') в диапозоне 0.50 - 25.00")