'''
Created on 8 mars 2014

@author: alex
'''

import sqlite3 as lite

fichierDonnees = "../rsc/app_cdi.db"
conn = lite.connect("fichierDonnees")
cursor = conn.cursor()

class GestionPoemeBase(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def addPoeme(self):
        
        requeteID = "SELECT MAX(id_poeme) FROM poeme"
        requeteNomAuteur = "SELECT id_auteur FROM auteur WHERE nom_auteur = "+self.nomArtiste
        requeteSiecle = "SELECT id_siecle FROM siecles WHERE siecle = "+self.siecle
        requeteLangue = "SELECT id_langue FROM langues WHERE langue = "+self.langue
        requeteForme = "SELECT id_forme FROM forme WHERE forme = " +self.formePoeme
        requeteEleve = "SELECT id_eleve FROM eleve WHERE nom_eleve = " +self.nomEleve
        
        maxID = cursor.execute(requeteID)
        idAuteur = cursor.execute(requeteNomAuteur)
        idSiecle = cursor.execute(requeteSiecle)
        idLangue = cursor.execute(requeteLangue)
        idForme = cursor.execute(requeteForme)
        idEleve = cursor.execute(requeteEleve)
        idPoeme = maxID+1
        titrePoeme = self.nomPoeme
        chemin = self.cheminPoeme
        
        requeteAjout = "INSERT INTO poeme VALUES ("+idPoeme+", '"+titrePoeme+"', '"+chemin+"', "+idAuteur+", "+idSiecle+", "+idLangue+", "+idForme+", "+idEleve+");"
        print(requeteAjout)
        cursor.execute(requeteAjout)
   
class GestionPoemeFichier:
    def __init__(self):
        '''
        Constructeur
        '''
        
        
        