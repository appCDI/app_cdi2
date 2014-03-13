from Poeme import *
from GestionPoeme import GestionPoemeBase

media = ""
titre = "Titre du poeme"
auteurNom = "Baudelaire"
auteurPrenom = "Charles"
auteur = Auteur(auteurNom, auteurPrenom)

eleve = "MONTIEL"
chemin = "home/alexandre/poemeSample.mp3"
forme = "sonnet"
siecle = "18"
langue = "francais"
themes = ['biere', 'bédo']

GestionPoemeBase.addAuthor(auteur)

for theme in themes:
    GestionPoemeBase.addTheme(theme)

testPoeme = Poeme(media, auteur, titre, siecle, eleve, forme, langue, chemin, themes)

GestionPoemeBase.addPoeme(testPoeme)

for poeme in Poeme:
    print(poeme.eleve)
    