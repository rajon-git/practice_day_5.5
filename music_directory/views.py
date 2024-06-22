from django.shortcuts import render,redirect 
from album.models import Album
from album.forms import AlbumForm

def home(request):
    data = Album.objects.all()
    return render(request , "home.html", {'data':data})

def edit_album(request,id):
    album = Album.objects.get(pk=id)
    album_forms = AlbumForm(instance=album)
    if request.method == 'POST':
        album_forms = AlbumForm(request.POST, instance= album)
        if album_forms.is_valid():
            album_forms.save()
            return redirect('homepage')
    return render(request, 'add_album.html' , {'form':album_forms})

def delete_album(request,id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')