from django.shortcuts import render
from calculator.forms import NumberForm

# Create your views here.


def index_view(request):
    result = ''
    number1 = ''
    number2 = ''
    operators = ''
    form = NumberForm()
    print(request.POST)
    if request.POST:
        form = NumberForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            operators = form.cleaned_data['operators']
            if form.cleaned_data['operators'] == '+':
                result = form.cleaned_data['number1'] + form.cleaned_data['number2']
            if form.cleaned_data['operators'] == '-':
                result = form.cleaned_data['number1'] - form.cleaned_data['number2']
            if form.cleaned_data['operators'] == '*':
                result = form.cleaned_data['number1'] * form.cleaned_data['number2']
            if form.cleaned_data['operators'] == '/':
                result = form.cleaned_data['number1'] / form.cleaned_data['number2']

    return render(request, 'calc.html', {'form': form, 'result': result, 'number1': number1, 'number2': number2, 'operators': operators})
