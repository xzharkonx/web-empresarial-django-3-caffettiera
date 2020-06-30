from .models import Link

#capitulo 45
#Con este archivo extenderemos el contexto, que quiere decir esto:
#El contexto es el diccionario que contendrá la información
#y este ya existe por default en las vistas para cada vista
#lo que hacemos es modificar ese diccionario para que asi tengamos
#estos elementos disponibles en cualquier vista como el request.path
#así podremos llamar a esas variables desde cualquier template.

#Recuerda que también tenemos que modificar el archivo de settings
#dentro de templates, options y en 'context_processors' añadir
#social.processors.ctx_dict
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    # Se crea un nuevo valor en el contexto al agregarlo así.
    for link in links:
        ctx[link.key] = link.url

    return ctx