classDiagram
    class Classe{
    -professeur: Professeur
    - eleves: List[Eleve]
    + ajouter_eleve()
    + retirer_eleve()

    }

    class Professeur{
    + nom: str
    + matière: str
    dossier: Dossier
    }

    class Eleve{
    + nom: str + age: int
    dossier: Dossier
    }

    class Dossier{
    + état_civil: str
    + coordonnées: str
    }
Classe"1" --o "1..n" Professeur: own
Classe "1" --> "0..30" Eleve: own
Dossier "1" --> "1" Professeur: own
Dossier "1" --> "1" Eleve: own