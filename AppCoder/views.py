from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm , CursoForm, ProfesorForm, EstudianteForm, BuscarCursoForm, EditProfileForm
from .models import Curso, PerfilUsuario
from django.contrib.auth.models import Group
from .decorators import rol_requerido

def inicio(request):
    return render(request, 'inicio.html')

@login_required
@rol_requerido("profesor")
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso creado correctamente.')
            return redirect('crear_curso')
    else:
        form = CursoForm()
    return render(request, 'curso_form.html', {'form': form})

@login_required
@rol_requerido("profesor")
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profesor creado correctamente.')
            return redirect('crear_profesor')
    else:
        form = ProfesorForm()
    return render(request, 'profesor_form.html', {'form': form})

@login_required
@rol_requerido("alumno")
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante creado correctamente.')
            return redirect('crear_estudiante')
    else:
        form = EstudianteForm()
    return render(request, 'estudiante_form.html', {'form': form})

@login_required
def buscar_curso(request):
    resultado = None
    form = BuscarCursoForm(request.GET or None)
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            resultado = Curso.objects.filter(nombre__icontains=nombre)
        else:
            resultado = Curso.objects.none()
    return render(request, 'buscar_curso.html', {'form': form, 'resultado': resultado})

# AUTH VIEWS
def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            rol = form.cleaned_data["rol"]
            PerfilUsuario.objects.create(user=user, rol=rol)
            login(request, user)
            return redirect("inicio")
    else:
        form = RegistroUsuarioForm()
    return render(request, "registro.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Has iniciado sesión.')
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada.')
    return redirect('inicio')

@login_required
def edit_profile(request):
    user = request.user
    perfil = PerfilUsuario.objects.get(user=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
        
            form.save()
            
            perfil.rol = form.cleaned_data['rol']
            perfil.save()
            return redirect('/')  
    else:
        
        form = EditProfileForm(instance=user, initial={'rol': perfil.rol})

    return render(request, 'edit_profile.html', {'form': form})

# custom 404
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
