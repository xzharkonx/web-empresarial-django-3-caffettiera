#Registrarlo dentro de la librería de templates para ello
#importamos a template
from django import template

#Importamos desde pages, recuerda que este archivo
#está dentro de una carpeta.
from pages.models import Page


#Vamos a hacer referencia a la librería de templates
register = template.Library()

#Creamos una función para conseguir la lista de páginas
#Con este decorador convertimos está función en un tag simple
#y lo registramos en la librería de templates
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages

#Es importante reiniciar el servidor.
#Dentro del template en este caso base.html los llamamos así:
#{% load pages_extras %}#Para que haga el queryset y cargue este método
#{% get_page_list %}    #