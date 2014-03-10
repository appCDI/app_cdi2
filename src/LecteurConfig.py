'''
Created on 8 mars 2014

@author: xavier
'''

from PyQt4 import QtGui
from PyQt4 import QtCore
from LecteurRecherchePoeme import *


class LecteurConfig(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        super(QtGui.QDialog,self).__init__()
        self.setupUi()
        
    def setupUi(self):
        '''
        Définition de l'interface
        '''
        #Tableau de poeme
        headers = ("Id","Titre","Auteur", "Thème", "Siècle", "Genre", 
                   "Langue","Elève")
        self.poemeTab = QtGui.QTableWidget(0,8)
        self.poemeTab.setHorizontalHeaderLabels(headers)
        self.poemeTab.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.poemeTab.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        layoutPoeme= QtGui.QHBoxLayout()
        layoutPoeme.addWidget(self.poemeTab)
        
        layoutOption = QtGui.QVBoxLayout()

        buttonAdd = QtGui.QPushButton("Ajouter")
        buttonEdit = QtGui.QPushButton("Editer")
        buttonRm = QtGui.QPushButton("Supprimer")


        layoutOption.addWidget(buttonAdd,QtCore.Qt.AlignCenter)
        layoutOption.addWidget(buttonEdit,QtCore.Qt.AlignCenter)
        layoutOption.addWidget(buttonRm,QtCore.Qt.AlignCenter)
        layoutPoeme.addLayout(layoutOption)
        layoutPoeme.setAlignment(layoutOption, QtCore.Qt.AlignCenter)
        
        buttonQuit = QtGui.QPushButton("Quitter")
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(LecteurRecherchePoeme())
        mainLayout.addLayout(layoutPoeme)
        mainLayout.addWidget(buttonQuit,1,QtCore.Qt.AlignRight)
    

        self.setLayout(mainLayout)
        self.setWindowTitle("Gestion des Poemes")
    
    def setupAction(self):
        '''
        Définition des Actions
        '''
        

class Formulaire(QtGui.QDialog):
    def __init__(self):
        super(QtGui.QDialog,self).__init__()
        
    def setupUi(self):
        '''
        Interface
        '''
        
class FormlaireAjout(Formulaire):
    def __init__(self):
        super().__init__()
        
    def setupUiAjout(self):
        '''
        Interface
        '''
    
    def setupActionAjout(self):
        '''
        Actions
        '''

class FormulaireEdit(Formulaire):
    def __init__(self):
        super().__init__()
        
    def setupUiEdit(self):
        ''' 
        Interface
        '''
        
    def setupActionEdit(self):
        '''
        Actions
        '''
        
    
        
        
        