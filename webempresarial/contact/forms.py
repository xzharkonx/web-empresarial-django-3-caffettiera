from django import forms
#Documentación:
#https://docs.djangoproject.com/en/2.0/topics/forms/
#https://docs.djangoproject.com/en/2.0/ref/forms/fields/#built-in-field-classes

#Creamos el formulario de contacto.
class ContactForm(forms.Form):
    #El parametro label, le colocara el nombre de etiqueta al campo
    #El campo de required=True por que es requerido.
    #El campo widget nos permitira reeditar los inputs de nuestros formularios
    #podemos pasarle en el metodo las opciones que queremos editar, en este caso
    #attrs para los atributos del input y un diccionario para indicar que sera
    #la clase la modificada
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    #Se agrega un widget para decirle que será un campo de textarea.
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        #Se puede separar añadir otra propiedad, en este caso rows para que nuestro
        #textarea tenga 3 filas de tamaño por default y no se vea tan grande.
        attrs={'class':'form-control','rows':3, 'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)

    #Ahora hay que pasarselo al template desde la view.
    # Para más detalles ver el otro proyecto de webplayground, en el modelo pages,
    # en script .forms
