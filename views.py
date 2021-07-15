from django.shortcuts import render, redirect
from .forms import RegisterForm, RestoForm, ItemForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} your account is created')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')

def add_resto(request):
    form = RestoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item')
    return render(request, 'user/resto.html', {'form': form})

def add_items(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'user/items.html', {'form':form})
