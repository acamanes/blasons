from ecu import *
monblase = Ecu(
    forme="moderne",
    email=[("hermine", ["sable", "argent"])],
)
monblase.piece(
    nom="chef",
    email=[("vair", ["or", "azur"])]
)
monblase.meuble(nom="marmitte",
                emaux=["gueules","sable"])
monblase.dessine(fichier="aigle_blase")
