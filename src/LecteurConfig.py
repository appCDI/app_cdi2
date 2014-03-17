'''
Created on 8 mars 2014

@author: xavier
'''

from PyQt4 import QtGui
from PyQt4 import QtCore
from LecteurRecherchePoeme import *
from LecteurAuteur import *

class LecteurConfig(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        super(QtGui.QDialog,self).__init__()
        self.setupUi()
        self.setupAction()
        
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
        self.layoutPoeme= QtGui.QHBoxLayout()
        self.layoutPoeme.addWidget(self.poemeTab)
        
        self.layoutOption = QtGui.QVBoxLayout()

        self.buttonAdd = QtGui.QPushButton("Ajouter")
        self.buttonEdit = QtGui.QPushButton("Editer")
        self.buttonRm = QtGui.QPushButton("Supprimer")


        self.layoutOption.addWidget(self.buttonAdd,QtCore.Qt.AlignCenter)
        self.layoutOption.addWidget(self.buttonEdit,QtCore.Qt.AlignCenter)
        self.layoutOption.addWidget(self.buttonRm,QtCore.Qt.AlignCenter)
        self.layoutPoeme.addLayout(self.layoutOption)
        self.layoutPoeme.setAlignment(self.layoutOption, QtCore.Qt.AlignCenter)
        
        self.buttonQuit = QtGui.QPushButton("Quitter")
        
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addWidget(LecteurRecherchePoeme())
        self.mainLayout.addLayout(self.layoutPoeme)
        self.mainLayout.addWidget(self.buttonQuit,1,QtCore.Qt.AlignRight)
    

        self.setLayout(self.mainLayout)
        self.setWindowTitle("Gestion des Poemes")
        self.setSizeIncrement(400, 500)
    def setupAction(self):
        '''
        Définition des Actions
        '''
        self.connect(self.buttonQuit, QtCore.SIGNAL('clicked()'),self.closeConfig)
        self.connect(self.buttonAdd, QtCore.SIGNAL('clicked()'),self.openFormAjout)
        self.connect(self.buttonEdit, QtCore.SIGNAL('cicked()'),self.openFormEdit)
    
    def closeConfig(self):
        self.close()
    
    def openFormEdit(self):
        self.form = FormulaireEdit()
        self.form.show()
        
    def openFormAjout(self):
        self.form = Formulaire()
        self.form.show()
        
        
        
class Formulaire(QtGui.QDialog):
    def __init__(self):
        super(QtGui.QDialog,self).__init__()
        self.setupUi()
        self.setupAction()
        
    def setupUi(self):
        '''
        Interface
        '''
        labelTitre= QtGui.QLabel("Nom du Poeme")
        editTitre = QtGui.QLineEdit()
        labelAuteur = QtGui.QLabel("Auteur")
        self.buttonAuteur = QtGui.QPushButton("Selectionner Auteur")
        
        self.buttonCancel = QtGui.QPushButton("Annuler")
        self.buttonSave = QtGui.QPushButton("Sauvergarder")
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(labelTitre)
        mainLayout.addWidget(editTitre)
        mainLayout.addWidget(labelAuteur)
        mainLayout.addWidget(self.buttonAuteur)
        #mainLayout.addRow(labelAuteur,editAuteur)
        
        
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        buttonBox.addButton(self.buttonCancel, QtGui.QDialogButtonBox.RejectRole)
        buttonBox.addButton(self.buttonSave,QtGui.QDialogButtonBox.ApplyRole)
        
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
       
       
    def setupAction(self):
        self.connect(self.buttonCancel, QtCore.SIGNAL("clicked()"), self.closeForm)
        self.connect(self.buttonAuteur, QtCore.SIGNAL("clicked()"), self.choixAuteur)
        
    def closeForm(self):
        self.close()
        
    def choixAuteur(self):
        self.selecAuteur = FormulaireAuteur()
        self.selecAuteur.show()
        
        
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
        
    
        
        
        