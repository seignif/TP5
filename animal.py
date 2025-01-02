class Habitat:
    def __init__(self, description: str):
        self.description = description


class Tête:
    pass


class Corps:
    pass


class Membres:
    pass


class Animal:
    def __init__(self, tête: Tête, corps: Corps, membres: Membres, habitat: Habitat):
        self.tête = tête
        self.corps = corps
        self.membres = membres
        self.habitat = habitat


class Herbivore(Animal):
    pass


class Carnivore(Animal):
    pass


if __name__ == "__main__":
    # Création des composants
    tête = Tête()
    corps = Corps()
    membres = Membres()
    habitat_foret = Habitat(description="Forêt")
    habitat_savane = Habitat(description="Savane")
    habitat_bergerie = Habitat(description="Bergerie")

    # Création d'un herbivore
    lapin = Herbivore(tête=tête, corps=corps, membres=membres, habitat=habitat_foret)
    mouton = Herbivore(tête=tête, corps=corps, membres=membres, habitat=habitat_bergerie)

    # Création d'un carnivore
    lion = Carnivore(tête=tête, corps=corps, membres=membres, habitat=habitat_savane)

    # Tests d'affichage
    print(f"L'habitat du lapin est : {lapin.habitat.description}")
    print(f"L'habitat du lion est : {lion.habitat.description}")
    print(f"L'habitat du mouton est : {mouton.habitat.description}")
