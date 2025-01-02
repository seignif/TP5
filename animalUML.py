classDiagram
    class Habitat {
    + description : str
    }

    class Animal{
    + tête : str
    + corps : str
    + membres : int
    + habitat : Habitat
    }
    class Tête{

    }

    class Corps{

    }
    class Membres{

    }

    class Herbivore{
    + Specific to herbivores
    }

    class Carnivore{
    + Specific to carnivores
    }
Animal "1" -- "1" Tête   : own
Animal "1"-- "1" Membres   : own
Animal "1" *-- "1" Corps   : own
Animal "1..n" --> "1" Habitat  : live
Animal  --|>  Herbivore : is a
Animal  --|>  Carnivore : is a