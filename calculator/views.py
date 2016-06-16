from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from calculator.forms import NumberForm
from calculator.models import Operation


def user_create_view(request):
    if request.POST:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home_view"))
        else:
            return render(request, "user_create.html", {"form": form})
    form = UserCreationForm()
    return render(request, "user_create.html", {"form": form})


@login_required
def profile_view(request):
    print(request.user)
    profile_data = {
        "data": list(Operation.objects.filter(user=request.user))
    }
    return render(request, "profile.html", profile_data)


def calculator_view(request):
    result = ''
    number1 = ''
    number2 = ''
    operators = ''
    all_data = ''
    form = NumberForm()
    print(request.POST)
    if request.POST:
        form = NumberForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            operators = form.cleaned_data['operators']
            if operators == '+':
                result = number1 + number2
            elif operators == '-':
                result = number1 - number2
            elif operators == '*':
                result = number1 * number2
            elif operators == '/':
                result = number1 / number2
        if request.user.is_authenticated():
            Operation.objects.create(number1=number1, number2=number2, operators=operators, result=result, user=request.user)




    return render(request, 'calc.html', {'form': form, 'result': result, 'number1': number1, 'number2': number2, 'operators': operators})
