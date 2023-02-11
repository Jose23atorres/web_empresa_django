from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    #Crear la plantilla
    contact_form = ContactForm()
    #Detectar si la plantilla se envia por metodo POST
    if request.method == "POST":
        #De ser asi, se llenara automaticamente nuestra plantilla
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@gmail.mailtrap.io",
                ["torres.jesus.176@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Si todo ha salido bien
                return redirect(reverse('contact')+"?ok")
            except:
                #Si algo no ha salido bien
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html",{'form':contact_form})
