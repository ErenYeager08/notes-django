from django import forms
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NoteAddForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets= {
            "title" : forms.TextInput(attrs={ 'class': 'form-control' }),
            "text" : forms.Textarea(attrs={ 'class': 'form-control' })

        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets= {
            "username" : forms.TextInput(attrs={ 'class': 'form-control' }),
            "password1" : forms.PasswordInput(attrs={ 'class': 'form-control' }),
            "password2" : forms.PasswordInput(attrs={ 'class': 'form-control' })

        }