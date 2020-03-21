from .models import University, OriginalDocument
from .forms import CreateUserForm, UploadDocumentForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {})

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('first_name')
                messages.success(
                    request, user + ', sizin, plagiant hesabınız yaradıldı.')
                return redirect('sign_in')
        context = {'form': form}
        return render(request, "sign_up.html", context)

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'İstifadəçi adı və ya parol yanlışdır.')

        context = {}
        return render(request, "sign_in.html", context)

def sign_out(request):
    logout(request)
    return redirect('/')

@login_required(login_url='sign_in')
def upload_document(request):
    context = {}
    form = UploadDocumentForm()
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('result')
    context = {
        'form': form,
    }
    return render(request, 'upload_document.html', context)

@login_required(login_url='sign_in')
def result(request):
    last_uploaded = OriginalDocument.objects.latest('id')
    context = {
        'last_uploaded': last_uploaded
    }
    return render(request, 'result.html', context)