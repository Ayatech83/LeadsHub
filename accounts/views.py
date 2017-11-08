from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import SubscribeForm

def subscribe_view(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about')
    else:
        form = SubscribeForm()
        args = {'form': form}
        return render(request, 'accounts/subscribe.html', args)


