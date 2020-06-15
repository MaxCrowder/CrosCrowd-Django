from django.shortcuts import render
from .forms import ContactForm


def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()

    args = {
        'form': form,
    }
    return render(request, 'index.html', args)
