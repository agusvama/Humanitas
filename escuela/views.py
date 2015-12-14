from django.shortcuts import render_to_response

# Create your views here.
#requiere el html para renderizar una vista
def index(request):
    return render_to_response('templates/escuela/index.html')
