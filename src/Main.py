'''
Created on 10 mars 2014
QtCore.Qt.AlignVCenter
@author: xavier
'''

from Lecteur import *
from LecteurConfig import LecteurConfig
from os import sys

if __name__ == '__main__':
    '''
    Parti qui s'occupe du lancement de toute l'application
    '''
    if (len(sys.argv))>1:
        if(sys.argv[1] == "adm"):
            print("adm mode")
            app = QtGui.QApplication(sys.argv)
            app.setApplicationName("Lecteur de poeme - Amdinistrateur mode")
            app.setQuitOnLastWindowClosed(True)
            window = LecteurAdm()
    else:
        print("usermode")
        app = QtGui.QApplication(sys.argv)
        app.setApplicationName("Lecteur de poeme - Amdinistrateur mode")
        app.setQuitOnLastWindowClosed(True)
        window = LecteurUser()
        
    
    
    
    window.show()
    
    sys.exit(app.exec_())    