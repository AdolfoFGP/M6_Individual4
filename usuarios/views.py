from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages

# Create your views here.

def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            username = formulario_p.cleaned_data["username"]
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
            formulario_p.save()
            return redirect('app_AE2:landing') 
           
        else:
            messages.error(request, 'Hubo un error en el registro')
    formulario = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {'formulario':formulario})
