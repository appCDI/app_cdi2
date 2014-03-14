from Poeme import *
from GestionPoeme import GestionPoemeBase

media = "media"
titre = "Y en a marre des riches"
auteurNom = "Le riche"
auteurPrenom = "Didier"
auteur = Auteur(auteurNom, auteurPrenom)

eleveNom = "Merde"
elevePrenom = "Jetan"
eleveClasse = "chose"
eleve = Eleve(eleveNom, elevePrenom, eleveClasse)

chemin = "home/alexandre/poemeSample.mp3"
forme = "truc drole"
siecle = "22"
langue = "patois"
themes = ["les riches", "l argent", "les putes"]

testPoeme = Poeme(media, titre, siecle, forme, langue, themes)
boum = GestionPoemeBase()
#boum.addPoeme(testPoeme, auteur, eleve)

#boum.DeletePoeme(testPoeme, auteur)

boum.UpdatePoeme(testPoeme, auteur, eleve)