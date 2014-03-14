'''
Created on 8 mars 2014

@author: xavier
'''
from PyQt4.phonon import Phonon

class Poeme:

    def __init__(self, media, nomPoeme, siecle, formePoeme, langue, listeThemes):
        self.mediaPoeme = media
        self.nomPoeme = nomPoeme
        self.siecle = siecle
        self.formePoeme = formePoeme
        self.langue = langue
        self.listeThemes = listeThemes
    
class Auteur:
    def __init__(self, nom, prenom):
        self.nomAuteur = nom
        self.prenomAuteur = prenom
        
class Eleve:
    def __init__(self, nom, prenom, classe):
        self.nomEleve = nom
        self.prenomEleve = prenom
        self.classeEleve = classe
     
class Playlist:
    def __init__(self):
        self.listePoeme = []
        self.lectureEnCours = 0
        
        
    def ajoutPoeme(self, poeme):
        self.listePoeme.append(poeme)
        
    def supprimerPoeme(self,poeme):
        self.listePoeme.remove(poeme)
        
    def suivantPoeme(self):
        if len(self.listePoeme) + 1 < len(self.listePoeme):
            self.lectureEnCours+=1
        
        
    def precendPoeme(self):
        self.lectureEnCours-=1
        
    def getPoemeEnCours(self):
        if len(self.listePoeme):
            return self.listePoeme[self.lectureEnCours]
        else:
            return None
    
    
        
        
        