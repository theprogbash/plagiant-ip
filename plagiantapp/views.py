from .models import Account, University
from .forms import SignUpForm, SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

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

#     if request.user.is_authenticated:
#         return render(request, 'index.html')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             form = AuthenticationForm(request.POST)
#             return render(request, 'sign_in.html', {'form': form})
#     else:
#         form = AuthenticationForm()
#         return render(request, 'sign_in.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('/')    