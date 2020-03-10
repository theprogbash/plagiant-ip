from django import forms
from .models import Account

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
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
        self.fields['password'].widget.attrs['id'] = 'password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'İstifadəçi Parolu'
        self.fields['password'].widget.attrs['autocomplete'] = 'off'
        self.fields['password'].widget.attrs['required'] = 'required'
        self.fields['password'].widget.attrs['name'] = 'password'
    
        # university_name
        self.fields['university_name'].widget.attrs['id'] = 'university_name'
        self.fields['university_name'].widget.attrs['name'] = 'university_name'
        self.fields['university_name'].widget.attrs['class'] = 'form-control'

        # physical_account
        self.fields['isPhysicalAccount'].label = "Şəxsi İstifadəçiyəm"

class SignInForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username','password')

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)

        # username
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'İstifadəçi Adı'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['required'] = 'required'
        self.fields['username'].widget.attrs['type'] = 'username'
        self.fields['username'].widget.attrs['name'] = 'username'

        # password
        self.fields['password'].widget.attrs['id'] = 'password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'İstifadəçi Parolu'
        self.fields['password'].widget.attrs['autocomplete'] = 'off'
        self.fields['password'].widget.attrs['required'] = 'required'
        self.fields['password'].widget.attrs['name'] = 'password'