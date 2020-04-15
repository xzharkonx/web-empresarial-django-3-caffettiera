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
