from django.shortcuts import render_to_response

# Create your views here.
##requiere un html para renderizaar la vista
def index(request):
    return render_to_response('inicio/index.html') #mandar el template a utilizar
