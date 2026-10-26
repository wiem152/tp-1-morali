from PyQt5.uic import *
from PyQt5.QtWidgets import *
from numpy import array
t = array([str] * 100)


def ajouter():

    nom = w.ln.text()
    if not (alpha(nom) and len(nom) >= 3):
        QMessageBox.critical(w, 'erreur', 'verifiez le nom d eleve ')
    else:
        f = open('nom.txt', 'a')
        f.write(nom + '\n')
        QMessageBox.information(w, 'succee', 'l ajout est reussite ')
        f.close()
    w.ln.clear()


def alpha(x):
    i = 0
    verif = True
    while i < len(x) and verif:
        if "A" <= x[i].upper() <= "Z":
            i = i + 1
        else:
            verif = False
    return verif


def afficher():
    w.list.clear()
    w.ln.clear()
    if not (w.r1.isChecked() or w.r2.isChecked()):
        QMessageBox.critical(w, 'erreur', 'il faut cliquer un de 2 boutons ')
    else:
        if w.r1.isChecked():
            w.list.clear()
            f = open('nom.txt', 'r')
            ch = f.read()
            w.list.addItem(ch)
            f.close()

        else:
            fc = open('croissant.txt', 'r')
            ch = fc.read()
            w.list.addItem(ch)
            fc.close()


def trier():

    if w.r2.isChecked():
        f = open('nom.txt', 'r')
        ch = f.readline()
        n = 0
        while ch != '':
            ch = ch[:-1]
            t[n] = ch

            n = n + 1
            ch = f.readline()
        f.close()

        for i in range(1, n):
            aux = t[i]
            j = i
            while j > 0 and len(t[j - 1]) > len(aux):
                t[j] = t[j - 1]
                j = j - 1
            t[j] = aux
        fc = open('croissant.txt', 'w')
        for i in range(n):
            fc.write(t[i] + '\n')


app = QApplication([])
w = loadUi("C:/Users/ghars/Desktop/ex classe/morali.ui")
w.show()
w.aj.clicked.connect(ajouter)
w.aff.clicked.connect(afficher)
w.tri.clicked.connect(trier)

app.exec_()
