from django import forms


class NumberForm(forms.Form):
    choices = [("+", "+"), ("-", "-"), ("*", "*"), ("/", "/")]
    number1 = forms.FloatField()
    operators = forms.ChoiceField(choices, required=True)
    number2 = forms.FloatField()

