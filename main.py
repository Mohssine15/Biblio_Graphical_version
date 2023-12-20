import sqlite3
import sys
from PyQt6.QtCore import Qt, QCoreApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox, \
    QGridLayout, QTableWidget, QTableWidgetItem

#Création des tables de la base de données
class BdTables:
    def __init__(self):
        self.con = sqlite3.connect("mydb.db")
        self.cur = self.con.cursor()
        req1 = "CREATE TABLE IF NOT EXISTS adherent(adhID INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, adhNum INTEGER )"
        self.cur.execute(req1)
        self.con.commit()

        req2 = "CREATE TABLE IF NOT EXISTS livre (livreID INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT, auteur TEXT, nbrPages INTERGER, ISBN INTEGER)"
        self.cur.execute(req2)
        self.con.commit()

        req3 = "CREATE TABLE IF NOT EXISTS emprunt (empruntID INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT, nomAdh TEXT, ISBN INTERGER, date TEXT)"
        self.cur.execute(req3)
        self.con.commit()
        self.cur.close()
        self.con.close()
#Création de classe de la fenetre ==Afficher liste des Adhérents == comme widget
class FenAfficherAdh(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = QWidget(self)
        self.widget.resize(500,300)
        self.setWindowTitle("Liste des adhérents")
        #création de Grid layout
        self.layout = QGridLayout(self)
        self.widget.setLayout(self.layout)
        #création de labels
        self.label1 = QLabel("Liste des adhérents",self.widget)
        self.layout.addWidget(self.label1, 0, 0)
        #création de table
        self.table = QTableWidget(self.widget)
        self.layout.addWidget(self.table, 1, 0)
        self.table.setColumnCount(4)
        # self.table.setRowCount(3)
        self.table.setHorizontalHeaderLabels(["AdhID", "Nom", "Prénom", "Numéro Adh"])
        #Création de bouton --afficher la liste des adhérents---
        self.btnAfficherAdh = QPushButton("  Afficher la liste des adhérents",self.widget)
        self.layout.addWidget(self.btnAfficherAdh, 2, 0,)
        self.btnAfficherAdh.setIcon(QIcon('liste.jpg'))
        self.btnAfficherAdh.clicked.connect(self.btnAfficherAdhClicked)

    def btnAfficherAdhClicked(self):
        self.con = sqlite3.connect("mydb.db")
        self.cur = self.con.cursor()
        req = "SELECT * FROM adherent"
        self.cur.execute(req)
        self.con.commit()
        self.resultat = self.cur.fetchall()
        print(self.resultat)
        print(len(self.resultat))
        self.table.setRowCount(len(self.resultat))
        # self.table.setItem(0, 0, QTableWidgetItem('1'))
        i = 0
        for x in self.resultat:
            # print(x)
            # # print(i)
            j = 0
            for y in x:
                # print("i = ", i, "j = ", j)
                # print(y)
                self.table.setItem(i, j, QTableWidgetItem(str(y)))
                j = j + 1
            i = i + 1
class FenAfficherLiv(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = QWidget(self)
        self.widget.resize(500,300)
        self.setWindowTitle("Liste des livres")
        #création de Grid layout
        self.layout = QGridLayout(self)
        self.widget.setLayout(self.layout)
        #création de labels
        self.label1 = QLabel("Liste des livres",self.widget)
        self.layout.addWidget(self.label1, 0, 0)
        #création de table
        self.table = QTableWidget(self.widget)
        self.layout.addWidget(self.table, 1, 0)
        self.table.setColumnCount(4)
        # self.table.setRowCount(3)
        self.table.setHorizontalHeaderLabels(["LivreID", "Titre", "Auteur", "Nbr de pages", "ISBN"])
        #Création de bouton --afficher la liste des adhérents---
        self.btnAfficherLiv = QPushButton("  Afficher la liste des livres",self.widget)
        self.layout.addWidget(self.btnAfficherLiv, 2, 0,)
        self.btnAfficherLiv.setIcon(QIcon('liste.jpg'))
        self.btnAfficherLiv.clicked.connect(self.btnAfficherLivClicked)

    def btnAfficherLivClicked(self):
        self.con = sqlite3.connect("mydb.db")
        self.cur = self.con.cursor()
        req = "SELECT * FROM livre"
        self.cur.execute(req)
        self.con.commit()
        self.resultat = self.cur.fetchall()
        print(self.resultat)
        print(len(self.resultat))
        self.table.setRowCount(len(self.resultat))
        # self.table.setItem(0, 0, QTableWidgetItem('1'))
        i = 0
        for x in self.resultat:
            # print(x)
            # # print(i)
            j = 0
            for y in x:
                # print("i = ", i, "j = ", j)
                # print(y)
                self.table.setItem(i, j, QTableWidgetItem(str(y)))
                j = j + 1
            i = i + 1
class FenAfficherEmp(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = QWidget(self)
        self.widget.resize(500,300)
        self.setWindowTitle("Liste des emprunts")
        #création de Grid layout
        self.layout = QGridLayout(self)
        self.widget.setLayout(self.layout)
        #création de labels
        self.label1 = QLabel("Liste des emprunts",self.widget)
        self.layout.addWidget(self.label1, 0, 0)
        #création de table
        self.table = QTableWidget(self.widget)
        self.layout.addWidget(self.table, 1, 0)
        self.table.setColumnCount(4)
        # self.table.setRowCount(3)
        self.table.setHorizontalHeaderLabels(["EmpruntID", "Titre", "Nom Adhérent", "ISBN", "Date"])
        #Création de bouton --afficher la liste des adhérents---
        self.btnAfficherEmp = QPushButton("  Afficher la liste des emprunts",self.widget)
        self.layout.addWidget(self.btnAfficherEmp, 2, 0,)
        self.btnAfficherEmp.setIcon(QIcon('liste.jpg'))
        self.btnAfficherEmp.clicked.connect(self.btnAfficherEmpClicked)

    def btnAfficherEmpClicked(self):
        self.con = sqlite3.connect("mydb.db")
        self.cur = self.con.cursor()
        req = "SELECT * FROM emprunt"
        self.cur.execute(req)
        self.con.commit()
        self.resultat = self.cur.fetchall()
        print(self.resultat)
        print(len(self.resultat))
        self.table.setRowCount(len(self.resultat))
        # self.table.setItem(0, 0, QTableWidgetItem('1'))
        i = 0
        for x in self.resultat:
            # print(x)
            # # print(i)
            j = 0
            for y in x:
                # print("i = ", i, "j = ", j)
                # print(y)
                self.table.setItem(i, j, QTableWidgetItem(str(y)))
                j = j + 1
            i = i + 1

#Création de classe de la fenetre ==Ajout Adhérent == comme widget
class FenAjouterAdh(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = QWidget(self)
        self.widget.setGeometry(50, 20, 450, 150)
        # self.widget.resize(450,150)
        self.setWindowTitle("Ajout d'adhérent")
        #création de Grid layout
        self.layout = QGridLayout(self)
        self.widget.setLayout(self.layout)
        #création de labels
        self.label1 = QLabel("Ajouter un adhérent",self.widget)
        self.layout.addWidget(self.label1, 0, 0)
        self.label2 = QLabel("Nom",self.widget)
        self.layout.addWidget(self.label2, 1, 0)
        self.label3 = QLabel("Prénom",self.widget)
        self.layout.addWidget(self.label3, 1, 1)
        self.label4 = QLabel("Numéro Adh",self.widget)
        self.layout.addWidget(self.label4, 1, 2)
        #création de zone de text
        self.lineEditNom = QLineEdit(self)
        self.layout.addWidget(self.lineEditNom, 2, 0)
        self.lineEditPrenom = QLineEdit(self)
        self.layout.addWidget(self.lineEditPrenom, 2, 1)
        self.lineEditNumAdh = QLineEdit(self)
        self.layout.addWidget(self.lineEditNumAdh, 2, 2)
        #Création de bouton d'ajout adhérent
        self.btnAjouterAdh = QPushButton("Ajouter",self.widget)
        self.layout.addWidget(self.btnAjouterAdh, 3, 0, 3, 0)
        self.btnAjouterAdh.setIcon(QIcon('addadh.png'))
        self.btnAjouterAdh.clicked.connect(self.btnAjouterAdhClicked)

    def btnAjouterAdhClicked(self):
        self.con = sqlite3.connect("mydb.db")
        self.cur = self.con.cursor()
        req = "INSERT INTO adherent VALUES(NULL, '"+self.lineEditNom.text()+"', '"+self.lineEditPrenom.text()+"', '"+self.lineEditNumAdh.text()+"')"
        self.cur.execute(req)
        self.con.commit()
        QMessageBox.information(self,"Info","L'adhérent '"+self.lineEditNom.text() + "' '" +self.lineEditPrenom.text()+ "' est ajouté avec succés")
        self.lineEditNom.clear()
        self.lineEditPrenom.clear()
        self.lineEditNumAdh.clear()
class FenAjouterLiv(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = QWidget(self)
        self.widget.setGeometry(50, 20, 450, 150)
        # self.widget.resize(450,150)
        self.setWindowTitle("Ajout de livre")
        #création de Grid layout
        self.layout = QGridLayout(self)
        self.widget.setLayout(self.layout)
        #création de labels
        self.label1 = QLabel("Ajouter un livre",self.widget)
        self.layout.addWidget(self.label1, 0, 0)
        self.label2 = QLabel("Titre",self.widget)
        self.layout.addWidget(self.label2, 1, 0)
        self.label3 = QLabel("Auteur",self.widget)
        self.layout.addWidget(self.label3, 1, 1)
        self.label4 = QLabel("Nbr de Pages",self.widget)
        self.layout.addWidget(self.label4, 1, 2)
        self.label5 = QLabel("ISBN",self.widget)
        self.layout.addWidget(self.label5, 1, 3)
        #création de zone de text
        self.lineEditTitre = QLineEdit(self)
        self.layout.addWidget(self.lineEditTitre, 2, 0)
        self.lineEditAuteur = QLineEdit(self)
        self.layout.addWidget(self.lineEditAuteur, 2, 1)
        self.lineEditNbrPages = QLineEdit(self)
        self.layout.addWidget(self.lineEditNbrPages, 2, 2)
        self.lineEditISBN = QLineEdit(self)
        self.layout.addWidget(self.lineEditISBN, 2, 3)
        #Création de bouton d'ajout adhérent
        self.btnAjouterLiv = QPushButton("Ajouter",self.widget)
        self.layout.addWidget(self.btnAjouterLiv, 3, 0, 4, 0)
        self.btnAjouterLiv.setIcon(QIcon('addadh.png'))
        self.btnAjouterLiv.clicked.connect(self.btnAjouterLivClicked)
    def btnAjouterLivClicked(self):
        self.con = sqlite3.connect("mydb.db")
        self.cur = self.con.cursor()
        req = "INSERT INTO livre VALUES(NULL, '"+self.lineEditTitre.text()+"', '"+self.lineEditAuteur.text()+"', '"+self.lineEditNbrPages.text()+"','"+self.lineEditISBN.text()+"')"
        self.cur.execute(req)
        self.con.commit()
        QMessageBox.information(self,"Info","Le livre '"+self.lineEditTitre.text() + "' est ajouté avec succés")
        self.lineEditTitre.clear()
        self.lineEditAuteur.clear()
        self.lineEditNbrPages.clear()
        self.lineEditISBN.clear()
class FenAjouterEmp(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = QWidget(self)
        self.widget.setGeometry(50, 20, 450, 150)
        # self.widget.resize(450,150)
        self.setWindowTitle("Ajout d'emprunt")
        #création de Grid layout
        self.layout = QGridLayout(self)
        self.widget.setLayout(self.layout)
        #création de labels
        self.label1 = QLabel("Ajouter un emprunt",self.widget)
        self.layout.addWidget(self.label1, 0, 0)
        self.label2 = QLabel("Titre",self.widget)
        self.layout.addWidget(self.label2, 1, 0)
        self.label3 = QLabel("Nom Adh",self.widget)
        self.layout.addWidget(self.label3, 1, 1)
        self.label4 = QLabel("ISBN",self.widget)
        self.layout.addWidget(self.label4, 1, 2)
        self.label5 = QLabel("Date",self.widget)
        self.layout.addWidget(self.label5, 1, 3)
        #création de zone de text
        self.lineEditTitre = QLineEdit(self)
        self.layout.addWidget(self.lineEditTitre, 2, 0)
        self.lineEditNomAdh = QLineEdit(self)
        self.layout.addWidget(self.lineEditNomAdh, 2, 1)
        self.lineEditISBN = QLineEdit(self)
        self.layout.addWidget(self.lineEditISBN, 2, 2)
        self.lineEditDate = QLineEdit(self)
        self.layout.addWidget(self.lineEditDate, 2, 3)
        #Création de bouton d'ajout adhérent
        self.btnAjouterEmp = QPushButton("Ajouter",self.widget)
        self.layout.addWidget(self.btnAjouterEmp, 3, 0, 4, 0)
        self.btnAjouterEmp.setIcon(QIcon('livre.png'))
        self.btnAjouterEmp.clicked.connect(self.btnAjouterEmpClicked)
    def btnAjouterEmpClicked(self):
        self.con = sqlite3.connect("mydb.db")
        self.cur = self.con.cursor()
        req = "INSERT INTO emprunt VALUES(NULL, '"+self.lineEditTitre.text()+"', '"+self.lineEditNomAdh.text()+"', '"+self.lineEditISBN.text()+"','"+self.lineEditDate.text()+"')"
        self.cur.execute(req)
        self.con.commit()
        QMessageBox.information(self,"Info","L'emprunt '"+self.lineEditTitre.text() + "' est ajouté avec succés")
        self.lineEditTitre.clear()
        self.lineEditNomAdh.clear()
        self.lineEditISBN.clear()
        self.lineEditDate.clear()
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #Création de la fenêtre principale
        self.resize(650,200)
        self.setWindowTitle("Gestion de Bibliothéque")
        #Création de widget central
        self.widget1 = QWidget(self)
        self.setCentralWidget(self.widget1)
        #Création de grid layout
        self.layout = QGridLayout(self)
        #affectation de widget1 to layout
        self.widget1.setLayout(self.layout)

        #Création de labels
        #Création de label Adhérent
        self.label1 = QLabel("Adhérent",self.widget1)
        self.layout.addWidget(self.label1, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        #Création de label Livre
        self.label1 = QLabel("Livre",self.widget1)
        self.layout.addWidget(self.label1, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        #Création de label Emprunt
        self.label1 = QLabel("Emprunt",self.widget1)
        self.layout.addWidget(self.label1, 0, 2, alignment=Qt.AlignmentFlag.AlignCenter)

        #Création des boutons
        #Création de boutons Adhérent
        self.btnAjouterAdh = QPushButton("  Ajouter un adéhrent",self.widget1)
        self.layout.addWidget(self.btnAjouterAdh, 1, 0)
        self.btnAjouterAdh.setIcon(QIcon('addadh.png'))
        self.btnAjouterAdh.clicked.connect(self.btnAjouterAdhClicked)
        self.btnAfficherAdh = QPushButton("  Afficher liste des adéhrents",self.widget1)
        self.layout.addWidget(self.btnAfficherAdh, 2, 0)
        self.btnAfficherAdh.setIcon(QIcon('liste.jpg'))
        self.btnSupprimerAdh = QPushButton("  Supprimer un adéhrents",self.widget1)
        self.layout.addWidget(self.btnSupprimerAdh, 3, 0)
        self.btnSupprimerAdh.setIcon(QIcon('trash.png'))
        self.btnAfficherAdh.clicked.connect(self.btnAfficherAdhClicked)

        #Création de boutons Livre
        self.btnAjouterLiv = QPushButton("  Ajouter un livre",self.widget1)
        self.layout.addWidget(self.btnAjouterLiv, 1, 1)
        self.btnAjouterLiv.setIcon(QIcon('livre.png'))
        self.btnAjouterLiv.clicked.connect(self.btnAjouterLivClicked)
        self.btnAfficherLiv = QPushButton("  Afficher liste des livres",self.widget1)
        self.layout.addWidget(self.btnAfficherLiv, 2, 1)
        self.btnAfficherLiv.setIcon(QIcon('liste.jpg'))
        self.btnAfficherLiv.clicked.connect(self.btnAfficherLivClicked)
        self.btnSupprimerLiv = QPushButton("  Supprimer un livre",self.widget1)
        self.layout.addWidget(self.btnSupprimerLiv, 3, 1)
        self.btnSupprimerLiv.setIcon(QIcon('trash.png'))

        #Création de boutons Emprunt
        self.btnAjouterEmp = QPushButton("  Ajouter un emprunt",self.widget1)
        self.layout.addWidget(self.btnAjouterEmp, 1, 2)
        self.btnAjouterEmp.setIcon(QIcon('emprunt.png'))
        self.btnAjouterEmp.clicked.connect(self.btnAjouterEmpClicked)
        self.btnAfficherEmp = QPushButton("  Afficher liste des emprunts",self.widget1)
        self.layout.addWidget(self.btnAfficherEmp, 2, 2)
        self.btnAfficherEmp.setIcon(QIcon('liste.jpg'))
        self.btnAfficherEmp.clicked.connect(self.btnAfficherEmpClicked)
        self.btnSupprimerEmp = QPushButton("  Supprimer un emprunt",self.widget1)
        self.layout.addWidget(self.btnSupprimerEmp, 3, 2)
        self.btnSupprimerEmp.setIcon(QIcon('trash.png'))

        #Création de bouton Quitter
        self.btnQuitter = QPushButton("  Quitter",self.widget1)
        self.layout.addWidget(self.btnQuitter, 4, 0, 3, 0)
        self.btnQuitter.setIcon(QIcon('quitter.jpg'))
        self.btnQuitter.clicked.connect(self.btnQuitterClicked)
    def btnAjouterAdhClicked(self):
        self.w = FenAjouterAdh()
        self.w.show()
    def btnAfficherAdhClicked(self):
        self.w = FenAfficherAdh()
        self.w.show()
    def btnAjouterLivClicked(self):
        self.w = FenAjouterLiv()
        self.w.show()
    def btnAfficherLivClicked(self):
        self.w = FenAfficherLiv()
        self.w.show()
    def btnAjouterEmpClicked(self):
        self.w = FenAjouterEmp()
        self.w.show()
    def btnAfficherEmpClicked(self):
        self.w = FenAfficherEmp()
        self.w.show()
    def btnQuitterClicked(self):
        QCoreApplication.quit()


# On crée une instance de l'application
bd = BdTables()
app = QApplication([])
# on créé une instance de la classe MainWindowBiblio()
Fen_Principale = MainWindow()
#on affiche la fenetre principale
Fen_Principale.show()
# on démarre l'application
app.exec()
