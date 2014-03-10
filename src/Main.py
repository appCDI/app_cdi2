'''
Created on 10 mars 2014

@author: xavier
'''
from PyQt4 import QtCore,QtGui
from Lecteur import *
from os import sys

if __name__ == '__main__':
    '''
    Parti qui s'occupe du lancement de toute l'application
    '''
    
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Lecteur de poeme")
    app.setQuitOnLastWindowClosed(True)
    
    window = LecteurUser()
    window.show()
    
    sys.exit(app.exec_())    