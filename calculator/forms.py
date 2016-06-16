from django import forms
from calculator.models import Operation


class NumberForm(forms.ModelForm):
    choices = [("+", "+"), ("-", "-"), ("*", "*"), ("/", "/")]
    number1 = forms.FloatField()
    operators = forms.ChoiceField(choices, required=True)
    number2 = forms.FloatField()

    class Meta:
        model = Operation
        fields = ["number1", "operators", "number2"]


