from ecu_external import *
from collections import OrderedDict

# Couleurs
emailtocouleur = {
                  # Couleurs
                  "gueules": "red",
                  "azur": "deepskyblue",
                  "sable": "black",
                  "sinople": "limegreen",
                  "pourpre": "mediumorchid",
                  # Metaux
                  "or": "yellow",
                  "argent": "white"
                  }

# Formes de blasons
formes = OrderedDict()
formes["ancien"] = txttoimg("./meubles/ecu_ancien.txt")
formes["moderne"] = txttoimg("./meubles/ecu_moderne.txt")
formes["carré"] = {"f1":((-100,-100,100,100,-100), (100,-100,-100,100,100))},\
                  (200,200),(0,0)
formes["losange"] = {"f1":((0,-100,0,100,0), (100,0,-100,0,100))},\
                  (200,200),(0,0)

# Fourrures
fourruresliste = OrderedDict()
fourruresliste["vair"] = txttoimg("./meubles/vair.txt")
fourruresliste["hermine"] = txttoimg("./meubles/hermine.txt")


# Partitions
parts = OrderedDict()
# 
parts["plain"] = (1,1)
# 1 trait
parts["parti"] = (1,2)
parts["coupé"]=(2,1)
parts["tranché"]=(2,"tranché")
parts["taillé"]=(2,"taillé")
# 2 traits
parts["écartelé"]=(2,2)
# 3 traits
parts["palé de 4 pièces"]=(1,4)
parts["fascé de 4 pièces"]=(4,1)
parts["bandé de 4 pièces"]=(4, "tranché")
parts["barré de 4 pièces"]=(4, "taillé")
# 5 traits
parts["palé"]=(1,6)
parts["fascé"]=(6,1)
parts["bandé"]=(6, "tranché")
parts["barré"]=(6, "taillé")
# 7 traits
parts["palé de 8 pièces"]=(1,8)
parts["fascé de 8 pièces"]=(8,1)
parts["bandé de 8 pièces"]=(8, "tranché")
parts["barré de 8 pièces"]=(8, "taillé")
# 9 traits
parts["vergeté"]=(1,10)
parts["burelé"]=(10,1)
parts["coticé"]=(10, "tranché") # Moins en pratique
parts["coticé en barres"]=(10, "taillé")

# Pieces
pieces = OrderedDict()
# 1 piece
pieces["chef"]=((4,1),[0]) # Triche pour avoir + petit
pieces["pal"]=((1,3),[2])
pieces["fasce"]=((3,1),[1])
pieces["bande"]=((5,"tranché"),[2]) # Triche pour avoir + petit
pieces["barre"]=((5,"taillé"),[2]) # Triche pour avoir + petit

# 2 pieces
pieces["2 pals"]=((1,5),[1,3])
pieces["2 fasces"]=((5,1),[1,3])
pieces["2 bandes"]=((5, "tranché"),[1,3])
pieces["2 barres"]=((5, "taillé"),[1,3])
# 3 pieces
pieces["3 pals"]=((1,7),[1,3,5])
pieces["3 fasces"]=((7,1),[1,3,5])
pieces["3 bandes"]=((7, "tranché"),[1,3,5])
pieces["3 barres"]=((7, "taillé"),[1,3,5])
# 4 pieces
pieces["4 vergettes"]=((1,9),[1,3,5,7])
pieces["4 burelles"]=((9,1),[1,3,5,7])
pieces["4 cotices"]=((9, "tranché"),[1,3,5,7])
pieces["4 cotices en barre"]=((9, "taillé"),[1,3,5,7])

