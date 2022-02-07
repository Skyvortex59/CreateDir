import os
from zipfile2 import ZipFile
import re

def createDir(dirLocate, nameFolder,nbrStart, nbrFinish, stringFinish = None):
    """
    Crée une multitude fichier (avec un nombre s'incrémentant de 1) dans un endroit qu'on lui demande.
    
    params:
        dirLocate [str] : Path vers le dossier contenant nos futurs dossier
        nameFolder [str] : Nom de la base de fichier qu'on veut leur donner (ex : "[Nom d'oeuvre] - ")
        nbrFtart [int] : nombre de commencement (ex : "Nom d'oeuvre - 70"
        nbrFinish [int] : nombre de fin (ex : "Nom d'oeuvre - 90")
        stringFinish [str] : optionnel, servant si vous souhaitez ajoutez un quelconque string en fin de dossier (ex : "Nom d'oeuvre - 60 V0", ici stringFinish = 'V0')
    """
    directory = ""
    for i in range(nbrStart, nbrFinish+1):
        directory = nameFolder + str(i)
        path = os.path.join(dirLocate, directory)
        os.makedirs(path)
        finishFolder = re.findall(r'[0-9]+', path)
        extractZip(dirLocate, path, finishFolder[0])
        
def extractZip(dirLocate, dirWish, finish):
    """
    Extrait les fichiers dans un endroit précis qu'on lui indique.
    
    params:
        dirLocate [str] : Path vers le dossier contenant nos fichiers zip
        dirWish [str] : Dossier où l'on veut extraire le fichier zip
        finish [int] : paramètre servant à détecter pour que le fichier zip aille dans le bon dossier (ex : "chap 50.zip" doit aller dans le dossier chap 50)
    """
    for filename in os.listdir(dirLocate):
        if(filename.endswith(".zip")):
            with open(os.path.join(dirLocate, filename), 'r') as f:
                name = f.name[:-4]
                if(name.endswith(finish)):
                    with ZipFile(f.name, 'r') as zip:
                        zip.extractall(dirWish)
                        print('⌈{0}⌋ is unzipped in ⌈{1}⌋ folder'.format(name.partition("\\")[2], dirWish.partition("\\")[2]))
