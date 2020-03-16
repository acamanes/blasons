from ecu import *
from ecu_constants import *


taille = 80
space = 40
emaux = ["argent"]
liste_pieces = list(pieces.keys())

nbre = len(liste_pieces)//5

fig = plt.figure(figsize=(10, 10), dpi=80)
ax = fig.add_subplot(1, 1, 1)
fig.suptitle("Présentation des pièces", fontsize=20)
for k, part in enumerate(liste_pieces):
    pos = (k % 5) * (taille+2*space), -(k//5) * (taille+2*space)
    b = Ecu(forme="moderne",
            taille=(taille,taille),
            centre = pos,
            dessins = {},
            email=["argent"],
            parent=True)
    
    s = b.piece(part,
                email=["sable"])

    bd = b.dessins
    z0 = -350
    for (i,k) in enumerate(bd):
        (contour, email) = bd[k]
        draw_polygon(contour, email, z=z0)

    ax.text(pos[0], pos[1]+taille/2+10,
            part,
            ha="center", fontsize=12)
        

plt.axis("equal")
ax.axis("off")

plt.savefig("presentation_pieces.png")
