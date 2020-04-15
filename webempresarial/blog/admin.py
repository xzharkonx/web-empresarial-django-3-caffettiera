from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
#Digamos que cada uno de estas clases es una tabla en la base de datos
#Entonces al mostrarlos, le indicamos como lo hará
class PostAdmin(admin.ModelAdmin):
    #Para que ahora si muestre (por que antes los ocultaba)
    #esto campos pero solo en modo lectura.
    readonly_fields = ('created', 'updated')
    #Para indicarle solo las columnas que queremos mostrar
    list_display = ('title', 'author', 'published','post_categories')
    #Ordenar nuestros datos
    #Para 1 solo dato se deja la coma para 1 solo dato, por que si no,
    #no sabe el que es una Tupla
    #ordering = ('author',) 
    #Pero en nuetro caso tomamos 2 datos
    ordering = ('author', 'published')
    #Para integrar campos de búsqueda, le pasamos el dato
    #por el cuál va a buscar
    #Para el caso del campo: 'author__username', como es una 
    #clave foranéa de un modelo (objeto) le decimos 
    # por que campo (username) de ese objeto (author) que esta en la base de datos
    search_fields = ('title', 'content','author__username', 'categories__name')
    #Creará una barra de navegación para las fechas en la interfaz
    date_hierarchy = 'published'
    #Creará en la interfaz del lado derecho un recuedro con los filtros
    #de los campos que le coloquemos, tiene más sentido si es una relación
    #como la de 'author_username'
    
    #Para 1 solo dato se deja la coma para 1 solo dato, por que si no,
    #no sabe el que es una Tupla
    #list_filter = ('author__username',)
    #Por lo general se usa para filtrar relaciones de uno o varios conjuntos de 
    #objetos.
    list_filter = ('author__username', 'categories__name')

    #Ahora como no podemos mostrar la lista de categorias haciendolo como 
    #list_display = ('categories__name') entonces crearemos nuestros propios campos

    #Para ello crearemos un metodo con nombre por ejemplo post_categories:
    #le pasamos adicionalmente un obj, que hará referencia a cada elemento de 
    #de la lista de categorias (o de esa relación many to many)

    #Luego colocamos el nombre del método así:
    #list_display = ('post_categories')
    def post_categories(self, obj):
        #Accedemos a los campos manytomany con obj.categories.all()
        #el objeto es post por lo que accedemos a su campo categories
        #con categories.all() que será una lista de las categorias que
        #tendrá este objeto, las ordenamos y se iran colocando en
        #c.name que con el metodo join anexara una coma y un expacio
        #entre cada campo que encuentre.
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    #Para poder colocarle el nombre de cabecera en la tabla, en vez de que
    #salga el nombre del método
    post_categories.short_description = "Categorías"
    #Si queremos agregar más campos y que a estos les podamos inyectar
    #código html como para agregar una imagen por ejemplo, consulta la
    #siguiente liga: 
    #https://stackoverflow.com/questions/47953705/how-do-i-use-allow-tags-in-django-2-0-admin



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)