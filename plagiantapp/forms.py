from django.forms import ModelForm
from .models import OriginalDocument
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UploadDocumentForm(ModelForm):
    class Meta:
        model = OriginalDocument
        fields = '__all__'
        exclude = ['date_added', 'checked_by']

    def __init__(self, *args, **kwargs):
        super(UploadDocumentForm, self).__init__(*args, **kwargs)
    
    # document
        self.fields['document'].widget.attrs['id'] = 'document'
        self.fields['document'].widget.attrs['class'] = 'form-control'
        self.fields['document'].widget.attrs['placeholder'] = 'Sənəd'
        self.fields['document'].widget.attrs['autocomplete'] = 'off'
        self.fields['document'].widget.attrs['required'] = 'required'
        self.fields['document'].widget.attrs['type'] = 'text'
        self.fields['document'].widget.attrs['name'] = 'document'

    # document title
        self.fields['document_title'].widget.attrs['id'] = 'document_title'
        self.fields['document_title'].widget.attrs['class'] = 'form-control'
        self.fields['document_title'].widget.attrs['placeholder'] = 'Sənədin adı'
        self.fields['document_title'].widget.attrs['autocomplete'] = 'off'
        self.fields['document_title'].widget.attrs['required'] = 'required'
        self.fields['document_title'].widget.attrs['type'] = 'text'
        self.fields['document_title'].widget.attrs['name'] = 'document_title'
    
    # student name
        self.fields['student_name'].widget.attrs['id'] = 'student_name'
        self.fields['student_name'].widget.attrs['class'] = 'form-control'
        self.fields['student_name'].widget.attrs['placeholder'] = 'Tələbənin adı'
        self.fields['student_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['student_name'].widget.attrs['required'] = 'required'
        self.fields['student_name'].widget.attrs['type'] = 'text'
        self.fields['student_name'].widget.attrs['name'] = 'student_name'

    # teacher name
        self.fields['teacher_name'].widget.attrs['id'] = 'teacher_name'
        self.fields['teacher_name'].widget.attrs['class'] = 'form-control'
        self.fields['teacher_name'].widget.attrs['placeholder'] = 'Rəhbərin adı'
        self.fields['teacher_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['teacher_name'].widget.attrs['required'] = 'required'
        self.fields['teacher_name'].widget.attrs['type'] = 'text'
        self.fields['teacher_name'].widget.attrs['name'] = 'teacher_name'

    # document type
        self.fields['document_type'].widget.attrs['id'] = 'document_type'
        self.fields['document_type'].widget.attrs['class'] = 'form-control'
        self.fields['document_type'].widget.attrs['placeholder'] = 'Sənədin növü'
        self.fields['document_type'].widget.attrs['autocomplete'] = 'off'
        self.fields['document_type'].widget.attrs['required'] = 'required'
        self.fields['document_type'].widget.attrs['type'] = 'text'
        self.fields['document_type'].widget.attrs['name'] = 'document_type'

    # university
        self.fields['university'].widget.attrs['id'] = 'university'
        self.fields['university'].widget.attrs['class'] = 'form-control'
        self.fields['university'].widget.attrs['placeholder'] = 'Universitet'
        self.fields['university'].widget.attrs['autocomplete'] = 'off'
        # self.fields['university'].widget.attrs['required'] = 'required'
        self.fields['university'].widget.attrs['type'] = 'text'
        self.fields['university'].widget.attrs['name'] = 'university'

        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

    # first_name
        self.fields['first_name'].widget.attrs['id'] = 'first_name'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ad'
        self.fields['first_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['required'] = 'required'
        self.fields['first_name'].widget.attrs['type'] = 'text'
        self.fields['first_name'].widget.attrs['name'] = 'first_name'

    # last_name
        self.fields['last_name'].widget.attrs['id'] = 'last_name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Soyad'
        self.fields['last_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['last_name'].widget.attrs['required'] = 'required'
        self.fields['last_name'].widget.attrs['type'] = 'text'
        self.fields['last_name'].widget.attrs['name'] = 'last_name'

    # email
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Elektron Poçt'
        self.fields['email'].widget.attrs['autocomplete'] = 'off'
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['name'] = 'email'

    # username
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'İstifadəçi Adı'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['required'] = 'required'
        self.fields['username'].widget.attrs['type'] = 'username'
        self.fields['username'].widget.attrs['name'] = 'username'

    # password
        self.fields['password1'].widget.attrs['id'] = 'password1'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'İstifadəçi Parolu'
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password1'].widget.attrs['required'] = 'required'
        self.fields['password1'].widget.attrs['name'] = 'password1'

    # confirm password
        self.fields['password2'].widget.attrs['id'] = 'password2'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Parolu Təkrar Edin'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['required'] = 'required'
        self.fields['password2'].widget.attrs['name'] = 'password2'