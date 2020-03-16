from ecu import *
from ecu_constants import *


taille = 80
space = 40
emaux = ["argent"]
liste_partitions = list(parts.keys())

nbre = len(liste_partitions)//5

fig = plt.figure(figsize=(10, 10), dpi=80)
ax = fig.add_subplot(1, 1, 1)
fig.suptitle("Présentation des partitions", fontsize=20)
for k, part in enumerate(liste_partitions):
    pos = (k % 5) * (taille+2*space), -(k//5) * (taille+2*space)
    b = Ecu(forme="ancien",
            taille=(taille,taille),
            centre = pos,
            dessins = {},
            email=["argent"],
            parent=True)
    
    s = b.partition(part,
                    emaux=["argent"])

    bd = b.dessins
    z0 = -350
    for (i,k) in enumerate(bd):
        (contour, email) = bd[k]
        draw_polygon(contour, email, z=z0)
        if len(bd) <= 5 and i > 0:
            X, Y = contour["f1"]
            xmin,xmax = min(X),max(X)
            ymin,ymax = min(Y),max(Y)
            c = (xmax+xmin)/2, (ymax+ymin)/2
            ax.text(c[0],c[1],str(i),ha="center",fontsize=8)

    ax.text(pos[0], pos[1]+taille/2+10,
            part,
            ha="center", fontsize=12)
        

plt.axis("equal")
ax.axis("off")

plt.savefig("presentation_partitions.png")
