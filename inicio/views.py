from django.shortcuts import render_to_response

# Create your views here.
##requiere un html para renderizaar la vista
def index(request):
    return render_to_response('inicio/index.html') #mandar el template a utilizar

def oferta(request):
    return render_to_response('inicio/oferta.html')

def galeria(request):
    return render_to_response('inicio/galeria.html')

def contacto(request):
    return render_to_response('inicio/contacto.html')