# Meubles
attributs = OrderedDict()
meubles = OrderedDict()
# Animaux
lion_rampant = txttoimg("./meubles/lion_rampant.txt")
meubles["lion rampant"]=lion_rampant
attributs["lion rampant"] = ["Animal", "Griffes", "Langue", "Oeil"]
#-----
cerbere = txttoimg("./meubles/cerbere.txt")
meubles["cerbère"]=cerbere
attributs["cerbère"] = ["Animal", "Griffes", "Langue", "Oeil"]
#-----
rat = txttoimg("./meubles/rat.txt")
meubles["rat"]=rat
attributs["rat"] = ["Animal", "Oeil"]
#-----
autruche = txttoimg("./meubles/autruche.txt")
meubles["autruche"]=autruche
attributs["autruche"] = ["Animal", "Oeil"]
#-----
cerf_passant = txttoimg("./meubles/cerf_passant.txt")
meubles["cerf passant"]=cerf_passant
attributs["cerf passant"] = ["Animal", "Oeil"]
#-----
ecureuil = txttoimg("./meubles/ecureuil.txt")
meubles["écureuil"] = ecureuil
attributs["écureuil"] = ["Animal", "Gland", "Oeil"]
#-----
salamandre = txttoimg("./meubles/salamandre.txt")
meubles["salamandre"] = salamandre
attributs["salamandre"] = ["Animal", "Langue", "Oeil"]
#-----
aigle_vol_abaisse = txttoimg("./meubles/aigle_vol_abaisse.txt")
meubles["aigle au vol abaissé"] = aigle_vol_abaisse
attributs["aigle au vol abaissé"] = ["Animal", "Griffes", "Bec", "Langue", "Oeil"]
#-----
ours_rampant = txttoimg("./meubles/ours_rampant.txt")
meubles["ours rampant"] = ours_rampant
attributs["ours rampant"] = ["Animal", "Griffes/Dents", "Langue", "Oeil"]
#-----
leopard_passant = txttoimg("./meubles/leopard_passant.txt")
meubles["léopard passant"] = leopard_passant
attributs["léopard passant"] = ["Animal", "Griffes/Dents", "Langue", "Oeil"]
#-----
dauphin = txttoimg("./meubles/dauphin.txt")
meubles["dauphin"] = dauphin
attributs["dauphin"] = ["Animal", "Nageoires", "Oeil"]
#-----
licorne_passante = txttoimg("./meubles/licorne_passante.txt")
meubles["licorne passante"] = licorne_passante
attributs["licorne passante"] = ["Animal", "Sabots", "Corne", "Langue", "Oeil"]
#-----
tortue = txttoimg("./meubles/tortue.txt")
meubles["tortue"] = tortue
attributs["tortue"] = ["Tête/Queue", "Carapace", "Pattes", "Oeil"]
#-----
dragon = txttoimg("./meubles/dragon.txt")
meubles["dragon"] = dragon
attributs["dragon"] = ["Animal", "Griffes/Dents", "Langue", "Oeil"]
#-----
cheval_cabre = txttoimg("./meubles/cheval_cabre.txt")
meubles["cheval cabré"] = cheval_cabre # Animal, Oeil
attributs["cheval cabré"] = ["Animal", "Oeil"]
#-----

# Vegetaux
arbre_arrache = txttoimg("./meubles/arbre_arrache.txt")
meubles["arbre arraché"]=arbre_arrache # Tronc, Feuillage
attributs["arbre arraché"] = ["Tronc", "Feuillage"]
#-----
fleur_de_lys = txttoimg("./meubles/fleur_de_lys.txt")
meubles["fleur de lys"]=fleur_de_lys
attributs["fleur de lys"] = ["Fleur"]
#-----
pomme = txttoimg("./meubles/pomme.txt")
meubles["pomme"]=pomme
attributs["pomme"] = ["Fruit", "Feuille"]
#-----

# Divers
ancre = txttoimg("./meubles/ancre.txt")
meubles["ancre"]=ancre
attributs["ancre"] = ["Ancre"]
#-----
tour = txttoimg("./meubles/tour.txt")
meubles["tour"]=tour
attributs["tour"] = ["Tour", "Ouvertures"]
#-----
tour_maconnee = txttoimg("./meubles/tour_maconnee.txt")
meubles["tour maçonnée"]=tour_maconnee
attributs["tour maçonnée"] = ["Tour", "Ouvertures"]
#-----
marmitte = txttoimg("./meubles/marmitte.txt")
meubles["marmitte"]=marmitte
attributs["marmitte"] = ["Marmitte", "Intérieur"]
#-----
couronne = txttoimg("./meubles/couronne.txt")
meubles["couronne"]=couronne
attributs["couronne"] = ["Couronne", "Intérieur"]
#-----
hermine = txttoimg("./meubles/hermine.txt")
meubles["hermine"]=hermine # 
attributs["hermine"] = ["Hermine"]
#-----



#################

