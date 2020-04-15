from django.shortcuts import render, get_object_or_404
#get_object_or_404: Sirve cuando consultamos un objeto con un id
#get_list_or_404: Sirve cuando consultamos una lista de objetos
from .models import Page
# Create your views here.
def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, "pages/sample.html", {'page':page})
    #En el template category.html cambiar la forma en que se llama al
    #objeto category de la siguiente forma category.post_set.all y
    #recorrerlo con un for
    