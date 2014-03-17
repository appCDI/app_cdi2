'''
Created on 8 mars 2014

@author: xavier
'''

from PyQt4 import QtGui, QtCore

from Poeme import *
from PyQt4.phonon import Phonon 
from LecteurRecherchePoeme import *
from LecteurConfig import LecteurConfig

class LecteurUser(QtGui.QMainWindow):
    '''
    classdocs
    '''
    
    def __init__(self):
        super(QtGui.QMainWindow,self).__init__()
        self.playlist = Playlist()
        self.setupUi()
        
        
        
    def setupUi(self):
        '''
        Met l'interface en place
        '''
        
        bar = QtGui.QToolBar()
        #bar.addAction(self.playAction)
        #bar.addAction(self.pauseAction)
        #bar.addAction(self.stopAction)
        
        self.seekSlider = Phonon.SeekSlider(self)
        #self.seekSlider.setMediaObject(self.playlist.getPoemeEnCours().mediaPoeme)
    
        
        self.volumeSlider = Phonon.VolumeSlider(self)
        #self.volumeSlider.setAudioOutput(self.audioOutput)
        self.volumeSlider.setMaximumSize(QtGui.QSizePolicy.Maximum, 
                                         QtGui.QSizePolicy.Maximum)
        
        volumeLabel = QtGui.QLabel()
        volumeLabel.setPixmap(QtGui.QPixmap('images/volume.png'))
        
        headers = ("Titre","Auteur", "Thème", "Siècle", "Genre", 
                   "Langue","Elève")
        self.poemeTab = QtGui.QTableWidget(0,7)
        self.poemeTab.setHorizontalHeaderLabels(headers)
        self.poemeTab.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.poemeTab.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        #self.poemeTab.cellPressed.connect(self.tableClicked)
        
        
        seekerLayout = QtGui.QHBoxLayout()
        seekerLayout.addWidget(self.seekSlider)
        
        playbackLayout = QtGui.QHBoxLayout()
        playbackLayout.addWidget(bar)
        playbackLayout.addStretch()
        playbackLayout.addWidget(volumeLabel)
        playbackLayout.addWidget(self.volumeSlider)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(LecteurRecherchePoeme())
        mainLayout.addWidget(self.poemeTab)
        mainLayout.addLayout(seekerLayout)
        mainLayout.addLayout(playbackLayout)
        
        widget = QtGui.QWidget()

        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)
        self.setWindowTitle("Printemps des poetes - Lecteur")
        
    def remplissageTableau(self):
        '''
        Pour remplir le tableau 
        '''
        
        if len(self.playlist) > 0:
            i = 0
            for i in range (len(self.playlist)):
                print(i)
        
        
    def setupAction(self):
        '''
        Définition des actions
        '''

class LecteurAdm(LecteurUser):
    def __init__(self):
        super().__init__()
        self.setupUiAdm()
        
    def ouvrirConfig(self):
        self.config = LecteurConfig()
        self.config.show()
        
        
    def setupUiAdm(self):
        '''
        Définition de l'interface admin
        '''
        buttonConfig = QtGui.QPushButton('Configuration')
        self.connect(buttonConfig, QtCore.SIGNAL("clicked()"),self.ouvrirConfig)
        self.centralWidget().layout().addWidget(buttonConfig)
        
    
        
        
        
        
    
