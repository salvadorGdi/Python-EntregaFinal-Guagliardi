from django.contrib import admin
from django.urls import path
from AppCoder import views
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('crear_profesor/', views.crear_profesor, name='crear_profesor'),
    path('crear_estudiante/', views.crear_estudiante, name='crear_estudiante'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso'),

    # Auth
    path('register/', views.registro_usuario, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]

handler404 = 'AppCoder.views.custom_404_view'
