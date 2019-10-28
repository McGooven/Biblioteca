from django.shortcuts import render,redirect
from .forms import AutorForm,GeneroForm
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from Apps.usuarios.forms import UserLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from Apps.usuarios.models import MyUser
from .models import Genero, Libro,Autor

# Create your views here.
def Home(request):   
    queryset=request.GET.get("Buscar") 
    current_user=request.user   
    top_libros=Libro.objects.filter(puntuacion__gt=4)
    if queryset:
        libros=Libro.objects.filter(Q(titulo__icontains=queryset))
        paginator=Paginator(libros,1)
        page=request.GET.get('page')
        libros=paginator.get_page('page')
        return render(request,'Biblioteca/galeria.html',{'libros':libros})
    return render(request,'index.html',{'user':current_user,'top':top_libros})

def cargarLibro(request):
    print(request.GET) 

def galeria(request):
    queryset=request.GET.get("Buscar")
    libros=Libro.objects.all() 
    if queryset:
        libros=Libro.objects.filter(Q(titulo__icontains=queryset))
    paginator=Paginator(libros,4)
    page=request.GET.get('page')
    libros=paginator.get_page(page)
    return render(request,'Biblioteca/galeria.html',{'libros':libros})

def perfil(request):    
    current_user=request.user 
    return render(request,'Accounts/perfil.html',{'user':current_user})

def libro(request): 
    return render(request,'Biblioteca/Libro.html',{})

def adminBase(request):    
    current_user=request.user   
    return render(request,'Accounts/Admin/adminBase.html',{'user':current_user})

def loginAdmin(request, *args, **kwargs):    
    form= UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request,user_obj)        
        return render(request,'Accounts/Admin/adminBase.html')
    return render(request,'Accounts/Admin/loginAdmin.html',{"form":form})


# CRUD  de autor

def crearAutor(request):
    if request.method == 'POST':
        print(request.POST)
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')       
    else:
        autor_form=AutorForm()
    return render(request,'Accounts/Admin/crear_autor.html',{'autor_form':autor_form})

def listarAutor(request):
    autores=Autor.objects.all()
    return render(request,'Accounts/Admin/listar_autor.html',{'autores':autores})

def editarAutor(request,id):
    autor_form=None
    error=None
    try:
        autor=Autor.objects.get(id = id)
        if request.method =='GET':
            autor_form=AutorForm(instance = autor)
        else:
            autor_form=AutorForm(request.POST,instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('listar_autor')
    except ObjectDoesNotExist as e:
        error=e   
    return render(request,'Accounts/Admin/editar_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutor(request,id):
    autor=Autor.objects.get(id=id)
    autor.delete()
    return redirect('listar_autor')
   

# CRUD  de Genero

def crearGenero(request):
    if request.method == 'POST':
        print(request.POST)
        genero_form = GeneroForm(request.POST)
        if genero_form.is_valid():
            genero_form.save()
            return redirect('listar_genero')       
    else:
        genero_form=GeneroForm()
    return render(request,'Accounts/Admin/crear_genero.html',{'genero_form':genero_form})

def listarGenero(request):
    genero=Genero.objects.all()
    return render(request,'Accounts/Admin/listar_genero.html',{'genero':genero})

def editarGenero(request,id):
    genero_form=None
    error=None
    try:
        genero=Genero.objects.get(id = id)
        if request.method =='GET':
            genero_form=GeneroForm(instance = genero)
        else:
            genero_form=GeneroForm(request.POST,instance=genero)
            if genero_form.is_valid():
                genero_form.save()
            return redirect('listar_genero')
    except ObjectDoesNotExist as e:
        error=e   
    return render(request,'Accounts/Admin/editar_genero.html',{'genero_form':genero_form,'error':error})

def eliminarGenero(request,id):
    genero=Genero.objects.get(id=id)
    genero.delete()
    return redirect('listar_genero')
   