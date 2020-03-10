from .models import Account, University
from .forms import SignUpForm, SignInForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html', {})

def sign_up(request):
    context = {}
    form = SignUpForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = SignUpForm(request.POST or None, request.FILES or None)
    context['form'] = form
    return render(request, "sign_up.html", context)


def sign_in(request):
    context = {}
    form = SignInForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        return redirect('/')
    else:
        form = SignInForm(request.POST or None, request.FILES or None)
    context['form'] = form
    return render(request, "sign_in.html", context)

def sign_out(request):
    logout(request)
    return redirect('/')    