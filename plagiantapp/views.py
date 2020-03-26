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

def search_by_count(last_uploaded, difference, original_words, report, files):
    rows = []

    found_count, fives_count = 0, 0
    
    fives_for_report, founded_docs_for_report = [], []

    def iterate():
        for i in range(len(original_words) - (difference-1)):
            for j in range(len(original_words)+1):
                if(j-i == difference):
                    original_each_five = original_words[i:j]
                    yield original_each_five
                else:
                    pass

    for each_file in files:
        other_docs = open(each_file, 'r')
        other_docs_words = other_docs.read().lower().split()

        for i in range(len(other_docs_words) - (difference-1)):
            for j in range(len(other_docs_words)+1):
                if(j-i == difference):
                    each_five_others = other_docs_words[i:j]
                    for original_each_five in iterate():
                        if(original_each_five == each_five_others):

                            fives_for_report.append(original_each_five)
                            founded_docs_for_report.append(each_file)
                            rows = zip(fives_for_report,
                                       founded_docs_for_report)

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
    rounded_percentage = int(round(percentage, 2)*100)
    percentage_for_chart = round(rounded_percentage)

    report.write('Plagiat faizi: {}%'.format(round(percentage, 2)*100))

    return found_count, fives_count, rounded_percentage, percentage_for_chart, fives_for_report, founded_docs_for_report, rows

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
    #region variables
    # Gets the last uploaded document
    last_uploaded = OriginalDocument.objects.latest('id')
    # Opens the las uploaded document
    original = open(str(last_uploaded.document), 'r')
    # Reads the last uploaded document after opening it
    original_words = original.read().lower().split()
    # Shows up number of WORDS in document
    words_count = len(original_words)
    # Opens the original document, reads it, and returns number of characters
    open_original = open(str(last_uploaded.document), "r")
    read_original = open_original.read()
    characters_count = len(read_original)
    # Makes report about result
    report = open("static/report_documents/" + str(last_uploaded.student_name) + 
    "-" + str(last_uploaded.document_title) + ".txt", 'w')
    # Path to the documents with which original doc is comparing
    path = 'static/other_documents/doc*.txt'
    files = glob.glob(path)
    #endregion

    found_count, fives_count, rounded_percentage, percentage_for_chart, fives_for_report, founded_docs_for_report, rows = search_by_count(last_uploaded, 5, original_words, report, files)

    context = {
        'last_uploaded': last_uploaded,
        'found_count': found_count,
        'fives_count': fives_count,
        'rounded_percentage': rounded_percentage,
        'percentage_for_chart': percentage_for_chart,
        'fives_for_report': fives_for_report,
        'founded_docs_for_report': founded_docs_for_report,
        'rows': rows,
        'words_count': words_count,
        'characters_count': characters_count,
    }

    return render(request, 'result.html', context)
