from django.core.exceptions import ValidationError
from django import forms
import re

def notValidTerm(value):
    reg = r"\d+"
    if value and re.match(reg, str(value)) is not None and 1 <= value <= 90:
        pass
    else:
        raise ValidationError("Ожидается положительное целочисленное число в диапозоне 1 - 90")