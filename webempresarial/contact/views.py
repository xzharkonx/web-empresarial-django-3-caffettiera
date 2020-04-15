#Importamos redirect para redireccionar la view
from django.shortcuts import render, redirect
#Importamos reverse para que la url sea dinámica
from django.urls import reverse
#Importamos una librería para el correo,
#sirve para crear la estructura del mensaje y poder enviarlo.
from django.core.mail import EmailMessage

#Importamos el formulario de contacto
from .forms import ContactForm
# Create your views here.
def contact(request):
    #Para comprobar que tipo de petición nos envía.
    #print("Tipo de petición: {}".format(request.method))
    #Instanciamos el formulario y se lo enviamos al template por
    #medio del contexto.
    contact_form = ContactForm()

    if request.method == "POST":
        #Si la petición es de tipo post, entonces los datos
        #los cargara en request.POST (un diccionario que
        #tendrá todos los datos del formulario enviado)
        contact_form = ContactForm(data=request.POST)
        #entonces lo que se hará rellenado es la plantilla.

        #Ahora vamos a validad con el metodo is_valid() para
        #saber si los campos están rellenados correctamente
        #Devolvera true o false encaso de que esten bien o no.
        if contact_form.is_valid():
            #Que podemos hacer si estamos seguros de que todos
            #los campos son correctos, pues podemos recuperarlos.
            #y si no hay ninguno que nos devuelva una cadena vacía.
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #ahora se procedera a crear una estructura para el email.
            #En este punto tenemos toda la información recuperada

            #Suponemos que todo ha ido bien entonces para indicarselo
            #al usuario lo redireccionaremos pasandole un parametro

            #Enviamos el correo y redireccionamos.
            email = EmailMessage(
                "La caffettiera: Nuevo mensaje de contacto", #asunto,
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),#cuerpo,
                #Se pone un correo que esta enviando automaticamente, puede ser
                #cambiado por el de la empresa.
                "no-contestar@inbox.mailtrap.io",#email_origen,
                #Se enviará a una lista de correos, en esta caso solo al mio.
                ['xzharkonx@gmail.com'],#email_destino,
                #Sirve para responderle aútomaticamente
                reply_to=[email]

            )

            try:
                #importamos redirect para la redirección.
                #return redirect('/contact/?ok')
                #El problema es que le estaremos pasando una url estática,
                #para que sea dinamica importan tambien reverse
                #De esta forma si cambiaramos la url, el namespace quedaria
                #igual y no habria problema, solo que ahora le sumamos
                #una cadena con el parametro y el signo ?

                #Lo redirecciona a contact (a el mismo) pero con un parametro
                #y este se comprueba en el template

                email.send()
                return redirect(reverse('contact')+"?ok")

            except:
                #Algo no ha ido bien, redireccionamos a Fail
                return redirect(reverse('contact')+"?fail")


            
            return redirect(reverse('contact')+"?ok")


    return render(request,"contact/contact.html",{'form':contact_form})