from django.shortcuts import render
from django.views.generic import ListView

from .models import Example


# Create your views here.

class HomePage(ListView):
    model = Example
    template_name = 'index.html'
    context_object_name = 'items'


def add_item(request):
    if request.method == 'POST':
        form = request.POST
        data = {}
        for i, k in form.items():
            if i != 'csrfmiddlewaretoken':
                data[i] = k
        Ex = Example(data=data)
        Ex.save()

        return render(request, 'add_form.html')
    return render(request, 'add_form.html')
