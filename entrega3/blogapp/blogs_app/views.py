from django.shortcuts import render, redirect
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm

def index(request):
    posts = Post.objects.all().order_by("-fecha_publicacion")
    return render(request, "index.html", {"posts": posts})

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AutorForm()
    return render(request, "autor_form.html", {"form": form})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CategoriaForm()
    return render(request, "categoria_form.html", {"form": form})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostForm()
    return render(request, "post_form.html", {"form": form})

def buscar_post(request):
    if request.method == "POST":
        form = BusquedaPostForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Post.objects.filter(titulo__icontains=query)
            return render(request, "resultados.html", {"resultados": resultados, "query": query})
    else:
        form = BusquedaPostForm()
    return render(request, "buscar.html", {"form": form})