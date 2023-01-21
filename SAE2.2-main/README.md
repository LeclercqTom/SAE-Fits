# SAE C2 Bastien B Tom L

Logiciel d'empilement d'image pour la SAE C2 de BUT2 APP pour **Bastien BRUNEL** & **Tom LECLERCQ**.
dernière version daté de 13/12/2022

## Installation

Nous avons codé la saé via **python 3.10.5** et nous vous conseillons de faire de même
Pour exécute le programme il faut utiliser les bibliothèques suivantes:
Installation avec [pip](https://pip.pypa.io/en/stable/)

 **1. Numpy**
Nous avons travaillé avec la **version 1.22.2**
Vous pouvez Installer Numpy avec :

```bash
pip install numpy
```

 **2. Matplotlib**
Nous avons travaillé avec la **version 3.6.2**
Vous pouvez installer MatPlotLib avec :

```bash
pip install matplotlib
```

 **3. Astropy**
Nous avons travaillé avec la **version 5.1.1**
Vous pouvez installer Astropy avec :

```bash
pip install astropy
```

**4. PyQt5**
Nous avons travaillé avec la **version 5.15.7** de PyQt5
Vous pouvez l'installer avec :

```bash
pip install pyQt5
```

## Utilisation

Pour exécuter notre programme il faut simplement exécuter le fichier ``main.py`` depuis un IDE ou via la commande :

```bash
 py main.py
```

## Résumé des fonctionnalités

- **Charger les images en .fits/.fit** **(en niveau de gris et en couleur)** dans le code grâce à une interface graphique en les sélectionnant dans l'onglet qui s'affiche. Le programme reconnaît automatiquement les images en couleur des images en niveau de gris. 
- **Empilement par moyenne** en cliquant sur le bouton correspondant en bas de la fenêtre PyQt5.
- **Empilement par médiane** en cliquant sur le bouton correspondant en bas de la fenêtre PyQt5.
Les 2 méthodes d'empilements sont compatibles avec le rejet des outliers, pour activer cette fonctionnalité il faut cocher la checkbox aux dessus des boutons du bas. 

Pour plus de détails sur l'utilisation des fonctions du code, vous pouvez vous référer à la documentation pydoc à la racine du dépôt.
