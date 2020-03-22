from .models import University, OriginalDocument
from .forms import CreateUserForm, UploadDocumentForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import glob

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

    original = open(str(last_uploaded.document), 'r')
    original_words = original.read().lower().split()
    report = open("static/report_documents/" + str(last_uploaded.document_title) + ".txt", 'w')
    found_count, fives_count = 0, 0
    path = 'static/other_documents/doc*.txt'
    files = glob.glob(path)

    def iterate():
        for i in range(len(original_words) - 4):
            for j in range(len(original_words)+1):
                if(j-i == 5):
                    original_each_five = original_words[i:j]
                    yield original_each_five
                else:
                    pass

    for each_file in files:
        other_docs = open(each_file, 'r')
        other_docs_words = other_docs.read().lower().split()

        for i in range(len(other_docs_words) - 4):
            for j in range(len(other_docs_words)+1):
                if(j-i == 5):
                    each_five_others = other_docs_words[i:j]
                    for original_each_five in iterate():
                        if(original_each_five == each_five_others):
                            found_count += 1
                            report.write('{} hissəsi {} sənədində tapıldı.\n'.format(
                                original_each_five, each_file))
                        else:
                            pass
                else:
                    pass

    for original_each_five in iterate():
        fives_count += 1

    percentage = found_count/fives_count
    rounded_percentage = round(percentage, 2)*100
    percentage_for_chart = round(rounded_percentage)

    report.write('Plagiat faizi: {}%'.format(round(percentage, 2)*100))

    context = {
        'last_uploaded': last_uploaded,
        'found_count': found_count,
        'fives_count': fives_count,
        'rounded_percentage': rounded_percentage,
        'percentage_for_chart': percentage_for_chart
    }

    return render(request, 'result.html', context)