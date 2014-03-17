from Poeme import *
from GestionPoeme import GestionPoemeBase



media = "media"
titre = "Je vais te violer dans ta bouche mmmmvoyez"
auteurNom = "Le riche"
auteurPrenom = "Didier"
auteur = Auteur(auteurNom, auteurPrenom)

eleveNom = "MONTIEL"
elevePrenom = "Alexandre"
eleveClasse = "BTS SIO 2"
eleve = Eleve(eleveNom, elevePrenom, eleveClasse)

chemin = "home/alexandre/poemeSample.mp3"
forme = "chanson"
siecle = "22"
langue = "patois"
themes = ["le cul"]


boum = GestionPoemeBase()

idPoeme = boum.getIdPoemeMax()
idPoeme = 7

testPoeme = Poeme(idPoeme, media, titre, auteur, siecle, eleve, forme, langue, themes)

#boum.addPoeme(testPoeme)

#boum.DeletePoeme(testPoeme, auteur)

laPlaylist = boum.RemplirPlaylist()

#boum.UpdatePoeme(testPoeme, auteur, eleve)