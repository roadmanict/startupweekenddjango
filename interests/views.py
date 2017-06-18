from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import InterestForm


def index(request: object) -> object:
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect('/thanks/')
    else:
        form = InterestForm()

    return render(request, 'interest.html', {'form': form})


def thanks(request: object) -> object:
    return render(request, 'thanks.html')