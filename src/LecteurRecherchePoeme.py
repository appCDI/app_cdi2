'''
Created on 8 mars 2014

@author: xavier
'''
from PyQt4 import QtGui

class LecteurRecherchePoeme(QtGui.QWidget):

    def __init__(self):
        super(QtGui.QWidget,self).__init__()
        
        self.setupUi()
        self.playlistRecherche = []
        
    def setupUi(self):
        searchLine = QtGui.QLineEdit()
        searchLine.setText("Rechercher")
        searchButton = QtGui.QPushButton("Go")
        
        searchList = ("Titre","Auteur", "Thème", "Siècle", "Genre", 
                   "Langue","Elève")
        searchBox = QtGui.QComboBox()
        searchBox.addItems(searchList)
        
        searchLayout = QtGui.QHBoxLayout()
        searchLayout.addWidget(searchLine)
        searchLayout.addWidget(searchBox)
        searchLayout.addWidget(searchButton)
        
        self.setLayout(searchLayout)
    
    def setupAction(self):
        ''' 
        Définition des Actions
        '''
        
    def recherche(self):
        '''
        Action de recherche
        '''
        
    
        