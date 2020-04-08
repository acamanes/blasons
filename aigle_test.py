from ecu import *

# Creation de l ecu
# La forme "moderne" fonctionne bien
# La forme "ancien" non...
# email : couleur du blason
monblase = Ecu(
    forme="moderne",
    email=["or"],
)

monblase.meuble(nom="aigle au vol abaissé",
          emaux=["sable","gueules","or","gueules","argent"])

# Enregistrement du fichier avec possibilite de choisir le nom
monblase.dessine(fichier="aigle_blase")
