from django.urls import path
from . import views

urlpatterns = [
    # Paths del blog
    path('', views.blog, name='blog'),
    #Creamos una url para que nuestre las categorias, 
    #a la cuál se le pasara un argumento <category_id> para saber a que
    #post pertenece, se recibirá en la view de esta app
    #de esta forma se recibira una cadena, pero se necesita
    #un número entero, por lo que se le indica int:nombre_variable
    path('category/<int:category_id>/', views.category, name="category"),
]