# Definition des fourrures
vair = fourruresliste["vair"]
herminep = fourruresliste["hermine"]

hvair, width, height = image(vair, (1,1), (0,0), sy=False, proportional=True)
vair_path = Polygon(
    [[hvair["f101"][0][i], hvair["f101"][1][i]] for i in range(len(hvair["f101"][0]))],
    closed=True, fill=False).get_path()

hhermine, width, height = image(herminep, (1,1), (0,0), sy=False, proportional=True)

hermine_path = [
    Polygon(
        [[hhermine["f10"+n][0][i], hhermine["f10"+n][1][i]] for i in range(len(hhermine["f10"+n][0]))],
        closed=True, fill=False).get_path()
    for n in "1234"]

    
hermine1_path = Polygon(
    [[hhermine["f101"][0][i], hhermine["f101"][1][i]] for i in range(len(hhermine["f101"][0]))] +
    [[hhermine["f102"][0][i], hhermine["f102"][1][i]] for i in range(len(hhermine["f102"][0]))] +
    [[hhermine["f103"][0][i], hhermine["f103"][1][i]] for i in range(len(hhermine["f103"][0]))],
    closed=True, fill=True).get_path()

hermine2_path = Polygon(
    [[hhermine["f104"][0][i], hhermine["f104"][1][i]] for i in range(len(hhermine["f104"][0]))],
                       closed=True, fill=True).get_path()


class VairHatch(matplotlib.hatch.Shapes):
    """
    Custom hatches defined by a path drawn inside [-0.5, 0.5] square.
    Identifier 'vair'.
    """
    filled = True
    size = 1
    path = vair_path

    def __init__(self, hatch, density):
        self.num_rows = (hatch.count('vair')) * 2
        self.shape_vertices = self.path.vertices
        self.shape_codes = self.path.codes
        matplotlib.hatch.Shapes.__init__(self, hatch, density)

class Hermine0Hatch(matplotlib.hatch.Shapes):
    """
    Custom hatches defined by a path drawn inside [-0.5, 0.5] square.
    Identifier 'hermine'.
    """
    filled = True
    size = 1.0
    path = hermine_path[0]

    def __init__(self, hatch, density):
        self.num_rows = (hatch.count('hermine0')) * 2
        self.shape_vertices = self.path.vertices
        self.shape_codes = self.path.codes
        matplotlib.hatch.Shapes.__init__(self, hatch, density)

class Hermine1Hatch(matplotlib.hatch.Shapes):
    """
    Custom hatches defined by a path drawn inside [-0.5, 0.5] square.
    Identifier 'hermine'.
    """
    filled = True
    size = 1.0
    path = hermine_path[1]

    def __init__(self, hatch, density):
        self.num_rows = (hatch.count('hermine1')) * 2
        self.shape_vertices = self.path.vertices
        self.shape_codes = self.path.codes
        matplotlib.hatch.Shapes.__init__(self, hatch, density)

class Hermine2Hatch(matplotlib.hatch.Shapes):
    """
    Custom hatches defined by a path drawn inside [-0.5, 0.5] square.
    Identifier 'hermine'.
    """
    filled = True
    size = 1.0
    path = hermine_path[2]

    def __init__(self, hatch, density):
        self.num_rows = (hatch.count('hermine2')) * 2
        self.shape_vertices = self.path.vertices
        self.shape_codes = self.path.codes
        matplotlib.hatch.Shapes.__init__(self, hatch, density)
    
class Hermine3Hatch(matplotlib.hatch.Shapes):
    """
    Custom hatches defined by a path drawn inside [-0.5, 0.5] square.
    Identifier 'hermine'.
    """
    filled = True
    size = 1.0
    path = hermine_path[3]

    def __init__(self, hatch, density):
        self.num_rows = (hatch.count('hermine3')) * 2
        self.shape_vertices = self.path.vertices
        self.shape_codes = self.path.codes
        matplotlib.hatch.Shapes.__init__(self, hatch, density)

        
matplotlib.hatch._hatch_types.append(VairHatch)
matplotlib.hatch._hatch_types.append(Hermine0Hatch)
matplotlib.hatch._hatch_types.append(Hermine1Hatch)
matplotlib.hatch._hatch_types.append(Hermine2Hatch)
matplotlib.hatch._hatch_types.append(Hermine3Hatch)
