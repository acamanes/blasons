# TODO : 
# Meubles dans le chef : sans repetition ?
# Reprendre ecu ancien - D'autres ecus ?
# Taille des hatch dans partition

import matplotlib.pyplot as plt
from matplotlib import path
import matplotlib.hatch


from ecu_external import *
from ecu_constants import *

class Ecu:
    def __init__(self,
                 forme="ancien",
                 taille=(200, 200),
                 centre=(0,0),
                 email=["argent"],
                 dessins={},
                 parent=True):
        """Definition
        forme : "ancien"/"moderne"/ecu
        taille : couple (width, height)
        centre : center (x, y)
        email : color in heraldic name
        dessins : dict of drawings (key : int : zorder)
        parent : True iff fundamental ecu
        """
        # Shape of the ecu
        self.width = taille[0]
        self.height = taille[1]
        # Position of the center
        self.xcenter=centre[0]
        self.ycenter=centre[1]
        self.ischef = False
        # dictionnaire des objets a tracer
        self.dessins = dessins
        # Chargement de la forme
        if isinstance(forme,str):
            self.forme=formes[forme]
        else:
            self.forme=forme, taille, centre
        # Mise aux dimensions de la forme
        if parent:
            d, taille, pos = image(self.forme, taille,
                            (self.xcenter,self.ycenter),
                            proportional=False)
            self.forme = d, taille, pos
        else:
            d, _, _ = self.forme
        # Ajout de la forme aux dessins
        d = {"f1":(d["f1"][0]+[d["f1"][0][0]],
                   d["f1"][1]+[d["f1"][1][0]])}

        ajoute_dessin(self.dessins, (d, email))

    def partition(self,
                  nom = "plain",
                  emaux = ["gueules"]):
        """
        partition : type de partition
        emaux : liste des couleurs
        """
        # Ca c'est crado !! A changer :-)
        partition = nom
        # Contour du blason a partitionner
        nom = self.forme
        # Parition est soit un couple ligne/col, soit un nom
        if isinstance(partition, str):
            nrows, ncols = parts[partition]
        else:
            nrows, ncols = partition
        if ncols == "tranché":
            sousecus = self.partition_oblique(nom, (nrows, ncols))
        elif ncols == "taillé":
            sousecus = self.partition_oblique(nom, (nrows, ncols))
        else :
            self.nrows = nrows
            self.ncols = ncols
            sousecus = self.rectpartition(nom, (nrows, ncols))
        # Creation des sous-blasons stockes dans une liste
        sousblasons = []
        for (k, contour) in enumerate(sousecus):
            if contour["X"] != []:
                # if fourrures != None:
                    # f = fourrures[k%len(fourrures)]
                # else:
                    # f = None
                dcontour = {"f1":(contour["X"], contour["Y"])}
                Xmin, Xmax = min(contour["X"]), max(contour["X"])
                Ymin, Ymax = min(contour["Y"]), max(contour["Y"])
                b = Ecu(forme=dcontour,
                        taille = (Xmax-Xmin, Ymax-Ymin),
                        centre= ((Xmax+Xmin)/2, (Ymax+Ymin)/2),
                        dessins = self.dessins,
                        # fourrure = f,
                        email = [emaux[k%len(emaux)]],
                        parent=False)
                sousblasons.append(b)
        return sousblasons


    def rectpartition(self, nom, couple):
        d = nom[0]
        forme = d["f1"][0], d["f1"][1]
        plgs = rectangles(forme, couple)
        dec = decoupe(forme, plgs)
        djoli = []
        for i in range(len(dec)):
            dico = {}
            b = dec[i]
            dico["X"] = [k[0] for k in b]
            dico["Y"] = [k[1] for k in b]
            djoli.append(dico)
        return djoli

    def partition_oblique(self, nom, couple):
        d = nom[0]
        forme = d["f1"][0], d["f1"][1]
        plgs = parallelograms(forme, couple)
        dec = decoupe(forme, plgs)
        djoli = []
        for i in range(len(dec)):
            dico = {}
            b = dec[i]
            dico["X"] = [k[0] for k in b]
            dico["Y"] = [k[1] for k in b]
            djoli.append(dico)
        return djoli

    def piece(self, nom=None, email=["or"]):
        """Trace les pieces
        email : couleur de la piece
        """
        # Lecture des pieces choisies
        (nrows,ncols), selection = pieces[nom]
        # Decoupage du blason en partitions
        if ncols == "tranché":
            # d = self.oldpartition_oblique(self.forme, nrows, 1)
            d = self.partition_oblique(self.forme, (nrows, ncols))
        elif ncols == "taillé":
            # d = self.oldpartition_oblique(self.forme, nrows, -1)
            d = self.partition_oblique(self.forme, (nrows, ncols))
        else :
            if nrows > 1:
                self.ischef = True
            d = self.rectpartition(self.forme, (nrows,  ncols))
        # Trace des partitions qui correspondent a la piece
        for k in selection:
            try:
                dcontour = {"f1":(d[k]["X"], d[k]["Y"])}
                dcontour = {"f1":(d[k]["X"]+[d[k]["X"][0]],
                              d[k]["Y"]+[d[k]["Y"][0]])}
                ajoute_dessin(self.dessins, (dcontour, email))
            except:
                pass
                

    def meuble(self,
               # position = 1,
               nom = "lion rampant",
               emaux=["or"],
               contourne = False,
               translation=(0,0),
               echelle=1,):
        """Positionne les meubles sur l ecu
        position : numero de la partition ou afficher le meuble
        nom : nom renvoyant au fichier image du meuble
        emaux : liste des couleurs a appliquer
        contourne : True pour avoir une relfexion verticale
        translation : translate le meuble de (vx, vy)
        echelle : met a l echelle le meuble d un facteur s
        """
        # Extremites du blason
        left, right = -self.width/2, self.width/2
        top, bottom = self.height/2, -self.height*(0.4)
        # Translate le meuble en presence du chef
        tx, ty = 0, 0
        if self.ischef:
            tx, ty = 0, -0.15
        # Position du centre en coordonnees barycentriques
        b = ([1/2,1/2],[1/2,1/2])
        # Echelle en largeur/hauteur a appliquer au meuble
        scw, sch = 1, 1
        if self.ischef:
            sch = 0.9
        sh = sch * 0.5 * echelle
        sw = scw * 0.5 * echelle

        # Positions et echelle
        pos = [self.xcenter+translation[0] + tx*self.width + b[0][0]*left + b[0][1]*right,\
                self.ycenter+translation[1] + ty*self.height + b[1][0]*top + b[1][1]*bottom]
        scale = (sw * self.width, sh * self.height)
        # Image positionnee et Mise a l echelle
        fd, Xdim, Ydim = image(meubles[nom], scale, pos,
                               sy=contourne)
        # Trace
        ajoute_dessin(self.dessins, (fd, emaux))

    def meuble_piece(self,
                     piece = "chef",
                     nom = "lion",
                     emaux=["or"],
                     nombre=1,
                     translation=[0,0],
                     echelle=1,
                     contourne=False):
        """Positionne les meubles sur l ecu
        position : numero de la partition ou afficher le meuble
        nom : nom renvoyant au fichier image du meuble
        emaux : liste des couleurs a appliquer
        contourne : True pour avoir une relfexion verticale
        translation : translate le meuble de (vx, vy)
        echelle : met a l echelle le meuble d un facteur s
        """
        # Extremites du blason
        left, right = self.xcenter-self.width/2, self.xcenter+self.width/2
        top, bottom = self.ycenter+self.height/2, self.ycenter+self.height/2-self.height/4
        for i in range(nombre):
            # Position du centre en coordonnees barycentriques
            b =(((1+i)/(1+nombre),1-(1+i)/(1+nombre)),(1/2,1/2))
            # Echelle en largeur/hauteur a appliquer au meuble
            scw, sch = 0.5, 0.5
            sh = sch * echelle
            sw = scw * echelle

            # Positions et echelle
            pos = [translation[0] + b[0][0]*left+b[0][1]*right,\
                   translation[1] + b[1][0]*top+b[1][1]*bottom]
            scale = (sw * (right-left), sh * (top-bottom))
            # Image positionnee et Mise a l echelle
            fd, Xdim, Ydim = image(meubles[nom], scale, pos)
            ajoute_dessin(self.dessins, (fd, emaux))

        
    def dessine(self, fichier="mon_blase"):
        plt.close()
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)        
        # self.
        ax.axis([-self.width/2, self.width/2,
                      -self.height/2, self.height/2])
        # self.
        ax.axis("equal")
        # self.
        ax.axis("off")
        # self.
        d = self.dessins
        z0 = -350
        k = int(abs(z0)//len(d))
        for i in range(len(d)):
            (contour, email) = d[i]
            draw_polygon(contour,
                         emaux = email, z=z0+i*k)
        fig.savefig(fichier+".pdf")
        fig.savefig(fichier+".png", dpi=300)
