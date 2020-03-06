from django.core.exceptions import ValidationError
from django import forms
import re

def notValidStep(value):
    reg = r"\d+"
    if value and re.match(reg, str(value)) is not None and 1 <= value <= 30:
        pass
    else:
        raise ValidationError("Ожидается положительное целочисленное число в диапозоне 1 - 30")