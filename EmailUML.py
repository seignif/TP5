classDiagram
    class Email{
        + titre : str
        + texte : str
        + expediteur : str
        + destination : str
        + Fichier : list[FichierJoint]
        +ajouter_fichier()
        +retirer_fichier()
    }
    class FichierJoint{
        + nom : str
        + taille : int
    }
Email "0..1" *-- "0..n" FichierJoint : owns