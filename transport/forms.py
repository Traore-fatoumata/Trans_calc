from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Marchandise, Cargaison

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class MarchandiseForm(forms.ModelForm):
    class Meta:
        model = Marchandise
        fields = ['numero', 'nom', 'poids', 'volume', 'type_cargaison']
        labels = {
            'nom': 'Nom de la marchandise',
        }

class CargaisonForm(forms.ModelForm):
    class Meta:
        model = Cargaison
        fields = ['type_cargaison', 'distance', 'marchandises']