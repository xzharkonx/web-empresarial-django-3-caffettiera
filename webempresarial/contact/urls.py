from django.urls import path
from . import views

urlpatterns = [
    # Paths del contacto
    path('', views.contact, name='contact'),

    # Obrserva que no hay ninguna otra url, por lo que 
    # al retornar esta url le pasamos un parametro,
    # con ese parametro indicamos que es una nueva url
    # pero no está registrada aquí, y reverse permite
    # que la url funcione sin necesidad de que este aquí.
    # Además de que estamos pasandole parametros variados.
    # Observa la view de esta app.
    # return redirect(reverse('contact')+"?ok")
]