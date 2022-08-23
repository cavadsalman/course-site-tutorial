from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Teacher, Student


class LoginForm(forms.Form):
    user_info = forms.CharField(max_length=100, label='Email or Username')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label="Password Again")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email).exists():
                raise ValidationError('Bele bir email movcuddur!', code='exist-email')

        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            if not username.isidentifier():
                raise ValidationError('Username duzgun yazilmayib!', code='wrong-username')
            elif not username.islower():
                raise ValidationError('Username ancaq kicik herflerden ibaret olmalidir!', code='lower-username')
            elif User.objects.filter(username=username).exists():
                raise ValidationError('Bele bir username movcuddur!', code='exsist-user')

        return username

    def clean(self):
        cleaned_data = super().clean()

        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('password2')

        if pass1 and pass2:
            if pass1 != pass2:
                raise ValidationError('Sifreler bir-birine beraber deyil!', code='not-same-passwords')
            elif pass1.isupper() or pass1.islower():
                raise ValidationError('Sifrede en az bir kicik ve ya boyuk herf olmalidir!', code='case-error')
            elif pass1.isnumeric():
                raise ValidationError('Sifrede en az 1 herf olmalidir', code='only-letter')
            elif pass1.isalpha():
                raise ValidationError('Sifrede en az 1 reqem olmalidir', code='nonly-digit')
            elif not pass1.isalnum():
                raise ValidationError('Sifre yalniz herf ve reqemlerden ibaret olmalidir!')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['user']


