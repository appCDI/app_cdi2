'''
Created on 8 mars 2014

@author: alex
'''

from Poeme import *
import sqlite3 as lite

fichierDonnees = "/home/alexandre/workspace3/app_cdi2/rsc/app_cdi.db"
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
    
    def addTheme(self, theme):
        libelle = theme.libelleTheme
        requeteIdMax = "SELECT MAX(id_theme) FROM themes"
        result = cursor.execute(requeteIdMax)
        idTheme = result + 1
        requeteAjoutTheme = "INSERT INTO themes VALUES("+idTheme+", "+libelle+");"
        cursor.execute(requeteAjoutTheme)
    
    def addAuthor(self, auteur):
        nom = auteur.nomAuteur
        prenom = auteur.prenomAuteur
        requeteIdMax = "SELECT MAX(id_auteur) FROM auteur"
        result = cursor.execute(requeteIdMax)
        idAuteur = result + 1
        requete = "INSERT INTO auteur VALUES("+idAuteur+", "+nom+", "+prenom+");"
        cursor.execute(requete)
    
    def addPoeme(self, poeme):
        
        requeteID = "SELECT MAX(id_poeme) FROM poeme"
        requeteNomAuteur = "SELECT id_auteur FROM auteur WHERE nom_auteur = "+poeme.nomArtiste
        requeteSiecle = "SELECT id_siecle FROM siecles WHERE siecle = "+poeme.siecle
        requeteLangue = "SELECT id_langue FROM langues WHERE langue = "+poeme.langue
        requeteForme = "SELECT id_forme FROM forme WHERE forme = " +poeme.formePoeme
        requeteEleve = "SELECT id_eleve FROM eleve WHERE nom_eleve = " +poeme.nomEleve
        
        maxID = cursor.execute(requeteID)
        idAuteur = cursor.execute(requeteNomAuteur)
        idSiecle = cursor.execute(requeteSiecle)
        idLangue = cursor.execute(requeteLangue)
        idForme = cursor.execute(requeteForme)
        idEleve = cursor.execute(requeteEleve)
        idPoeme = maxID+1
        titrePoeme = poeme.nomPoeme
        chemin = poeme.cheminPoeme
        
        requeteAjout = "INSERT INTO poeme VALUES ("+idPoeme+", '"+titrePoeme+"', '"+chemin+"', "+idAuteur+", "+idSiecle+", "+idLangue+", "+idForme+", "+idEleve+");"
        print(requeteAjout)
        cursor.execute(requeteAjout)
        
        for theme in Poeme.listeThemes:
            requeteTheme = "SELECT * FROM themes WHERE libelle_theme = '"+theme
            result = cursor.execute(requeteTheme)
            if result != "":
                requeteAjoutTheme = "INSERT INTO rel_poeme_theme VALUES ("+idPoeme+", "+theme+");"
                cursor.execute(requeteAjoutTheme)
            else:
                idMaxTheme = "SELECT MAX(id_theme) FROM themes;"
                requeteAjoutTheme = "INSERT INTO themes VALUES("+idMaxTheme+", "+theme+");"
                cursor.execute(requeteAjoutTheme)
                requeteAjoutTheme = "INSERT INTO rel_poeme_theme VALUES ("+idPoeme+", "+theme+");"
                cursor.execute(requeteAjoutTheme)
                
    def DeletePoeme(self, poeme):
        """------------------> To be continued <--------------------"""
    def UpdatePoeme(self, poeme):
        """------------------> To be continued <--------------------"""
                
class GestionPoemeFichier:
    def __init__(self):
        '''
        Constructeur
        '''
        
        
        