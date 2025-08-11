Instrucciones rápidas:

1. Instalar dependencias:
   pip install -r requirements.txt

2. Migraciones:
   python manage.py makemigrations
   python manage.py migrate

3. Crear superuser si se desea acceder al admin (y escribir en el buscador /admin/):
   python manage.py createsuperuser

4. Ejecutar el servidor:
   python manage.py runserver

5. Para probar la página 404, ponga DEBUG=False en settings.py y agregue los ALLOWED_HOSTS.
