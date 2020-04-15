from django.contrib import admin

from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Para detectar si el usuario forma parte del grupo "Personal"
    #Y añadir o quitar, según que campos a readonlyfields
    #Para extender esta función en tiempo de ejecución
    #Son parametros que se le deben de pasar
    #Más información en: https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-methods
    def get_readonly_fields(self, request, obj=None):
        #request nos permite comprobar en tiempo de ejecución,
        #si hay algún usuario identificado y si ese usuario
        #forma parde del grupo personal.
        #Esto comprobara si dentro del grupo persona, existe el usuario
        if request.user.groups.filter(name="Personal").exists():
            #Si existe, vamos a devolver el valor que va a sobreescribir
            #a readonly_fields
            #No mostramos 'created','updated', para los usuarios que esten 
            #en el grupo Personal
            return ('key','name')
        else:
            #Si no, supondrá que es otro usuario y solo harémos de created
            #y updated
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)