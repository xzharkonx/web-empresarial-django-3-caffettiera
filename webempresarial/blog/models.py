from django.db import models
#Importamos este paquete para obtener la hora actual
#from django.utils import timezone  # timezone.now()
from django.utils.timezone import now

#Importamos este paquete para tener acceso al modelo del usuario
#Que contiene todos los usuarios en el administrador
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    #Para poder indicarle la fecha manualmente y si no la fecha actual por default
    #antes hay que importar el paquete de timezone
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    #Aquí si que le decimos que puede ser nulo o en blanco, para no
    #obligar al usuario de poner imagen en el post
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    #Esta es la clave foranéa de 1-N (uno a muchos), le pasamos el modelo
    #del cual necesita extender este modelo.

    #Si colocamos on_delete=models.CASCADE, entonces al borrar el usuario se borraran
    #todos los post de este.

    #Si colocamos on_delete=models.PROTECT, entonces protegeriamos al capo de ser borrado
    #a pesar de que se borre el autor que creo el post, pero si se hace esto hay que
    #agregarle al campo que sea nulo y que puea ir en blanco, para que se pueda permitir.

    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    #Para muchos a muchos
    #Con related_name="get_posts" cambiamos el nombre de está relación, de está forma podemos acceder a esta relación
    #cuando lo definimos, yo puedo ir a buscar la relación inversamente a ese campo
    #desde 1 categoria a todos sus post de esta categoria y se utiliza en el template
    #de category.html donde se le pregunta 1 categoria y este va por todos sus post
    #de esa categoría
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title