
#################################################
# SAE 2.2 développement efficace                #
# software qt qui combine des images en .fits   #
# @author: Bastien BRUNEL & Tom LECLERCQ        #
# 16/12/2022                                    #
# V1.7 prise en compte image en couleur         #
#################################################

#import qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QCheckBox, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#import astropy
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.stats import sigma_clip
# from scipy import stats


#var globales test
test = [['C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0001.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0002.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0003.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0004.fits', 
'C:/Users/Vidox/OneDrive/Documents/Cours/2/S3/SAE/C2/fits_tests/M13_blue/M13_blue_0005.fits']]

class App(QWidget):
    def __init__(self):
        super().__init__()
        
        #label
        self.label = QLabel("Choisir une méthode de calcul")


        # attribut liste des chemins d'images
        self.liste = []
        self.setWindowTitle('SAE 2.2')
        self.figure = plt.figure()

        # jointure plt/qt
        self.canvas = FigureCanvas(self.figure)

        # création d'un petit layout rapide
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # création boutons 
        self.btnAvg = QPushButton("Moyenne")
        self.btnMed = QPushButton("Médiane")
        self.check = QCheckBox("éliminer les ouliers ?")
        

        # création connexions bouton/méthode
        self.btnMed.clicked.connect(self.btnMedClicked)
        self.btnAvg.clicked.connect(self.btnAvgClicked)

        # layout 2 le retour
        layout.addWidget(self.check)
        layout.addWidget(self.btnAvg)
        layout.addWidget(self.btnMed)

        # appel fichieres
        self.openFileNamesDialog()

        #affichage
        self.show()

    def btnAvgClicked(self):
        """
        méthode qui calcule l'image composée des pixels moyens de tous les fichiers présent dans self.liste
        """
        self.chargerAllImages(self.liste[0], option = 1) 

    def btnMedClicked(self):
        """
        méthode qui calcule l'image composée des pixels médians de tous les fichiers présent dans self.liste
        """
        self.chargerAllImages(self.liste[0], option = 2)

    def openFileNamesDialog(self):
        """
        méthode qui charge plusieurs fichiers et les ajoutes directement dans self.liste
        """
        #                        widget parent, label explication, chemin ou ouvrir la boite de dialogue, type de fichier a ouvrir
        files, _ = QFileDialog.getOpenFileNames(self,"Select one or more files to open", "","Images (*.fits / *.fit)")
        if files:
            self.liste.append(files)

                
    def chargerAllImages(self, listImage : list, option=1):
        """Cette fonction permet d'empiler les images et d'afficher le résultat
        Il y a deux types d'empilement : 
            - empilement par moyenne 
            - empilement par médiane 

        On peut aussi supprimer les valeurs aberrantes en cochant la checkbox 

        Args:
            listImage (list): liste contenant toutes les images à empiler
            option (int, optional): option permet de différencier la moyenne et la médiane. Defaults to 1.
        """
        # je toutes les données de chaque image dans la variable imageConcat
        imageConcat = [fits.getdata(image) for image in listImage]
        
        # je clear la figure 
        self.figure.clear()
        
        Image = []
        if len(imageConcat[0])==3:
            for i in range(len(imageConcat)):
                Image.append(imageConcat[i][0]+imageConcat[i][1]+imageConcat[i][2])
                cmap=None
        else:
            Image = imageConcat
            cmap='gray'
        
    
        imageSansValeurAberrante = []
    
        # Pour chaque image dans imageConcat
        for i in Image:
                imageSansValeurAberrante.append(sigma_clip(i, sigma=2.85, maxiters=1)) # je stocke récupère les données de l'image sans les valeurs aberrantes
        



        # Si l'option vaut 1
        if option == 1:
            # je fais l'empilement par moyenne
            copieImage = np.mean(Image, axis=0)
            # si la case est cochée
            if self.check.isChecked():
                # je fais l'empilement par moyenne sans les valeurs aberrantes
                copieImage = np.mean(imageSansValeurAberrante, axis=0)
                self.label.setText("Empilement par moyenne avec rejet des outliers")
            else:
                self.label.setText("Empilement par moyenne simple")

         # Si l'option vaut 1
        elif option == 2:
            # je fais l'empilement par médiane
            copieImage = np.median(Image, axis=0)
             # si la case est cochée
            if self.check.isChecked():
                 # je fais l'empilement par médiane sans les valeurs aberrantes
                copieImage =  np.median(imageSansValeurAberrante, axis=0)
                    
                self.label.setText("Empilement par médiane avec rejet des outliers")
            else:
                self.label.setText("Empilement par médiane simple")

        plt.imshow(copieImage, cmap) # j'affiche l'image
        plt.colorbar() # j'affiche la color bar sur le coté de l'image
        self.canvas.draw() # je l'ajoute au canvas

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
