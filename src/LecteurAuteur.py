'''
Created on 17 mars 2014

@author: xavier
'''

from PyQt4 import QtGui, QtCore
from Poeme import Auteur
from GestionPoeme import *

class FormulaireAuteur(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(QtGui.QDialog, self).__init__()
        self.setupUi()
        self.setupAction()
        
    def setupUi(self):
        headers = ("nom","prenom")
        self.tableAuteur = QtGui.QTableWidget(0,2)
        self.tableAuteur.setHorizontalHeaderLabels(headers)
        self.tableAuteur.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableAuteur.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.tableAuteur)
        
        
        self.rechercheAuteurEdit = QtGui.QLineEdit()
        self.rechercheAuteurButton = QtGui.QPushButton("Rechercher")
        
        layoutRechercher = QtGui.QHBoxLayout()
        layoutRechercher.addWidget(self.rechercheAuteurEdit)
        layoutRechercher.addWidget(self.rechercheAuteurButton)
        
        mainLayout.addLayout(layoutRechercher)
        
        buttonBox = QtGui.QDialogButtonBox()
        self.selecButton = QtGui.QPushButton("Selectionner")
        self.quitButton = QtGui.QPushButton("Annuler")
        self.addAuteurButton = QtGui.QPushButton("Ajouter Auteur")
        buttonBox.addButton(self.quitButton, QtGui.QDialogButtonBox.RejectRole)
        buttonBox.addButton(self.addAuteurButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(self.selecButton, QtGui.QDialogButtonBox.AcceptRole)
        mainLayout.addWidget(buttonBox)
        
        self.setLayout(mainLayout)
    def setupAction(self):
        self.connect(self.addAuteurButton, QtCore.SIGNAL("clicked()"), self.ouvrirAjoutAuteur)
        self.connect(self.quitButton, QtCore.SIGNAL("clicked()"), self.quitForm)
    
    def quitForm(self):
        self.close()
    def ouvrirAjoutAuteur(self):
        print("Action")
        self.formAjout = AjoutAuteur()
        self.formAjout.show()
        
class AjoutAuteur(QtGui.QDialog):
    def __init__(self):
        super(QtGui.QDialog, self).__init__()
        self.setupUi()
        self.setupActions()
        
    def setupUi(self):
        self.nomLabel = QtGui.QLabel("Nom")
        self.nomEdit = QtGui.QLineEdit()
        self.prenomLabel = QtGui.QLabel("Prénom")
        self.prenomEdit = QtGui.QLineEdit()
        self.buttonQuit = QtGui.QPushButton("Annuler")
        self.buttonSave = QtGui.QPushButton("Sauvegarder")
        
        mainLayout = QtGui.QVBoxLayout()
        formLayout = QtGui.QFormLayout()
        formLayout.addRow(self.nomLabel, self.nomEdit)
        formLayout.addRow(self.prenomLabel, self.prenomEdit)
        buttonGroup = QtGui.QDialogButtonBox()
        buttonGroup.addButton(self.buttonQuit, QtGui.QDialogButtonBox.RejectRole)
        buttonGroup.addButton(self.buttonSave, QtGui.QDialogButtonBox.AcceptRole)
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(buttonGroup)
        
        self.setLayout(mainLayout)
        
    def setupActions(self):
        self.connect(self.buttonSave, QtCore.SIGNAL("clicked()"), self.enrAuteur)
        self.connect(self.buttonQuit, QtCore.SIGNAL("clicked()"), self.quitAuteur)
        
    def quitAuteur(self):
        self.close()
        
    def enrAuteur(self):
        if (len(self.nomEdit.text()) == 0 or len(self.prenomEdit.text()) == 0):
            QtGui.QMessageBox.about(self, "Erreur", "Veuillez remplir tous les champs du formulaire")
            return
        
        gestion = GestionPoemeBase()
        aut = Auteur(self.nomEdit.text(), self.prenomEdit.text())
        gestion.addAuthor(aut)
        QtGui.QMessageBox.about(self, "Enregistrement effectué", "Le nouvel auteur a bein été enregistré dans la base de donnée")
        self.close()
    
        