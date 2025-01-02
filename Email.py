from typing import List


class FichierJoint:
    def __init__(self, nom: str, taille: int):
        self.nom = nom
        self.taille = taille


class Email:
    def __init__(self, titre: str, texte: str, expediteur: str, destination: str):
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers: List[FichierJoint] = []

    def ajouter_fichier(self, fichier: FichierJoint):
        self.fichiers.append(fichier)

    def retirer_fichier(self, fichier: FichierJoint):
        if fichier in self.fichiers:
            self.fichiers.remove(fichier)


if __name__ == "__main__":
    # Création d'un email
    email = Email(titre="Rapport", texte="Voici le rapport demandé.", expediteur="expediteur@example.com",
                  destination="destination@example.com")

    # Création de fichiers joints
    fichier1 = FichierJoint(nom="rapport.pdf", taille=1024)
    fichier2 = FichierJoint(nom="diagramme.png", taille=2048)

    # Ajout des fichiers à l'email
    email.ajouter_fichier(fichier1)
    email.ajouter_fichier(fichier2)

    # Affichage des fichiers joints
    print(f"Email : {email.titre}")
    print(f"Fichiers joints : {[fichier.nom for fichier in email.fichiers]}")
