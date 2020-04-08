import ecu
from ecu_constants import *


taille = 80
space = 40
emaux = ["argent"]
liste_meubles = list(meubles.keys())
liste_meubles.sort()
print(liste_meubles)

nbre = len(liste_meubles)//5

fig = plt.figure(figsize=(15, 10), dpi=80)
ax = fig.add_subplot(1, 1, 1)
fig.suptitle("Présentation des meubles",fontsize=20)
for k, animal in enumerate(liste_meubles):
    pos = (k % 5) * (taille+2*space), -(k//5) * (taille+2*space)
    d, _, _ = image(meubles[animal],
                    (taille,taille),
                    pos)            
    draw_polygon(d,emaux)
    ax.text(pos[0], pos[1]+taille/2+10,
            animal.replace(" ", "\n "),
            ha="center", fontsize=12)

for (k, animal) in enumerate(liste_meubles):
    ax.text(5 * (taille + 2*space), taille/2+space-30*k,
            animal + " : " + ", ".join(attributs[animal]),
            ha="left", fontsize=12)
        

plt.axis("equal")
plt.axis([-taille/2,9*(taille+2*space),pos[1]+4*taille,-2*taille])
ax.axis("off")

plt.savefig("presentation_meubles.png")
plt.savefig("presentation_meubles.ps",
            papertype="a4",
            orientation="landscape")
import os
os.system("ps2pdf presentation_meubles.ps")
