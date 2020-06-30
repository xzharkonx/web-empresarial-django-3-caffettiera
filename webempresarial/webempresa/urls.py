"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from core import views
#Se importa para poder trabajar con las imagenes
from django.conf import settings

urlpatterns = [
    #Paths del admin.
    #Se añade una liga url a una app
    #path('core/', include('core.urls')),
    #Para este caso, se deja vacía para que sea lo principal

    #Paths del core
    path('', include('core.urls')),
    #Paths de services
    path('services/', include('services.urls')),
    #Paths del blog
    path('blog/', include('blog.urls')),
    #Paths de las págias secundarias
    path('page/', include('pages.urls')),
    # Paths del contacto
    path('contact/', include('contact.urls')),
    #Paths del admin
    path('admin/', admin.site.urls),
]

#Solo si el debug esta activo, es decir, solo durante la fase de desarrollo
#ya que django por si solo no carga imagenes, entonces hacemos esta configuración
#al subirlo a un servidor, el servidor se encargara de procesar las imagenes
#por lo que solo si esta en modo debug se utilizara esta configuración
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Custom titles for admin

# Cambiar el titulo del admin.
admin.site.site_header = "La Caffetiera"
# Cambiar el subtitulo del admin.
admin.site.index_title = "Panel de administrador"
# Cambiar el title del admin.
admin.site.site_title = "La Caffetiera"

# Para colocar un logo es un poco más complejo y requiere cambiar los templates
# del panel de administrador
# Vamos a indicarle a django que los búsque en un directorio especifico donde vamos a poner
# los que queremos sobreescribir
# En la raíz del todo, crearemos una carpeta llamada templates
# Luego en el archivo settings, configurar la parte de TEMPLATES donde están los 'DIRS' y añadir
# la url en este caso será 'DIRS': [.os.path.join(BASE_DIR,'templates/')],

# Una vez añadida y creada la carpeta en la raíz del proyecto llamada "templates"
# Podemos ir a burcar el template original del administrador según el entorno (environment) en:
# C:\Users\zhark\Anaconda3\envs\django3\Lib\site-packages\django\contrib\admin\templates\admin
# Y elegir el archivo base_site.html para copiarlo y dentro de la carpeta que creamos de templates
# crearemos otra llamada "admin" y dentro de ella pegaremos este template.
# De manera que ahora se pueda abrir y que nosotros podamos sobreescribir el código.
# También puede añadirse el archivo base.html que esta dentro de esa carpeta también.

# Entonces personalizaremos ese archivo.

# Si queremos añadir en nuestro caso una imagen al admin, tendremos que crear una carpeta en la raíz
# llamada static donde alamacenaremos la imagenes.
# Ahora solo la cargaremos, todo esto en la raíz del directorio dentro de la carpeta templates/admin/base_site.html
# Pero nos toparemos con un problema de urls static, para solucionarlo hay que añadir a settings.py donde está la sección
# de los archivos estáticos colocar lo siguiente:
# Le añadiremos los ficheros donde tiene que ir a buscar ficheros estáticos a niel global que no forman parte de una app
# en especifico.
# STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, "static"),
# ]

# Con esto ya habrá quedado nuestro logo.

# Ahora para agregar estilos en nuestro admin en el archivo templates/admin/base_site.html, podemos hacerlo en un bloque llamado:
# {% block extrastyle %}
# {% endblock %}
# Y dentro colocar nuestros estilos css.
# Buscamos por el inspector en la página del admin para saber a que ids afectar para colocarle
# los estilos a esos bloques.(Revisar el archivo).