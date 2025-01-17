from ecu import *

# Creation de l ecu
# La forme "moderne" fonctionne bien
# La forme "ancien" non...
# email : couleur du blason
monblase = Ecu(
    forme="moderne",
    email=["or"],
)

# Permet de partitionner le blason de creer des sous-blasons
# Les partitions possible sont decrites sur "presentation_partitions.png"
[b1,b2,b3,b4] = monblase.partition(
    nom = "écartelé",
    emaux = ["or","gueules",
           "gueules","or"]
)

# Ajout d une piece sur le premier blason
# La liste des pieces est decrite sur "presentation_pieces.png"
b1.piece(nom="chef", email=["azur"])
# Ajout d un meuble sur le chef (ne marche pas encore pour les autres pieces)
# Liste des meubles disponibles sur 
b1.meuble_piece(piece="chef",
                nom="fleur de lys",
                nombre = 5,
                emaux=["or"])

b1.meuble(nom="aigle au vol abaissé",
          emaux=["sable","gueules",
                 "or","gueules","argent"])

# Partitionnement d un sous blason
b11,b12,b13,b14=b4.partition(
    nom = "écartelé",
    emaux=["gueules","or","or","gueules"])
# Ajout de piece
b11.piece(nom = "4 burelles",
          email=["argent"])
# Nouveau partitionnement
b12.partition(nom = "taillé",
              emaux = ["sable","argent"])
# Ajout de piece
b13.piece(nom = "2 barres",
          email = ["gueules"])
# Nouveau partitionnement
b14.partition(
    nom = "écartelé",
    emaux = ["or","argent","argent","or"])
# Ajout d un meuble
b14.meuble(nom="tortue",
           emaux=["sinople","sable",
                  "sinople","argent"])

[b21,b22,b23,b24] = b2.partition(
    nom = "écartelé",
    emaux=["or", ("hermine", ["or", "gueules"]),"gueules","or"])
b21.partition(nom = "fascé",emaux=["azur","sinople"])
b22.piece(nom = "chef",email=["argent"])
b22.meuble_piece(piece="chef",nom="ancre",
                 nombre=4,
                 emaux=["gueules"])
b22.meuble(nom="rat",
           translation=(0,-b22.height/6),
           emaux=["argent","sable"])

b23.meuble(nom="cerbère",
           emaux=["argent","or","or","sable"])

b24.partition(nom = "écartelé",
              emaux = ["azur","sinople","sinople","azur"])

b3.partition(nom = "fascé",emaux=["gueules","or"])
b3.meuble(nom="lion rampant",
          contourne=False,
          translation=(b3.width/5,0),
          echelle=1,
          emaux=["or", "gueules", "azur", "argent"])

b3.meuble(nom="dauphin",
          contourne=True,
          translation=(-b3.width/5,0),
          echelle=1,
          emaux=["argent", "or", "argent"])

# Enregistrement du fichier avec possibilite de choisir le nom
monblase.dessine(fichier="alain_blase")
