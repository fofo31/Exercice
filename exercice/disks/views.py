from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from disks.models import Album
from .forms import SearchForm


def home(request):
    """ Afficher tous les albums disponibles et le champ de recherche"""
    albums = Album.objects.all()

    return render(request, 'disks/accueil.html', {'tous_albums': albums})


def afficher_album(request, id):
    """ Afficher les caractéristiques de l'album"""

    album = get_object_or_404(Album, id=id)
    titres = album.track_set.all()

    return render(request, 'disks/afficher_album.html', {'album': album, 'tous_titres': titres})


def search(request):
    form = SearchForm(request.Post or None)
    if form.is_valid():
        search = form.cleaned_data('search')

    return render(request, 'disks/search.html', locals())
