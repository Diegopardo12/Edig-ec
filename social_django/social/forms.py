from cProfile import label
from dataclasses import fields
from tkinter import Label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }
class EstudianteForm(ModelForm):
    class Meta:
    	fields = ['nombre', 'apellido', 'cedula', 'correo']
		


