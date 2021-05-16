from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home,name='accueil'),
    path('album/<int:id>',views.afficher_album, name='afficher_album'),
    path('search/',views.search, name ='recherche')
]


