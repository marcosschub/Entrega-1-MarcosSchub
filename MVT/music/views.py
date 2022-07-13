from django.shortcuts import render
from music.models import Album, Artista, Cancion
from music.forms import ArtistaFormulario,AlbumFormulario,CancionFormulario

def formulario_artista(request):
    if request.method == "POST":
        mi_formulario = ArtistaFormulario(request.POST)

        print(mi_formulario) 
    
        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            artista = Artista(alias=informacion['alias'], nombre=informacion['nombre'],
                    apellido=informacion['apellido'], email=informacion['email'])

            artista.save()

            return render(request, "music/home.html")

    else:
        mi_formulario = ArtistaFormulario()
        
    return render(request, "music/artistas.html",{"mi_formulario":mi_formulario})

def formulario_album(request):
    if request.method == "POST":
        mi_formulario = AlbumFormulario(request.POST)

        print(mi_formulario) 
    
        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            album = Album(nombre=informacion['nombre'],
            fechaDePublicacion=informacion['fechaDePublicacion'], artista=informacion['artista'])

            album.save()

            return render(request, "music/home.html")

    else:
        mi_formulario = AlbumFormulario()
        
    return render(request, "music/albumes.html",{"mi_formulario":mi_formulario})

def formulario_cancion(request):
    if request.method == "POST":
        mi_formulario = CancionFormulario(request.POST)

        print(mi_formulario) 
    
        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            cancion = Cancion(nombre=informacion['nombre'], album=informacion['album'])

            cancion.save()

            return render(request, "music/home.html")

    else:
        mi_formulario = CancionFormulario()
        
    return render(request, "music/canciones.html",{"mi_formulario":mi_formulario})
    

def mostrar_home(request):
    return render(request, "music/home.html", {})