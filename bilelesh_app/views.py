from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from .forms import BookForm

def index(request):
    return render(request, 'bilelesh/index.html')

@csrf_protect
def book(request):
    if request == "POST":
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

        # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()

    return render(request, "bilelesh/index.html", {"form": form})
