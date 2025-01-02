from typing import List


class Dossier:
    def __init__(self, état_civil: str, coordonnées: str):
        self.état_civil = état_civil
        self.coordonnées = coordonnées


class Professeur:
    def __init__(self, nom: str, matière: str, dossier: Dossier):
        self.nom = nom
        self.matière = matière
        self.dossier = dossier


class Élève:
    def __init__(self, nom: str, age: int, dossier: Dossier):
        self.nom = nom
        self.age = age
        self.dossier = dossier


class Classe:
    def __init__(self, professeur: Professeur):
        self.professeur = professeur
        self.élèves = []

    def ajouter_élève(self, élève: Élève):
        if len(self.élèves) < 30:
            self.élèves.append(élève)
        else:
            raise Exception("La classe ne peut pas contenir plus de 30 élèves.")

    def retirer_élève(self, élève: Élève):
        if élève in self.élèves:
            self.élèves.remove(élève)


if __name__ == "__main__":
    # Création d'un dossier pour le professeur
    dossier_prof = Dossier(état_civil="Jean Dupont", coordonnées="123 Rue Principale")
    professeur = Professeur(nom="Jean Dupont", matière="Mathématiques", dossier=dossier_prof)

    # Création de la classe
    classe_math = Classe(professeur=professeur)

    # Création des élèves
    dossier_eleve1 = Dossier(état_civil="Élève 1", coordonnées="456 Rue Secondaire")
    élève1 = Élève(nom="Alice", age=14, dossier=dossier_eleve1)

    dossier_eleve2 = Dossier(état_civil="Élève 2", coordonnées="789 Rue Tertiaire")
    élève2 = Élève(nom="Bob", age=15, dossier=dossier_eleve2)

    # Ajout des élèves à la classe
    classe_math.ajouter_élève(élève1)
    classe_math.ajouter_élève(élève2)

    # Affichage
    print(f"Professeur : {classe_math.professeur.nom}")
    print(f"Élèves dans la classe : {[élève.nom for élève in classe_math.élèves]}")
