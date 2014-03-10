from Poeme import *
from GestionPoeme import GestionPoemeBase

media = ""
titre = "Titre du poeme"
auteur = "Baudelaire"
eleve = "MONTIEL"
chemin = "home/alexandre/poeme.mp3"
forme = "sonnet"
siecle = "18"
langue = "francais"
themes = ['biere', 'bédo']

testPoeme = Poeme(media, auteur, titre, siecle, eleve, forme, langue, chemin, themes)

GestionPoemeBase.addPoeme(testPoeme)

for poeme in Poeme:
    print(poeme.eleve)