from django.shortcuts import render
from .models import Usuario

# Create your views here.
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'app_AE3/usuarios.html', {'usuarios': usuarios})
