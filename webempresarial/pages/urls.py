from django.urls import path
from . import views

urlpatterns = [
    # Paths de las páginas secundarias.

    #Creamos una url para que nuestre las páginas secundarias (Page), 
    #a la cuál se le pasara un argumento <page_id> para saber a que
    #post pertenece, se recibirá en la view de esta app
    #de esta forma se recibira una cadena, pero se necesita
    #un número entero, por lo que se le indica int:nombre_variable
    path('<int:page_id>/<slug:page_slug>', views.page, name="page"),
]