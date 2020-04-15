from django.db import models

# Create your models here.

class Link(models.Model):
    #Un campo slug nos obligara a usar caracteres alfanumericos, guiones
    #o barras y no nos permitira utilizar espacios ni carácteres especiales,
    #es perfecto para utilizarlo como clave a modo de registro como si fuera 
    #un diccionario, es decir, nosotros vamos a mapear estos enlaces dentro de la
    #memoria de la página utilizando esta clave y luego accederemos a ella 
    # como si un diccionario.
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ["name"]

    def __str__(self):
        return self.name