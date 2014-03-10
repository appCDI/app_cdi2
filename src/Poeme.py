'''
Created on 8 mars 2014

@author: xavier
'''
from PyQt4.phonon import Phonon

class Poeme:

    def __init__(self, media, nom, nomPoeme, genrePoeme, langue):
        self.mediaPoeme = media
        self.nomArtiste = nom
        self.nomPoeme = nomPoeme
        self.genrePoeme = genrePoeme
        self.langue = langue
    
                
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
    
    
        
        
        