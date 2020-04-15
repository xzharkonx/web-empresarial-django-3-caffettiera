from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request,"blog/blog.html",{'posts':posts})

#Se le coloca el parametro category_id para que reciba el valor en la url
#para esto ya se debio de haber configurado la url de esta app
def category(request,category_id):

    #Se hace la consulta especificamente a ese id para saber que categoría es
    #pero, nos dará error de no encuentra la página para ello, 
    #si ya sabemos que no la encontrará le diremos que nos salte un error de 404
    #si no encuentra el valor.
    #category = Category.objects.get(id=category_id)
    #por ello se importa get_object_or_404
    
    ###category = get_object_or_404(Category, id=category_id)

    #Ahora recuperar los todos los post que pertenecen a esa categoría
    #Buscaremos esos posts filtrando cuales concuerdan con ese categoría_id
    #Para ello ocuparemos filter y como el objeto (modelo) post tiene
    #su campo categories (manytomany) le pasamos el objeto de la categoría
    #que encontramos para que nos devuelva todos los post con esa categoría.
    
    ###posts = Post.objects.filter(categories=category)

    ###return render(request, "blog/category.html", {'category':category,
    ###                                                'posts':posts})

    
    #No se ocupo el código anterior, ya que haremos la consulta
    #de una manera más practica, es decir, desde un solo modelo,
    #haciendo una consulta inversa 

    category = get_object_or_404(Category, id=category_id)
    #En el template category.html cambiar la forma en que se llama al
    #objeto category de la siguiente forma category.post_set.all y
    #recorrerlo con un for
    return render(request, "blog/category.html", {'category':category})