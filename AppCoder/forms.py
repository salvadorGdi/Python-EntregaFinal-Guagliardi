from django import forms
from .models import Curso, Profesor, Estudiante, PerfilUsuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    rol = forms.ChoiceField(choices=PerfilUsuario.ROL_CHOICES, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "rol"]

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'email']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'curso']

class BuscarCursoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del curso", required=False)

class EditProfileForm(forms.ModelForm):
    rol = forms.ChoiceField(choices=PerfilUsuario.ROL_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {'username': 'Nuevo nombre de usuario'}

    def clean_username(self):
        username = self.cleaned_data.get('username')
       
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username
    