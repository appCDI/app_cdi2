'''
Created on 8 mars 2014

@author: alex
'''

from Poeme import *
import sqlite3 as lite

fichierDonnees = "/home/alexandre/workspace3/app_cdi2/rsc/app_cdi.db"
conn = lite.connect(fichierDonnees)
cursor = conn.cursor()

class GestionPoemeBase(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def addTheme(self, libelle):
        requeteIdMax = "SELECT MAX(id_theme) FROM themes"
        requeteExistTheme = "SELECT * FROM themes WHERE libelle_theme = '" + libelle + "';"
        cursor = conn.cursor()
        cursor.execute(requeteExistTheme)
        donnees = list(cursor)
        if(donnees == []):
            cursor.execute(requeteIdMax)
            result = list(cursor)
            
            if(result == [(None,)]):
                idTheme = 1
            else:
                for i in result:
                    idTheme = i[0] + 1
                
            requeteAjoutTheme = "INSERT INTO themes VALUES("+str(idTheme)+", '"+libelle+"');"
            cursor.execute(requeteAjoutTheme)
            conn.commit()
            cursor.close()
            
            message = 'Le thème "'+libelle+'" a bien été ajouté.'
        else:
            message = "Ce thème existe déjà."
        return message
        
    
    def addAuthor(self, auteur):
        nom = auteur.nomAuteur
        prenom = auteur.prenomAuteur
        requeteIdMax = "SELECT MAX(id_auteur) FROM auteur"
        requeteExistAuteur = "SELECT * FROM auteur WHERE nom_auteur = '"+nom+"' AND prenom_auteur = '"+prenom+"';"
        cursor = conn.cursor()
        cursor.execute(requeteExistAuteur)
        donnees = list(cursor)
        if(donnees == []):
            cursor.execute(requeteIdMax)
            result = list(cursor)
            
            if(result == [(None,)]):
                idAuteur = 1
            else:
                for i in result:
                    idAuteur = int(i[0]) + 1
   
            requete = "INSERT INTO auteur VALUES("+str(idAuteur)+", '"+nom+"', '"+prenom+"');"
                           
            cursor.execute(requete)
            conn.commit()
            cursor.close()
            
            message = "L'auteur "+nom+" "+prenom+" a bien été ajouté."
        else:
            message = "Cet auteur existe déjà."
                    
    def addEleve(self, eleve):
        nom = eleve.nomEleve
        prenom = eleve.prenomEleve
        classe = eleve.classeEleve
        requeteIdMax = "SELECT MAX(id_eleve) FROM eleve"
        requeteExistEleve = "SELECT * FROM eleve WHERE nom_eleve = '"+nom+"' AND prenom_eleve = '"+prenom+"' AND classe_eleve='"+classe+"';"
        cursor = conn.cursor()
        cursor.execute(requeteExistEleve)
        donnees = list(cursor)
        if(donnees == []):
            cursor.execute(requeteIdMax)
            result = list(cursor)
            
            if(result == [(None,)]):
                idEleve = 1
            else:
                for i in result:
                    idEleve = i[0] + 1
   
            requete = "INSERT INTO eleve VALUES("+str(idEleve)+", '"+nom+"', '"+prenom+"', '"+classe+"');"
                           
            cursor.execute(requete)
            conn.commit()
            cursor.close()
            
            message = "L'élève "+nom+" "+prenom+" en classe de "+classe+" a bien été ajouté."
        else:
            message = "Cet élève a déjà été ajouté."     
    
    def getIdPoemeMax(self):
        requete = "SELECT MAX(id_poeme) FROM poeme;"
        cursor.execute(requete)
        result = list(cursor)
        for i in result:
            idMaxPoeme = i[0] + 1
        return idMaxPoeme
         
    def addPoeme( self, poeme):
        
        nomAuteur = poeme.auteur.nomAuteur
        prenomAuteur = poeme.auteur.prenomAuteur
        
        nomEleve = poeme.eleve.nomEleve
        prenomEleve = poeme.eleve.prenomEleve
        classeEleve = poeme.eleve.classeEleve
        
        #requeteID = "SELECT MAX(id_poeme) FROM poeme"
        requeteNomAuteur = "SELECT id_auteur FROM auteur WHERE nom_auteur = '"+nomAuteur+"' AND prenom_auteur = '"+prenomAuteur+"';"
        requeteSiecle = "SELECT id_siecle FROM siecles WHERE siecle = "+poeme.siecle+";"
        requeteLangue = "SELECT id_langue FROM langues WHERE langue = '"+poeme.langue+"';"
        requeteForme = "SELECT id_forme FROM formes WHERE libelle_forme = '" +poeme.formePoeme+"';"
        requeteEleve = "SELECT id_eleve FROM eleve WHERE nom_eleve = '" +nomEleve+"' AND prenom_eleve = '"+prenomEleve+"' AND classe_eleve = '"+classeEleve+"';"
        
        cursor.execute(requeteNomAuteur)
        result = list(cursor)
        auteurPoeme = Auteur(nomAuteur, prenomAuteur)
        if(result == []):
            GestionPoemeBase.addAuthor(self, auteurPoeme)
            cursor.execute(requeteNomAuteur)
            result = list(cursor)
            for i in result:
                idAuteur = i[0]
        else:
            for i in result:
                idAuteur = i[0]
        
        cursor.execute(requeteSiecle)
        result = list(cursor)
        if(result == []):
            requeteID = "SELECT MAX(id_siecle) FROM siecles;"
            cursor.execute(requeteID)
            result = list(cursor)
            if(result == [(None,)]):
                idSiecle = 1
            else:            
                for i in result:
                    idSiecle = i[0] + 1
            requeteAjoutSiecle = "INSERT INTO siecles VALUES("+str(idSiecle)+", '"+poeme.siecle+"');"
            cursor.execute(requeteAjoutSiecle)
            conn.commit()
        else:
            for i in result:
                idSiecle = i[0]
            
        cursor.execute(requeteLangue)
        result = list(cursor)
        if(result == []):
            requeteID = "SELECT MAX(id_langue) FROM langues;"
            cursor.execute(requeteID)
            result = list(cursor)
            if(result == [(None,)]):
                idLangue = 1
            else:            
                for i in result:
                    idLangue = i[0] + 1
            requeteAjoutLangue = "INSERT INTO langues VALUES("+str(idLangue)+", '"+poeme.langue+"');"
            cursor.execute(requeteAjoutLangue)
            conn.commit()
        else:
            for i in result:
                idLangue = i[0]
                 
        cursor.execute(requeteForme)
        result = list(cursor)
        if(result == []):
            requeteID = "SELECT MAX(id_forme) FROM formes;"
            cursor.execute(requeteID)
            result = list(cursor)
            if(result == [(None,)]):
                idForme = 1
            else:            
                for i in result:
                    idForme = i[0] + 1
            requeteAjoutForme = "INSERT INTO formes VALUES("+str(idForme)+", '"+poeme.formePoeme+"');"
            cursor.execute(requeteAjoutForme)
            conn.commit()
        else:
            for i in result:
                idForme = i[0]     
        
        cursor.execute(requeteEleve)
        result = list(cursor)
        elevePoeme = Eleve(nomEleve, prenomEleve, classeEleve)
        if(result == []):
            GestionPoemeBase.addEleve(self, elevePoeme)
            cursor.execute(requeteEleve)
            result = list(cursor)
            for i in result:
                idEleve = i[0] + 1
        else:
            for i in result:
                idEleve = i[0]
               
        titrePoeme = poeme.nomPoeme
        titrePoeme = titrePoeme.capitalize()
        mediaPoeme = poeme.mediaPoeme
        
        requeteVerifPoeme = "SELECT id_poeme FROM poeme WHERE id_poeme = '"+str(poeme.idPoeme)+"' AND id_auteur = "+str(idAuteur)+";"
        cursor.execute(requeteVerifPoeme)
        result = list(cursor)
#         for i in result:
#             idPoeme = i[0]
        if(result == []):
            
#             cursor.execute(requeteID)
#             result = list(cursor)       
#             if(result == [(None,)]):
#                     idPoemeACreer = 1
#             else:
#                 for i in result:
#                     idPoemeACreer = i[0] + 1
                  
            requeteAjout = "INSERT INTO poeme VALUES ("+str(poeme.idPoeme)+", '"+titrePoeme+"', '"+mediaPoeme+"', "+str(idAuteur)+", "+str(idSiecle)+", "+str(idLangue)+", "+str(idForme)+", "+str(idEleve)+");"
            cursor.execute(requeteAjout)
            conn.commit()
        else:
            message = "Ce poème à déjà été ajouté"
        
        for theme in poeme.listeThemes:
            requeteTheme = "SELECT id_theme FROM themes WHERE libelle_theme = '"+theme+"';"
            cursor.execute(requeteTheme)
            result = list(cursor)
            if(result != []):
                for i in result:
                    idTheme = i[0]
                requeteAjoutTheme = "INSERT INTO rel_poeme_theme VALUES ("+str(poeme.idPoeme)+", "+str(idTheme)+");"
                cursor.execute(requeteAjoutTheme)
                conn.commit()
            else:
                idMaxTheme = "SELECT MAX(id_theme) FROM themes;"
                cursor.execute(idMaxTheme)
                result = list(cursor)
                for i in result:
                    idTheme = i[0] + 1
                requeteAjoutTheme = "INSERT INTO themes VALUES("+str(idTheme)+", '"+theme+"');"
                cursor.execute(requeteAjoutTheme)
                conn.commit()
                requeteAjoutThemePoeme = "INSERT INTO rel_poeme_theme VALUES ("+str(poeme.idPoeme)+", "+str(idTheme)+");"
                cursor.execute(requeteAjoutThemePoeme)
                conn.commit()
                
    def DeletePoeme(self, poeme):
        
        requetePoeme = "SELECT id_poeme FROM poeme INNER JOIN auteur ON poeme.id_auteur = auteur.id_auteur WHERE titre_poeme = '"+poeme.nomPoeme+"' AND nom_auteur = '"+poeme.auteur.nomAuteur+"';"
        cursor.execute(requetePoeme)
        result = list(cursor)
        for i in result:
            idPoemeASupprimer = i[0]
        requete = "DELETE FROM poeme WHERE id_poeme = "+str(idPoemeASupprimer)+";"
        cursor.execute(requete)
        conn.commit()
        
        requete = "DELETE FROM rel_poeme_theme WHERE id_poeme = "+str(idPoemeASupprimer)+";"
        cursor.execute(requete)
        conn.commit()
        
        message = "Le poème a bien été supprimé"
        
    def UpdatePoeme(self, poeme):
        
#         requetePoeme = "SELECT id_poeme FROM poeme INNER JOIN auteur ON poeme.id_auteur = auteur.id_auteur WHERE titre_poeme = '"+poeme.nomPoeme+"' AND nom_auteur = '"+auteur.nomAuteur+"';"
#         cursor.execute(requetePoeme)
#         result = list(cursor)
#         for i in result:
#             idPoemeAModifier = i[0]
#         
        requeteSiecle = "SELECT id_siecle FROM siecles WHERE siecle = "+poeme.siecle+";"
        cursor.execute(requeteSiecle)
        result = list(cursor)
        if(result == []):
            requeteIdSiecle = "SELECT MAX(id_siecle) FROM siecles;"
            cursor.execute(requeteIdSiecle)
            result = list(cursor)
            for i in result:
                idSiecle = i[0] + 1
            requeteAjoutSiecle = "INSERT INTO siecle VALUES ("+str(idSiecle)+", '"+poeme.siecle+"');"
            cursor.execute(requeteAjoutSiecle)
            conn.commit()
        else:
            for i in result:
                idSiecle = i[0]
                
        requeteLangue = "SELECT id_langue FROM langues WHERE langue = '"+poeme.langue+"';"
        cursor.execute(requeteLangue)
        result = list(cursor)
        if(result == []):
            requeteIdLangue = "SELECT MAX(id_langue) FROM langues;"
            cursor.execute(requeteIdLangue)
            result = list(cursor)
            for i in result:
                idLangue = i[0] + 1
            requeteAjoutLangue = "INSERT INTO langues VALUES ("+str(idLangue)+", '"+poeme.langue+"');"
            cursor.execute(requeteAjoutLangue)
            conn.commit()
        else:
            for i in result:
                idLangue = i[0]   
        
        requeteForme = "SELECT id_forme FROM formes WHERE libelle_forme = '" +poeme.formePoeme+"';"
        cursor.execute(requeteForme)
        result = list(cursor)
        if(result == []):
            requeteIdForme = "SELECT MAX(id_forme) FROM formes;"
            cursor.execute(requeteIdForme)
            result = list(cursor)
            for i in result:
                idForme = i[0] + 1
            requeteAjoutForme = "INSERT INTO formes VALUES ("+str(idForme)+", '"+poeme.forme+"');"
            cursor.execute(requeteAjoutForme)
            conn.commit()
        else:
            for i in result:
                idForme = i[0]
            
        requeteAuteur = "SELECT id_auteur FROM auteur WHERE nom_auteur = '"+poeme.auteur.nomAuteur+"' AND prenom_auteur = '"+poeme.auteur.prenomAuteur+"';"
        cursor.execute(requeteAuteur)
        result = list(cursor)
        for i in result:
            idAuteur = i[0]
            
        requeteEleve = "SELECT id_eleve FROM eleve WHERE nom_eleve = '"+poeme.eleve.nomEleve+"' AND prenom_eleve = '"+poeme.eleve.prenomEleve+"' AND classe_eleve = '"+poeme.eleve.classeEleve+"' ;"
        cursor.execute(requeteEleve)
        result = list(cursor)
        for i in result:
            idEleve = i[0]
        
        requete = "UPDATE poeme SET titre_poeme = '"+poeme.nomPoeme+"', chemin_poeme = '"+poeme.mediaPoeme+"', id_auteur = "+str(idAuteur)+", id_siecle = "+str(idSiecle)+", id_langue = "+str(idLangue)+", id_forme = "+str(idForme)+", id_eleve = "+str(idEleve)+" WHERE id_poeme = "+str(poeme.idPoeme)+";"
        cursor.execute(requete)
        conn.commit()
        
    def RemplirPlaylist(self):
        listPoemes = []
        requete = "SELECT * FROM poeme INNER JOIN auteur ON poeme.id_auteur = poeme.id_auteur INNER JOIN eleve ON eleve.id_eleve = poeme.id_eleve WHERE auteur.id_auteur = poeme.id_auteur;"
        cursor.execute(requete)
        listResult = list(cursor)
        for lignePoeme in listResult:
            requeteTheme = "SELECT themes.id_theme, themes.libelle_theme FROM themes INNER JOIN rel_poeme_theme ON rel_poeme_theme.id_theme = themes.id_theme WHERE rel_poeme_theme.id_poeme = "+str(lignePoeme[0])+";"
            cursor.execute(requeteTheme)
            listeThemePoeme = list(cursor)
            listThemes =[]
            for i in listeThemePoeme:
                theme = i[1]
                
                listThemes.append(theme)
            
            objEleve = Eleve(lignePoeme[12], lignePoeme[13], lignePoeme[14])
            objAuteur = Auteur(lignePoeme[9], lignePoeme[10])
            objPoeme = Poeme(lignePoeme[0], lignePoeme[2], lignePoeme[1], objAuteur, lignePoeme[4], objEleve ,lignePoeme[6], lignePoeme[5], listThemes)
#             requeteAuteur = "SELECT * FROM auteur INNER JOIN poeme ON poeme.id_auteur = auteur.id_auteur WHERE poeme.id_poeme = "+lignePoeme[0]+";"
#             cursor.execute(requeteAuteur)
#             resultAuteur = list(cursor)
#             for i in resultAuteur:
#                 nom = i[1]
#                 prenom = i[2]
#   
#             objAuteur = Auteur(nom, prenom)
            
            listPoemes.append(objPoeme)
            
        laPlaylist = Playlist(listPoemes, 0)
        return laPlaylist
        
class GestionPoemeFichier:
    def __init__(self):
        '''
        Constructeur
        '''
        
        
        