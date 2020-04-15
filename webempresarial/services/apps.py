from django.apps import AppConfig


class ServicesConfig(AppConfig):
    name = 'services'
    #Recuerda que debes editar en settings el nombre de la app
    #de la siguiente forma:
    #'services.apps.ServicesConfig',
    verbose_name = 'Servicios'
