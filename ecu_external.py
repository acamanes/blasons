import matplotlib.pyplot as plt

precision = 15
epsilon = 10**(-precision)

# Definition des couleurs
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

def center(liste, lmin, lmax):
    """Centere les listes autour de (lmin+lmax)/2"""
    tl = -(lmax+lmin)/2
    return [l+tl for l in liste]

def txttoimg(lien):
    """Input : fichier texte
    Output : liste des abscisses, ordonnees, largeur, hauteur
    """
    Xmin, Xmax = float("inf"), -float("inf")
    Ymin, Ymax = float("inf"), -float("inf")
    # Ouverture du fichier
    with open(lien,'r') as f:
        chaine = f.read()
        # Recuperation des chemins
        liste_chemins = chaine.split(",")
        # Pour chacun des chemins, recuperation des coordonnees
        d = {}
        for path in liste_chemins:
            s = path.split(":")
            if len(s) > 1:
                d[s[0]] = s[1]
        # Pour chacun des chemins, recuperation des couples
        # abscisses / ordonnees
        fd = {}
        for path in d:
            chaine = d[path]
            ln = chaine.split(" ")
            X, Y = [], []
            for i in range(0,len(ln),2):
                X.append(float(ln[i]))
                Y.append(-float(ln[i+1]))
            fd[path] = (X,Y)
            Xmin, Xmax = min(min(X), Xmin), max(max(X), Xmax)
            Ymin, Ymax = min(min(Y), Ymin), max(max(Y), Ymax)

        # Stockage des couples centres
        for path in fd:
            X, Y = fd[path]
            fd[path] = (center(X, Xmin, Xmax),
                        center(Y, Ymin, Ymax))
    return fd, (Xmax-Xmin, Ymax-Ymin), (0, 0)

def image(nom, ndim, pos, sy=False, proportional=True):
    """Translate et mise a l echelle des images"""
    (nw, nh) = ndim
    d, (Xdim, Ydim), (Xcenter, Ycenter) = nom
    # Calcul de l echelle a appliquer
    scalex, scaley = nw/Xdim, nh/Ydim
    if proportional:
        scalex = min(scalex, scaley)
        scaley = min(scalex, scaley)
    # Symetrie verticale
    if sy:
        eg = -1
    else:
        eg=1
    # Mise a l echelle de chacun des chemins
    nd = {}
    for k in d:
        X, Y = d[k]
        X = [eg * x * scalex + pos[0] for x in X]
        Y = [y * scaley + pos[1] for y in Y]
        nd[k] = X, Y
    return nd, Xdim, Ydim

def ajoute_dessin(d, f):
    """Ajoute un dessin au dictionnaire des dessins
    La numerotation des cles permet de gerer les profondeurs"""
    if d == {}:
        d[0] = f
    else:
        zmax = max(d.keys())
        d[zmax+1] = f

def draw_polygon(fd, emaux=["or"], z=-100):
    """Trace les polygones et leurs pourtours"""
    # Types de chemins : f (filled), l (lines)
    # Nombre de groupes
    ngpes = max([int(path[1])-1 for path in fd])
    for path in fd:
        X, Y = fd[path]
        # Trace des polygones
        if path[0] == "f":
            # Numero de groupe
            gpe = int(path[1])-1
            plt.fill(X, Y,
                     color=emailtocouleur[emaux[gpe%len(emaux)]],
                     # edgecolor="k",
                     zorder=z+10*gpe)
            # Trace des contours
            plt.plot(X, Y, color="k", zorder=z+10*gpe)
        else:
            # Trace des contours au dessus de tous les groupes
            plt.plot(X, Y, color="k", zorder=z+10*(ngpes+1))

def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)

def angle(a, b, c):
    ab = (b[0] - a[0], b[1] - a[1])
    ac = (c[0] - a[0], c[1] - a[1])
    if ac == (0,0) or ac == (0,0) :
        return 0
    det = ab[0] * ac[1] - ab[1] * ac[0]
    return det

def is_in_square(d, plg):
    hg, bg, bd, hd = plg
    (X, Y) = d
    nX, nY = [], []
    xb, yb = (bd[0] - bg[0]), (bd[1] - bg[1])
    xc, yc = (hg[0] - bg[0]), (hg[1] - bg[1])
    d = xb * yc - yb * xc
    for i in range(len(X)):
        xp = X[i] - bg[0]
        yp = Y[i] - bg[1]
        oned = 1.0 / d;
        bb = (xp * yc - yp * xc) * oned
        cc = (xb * yp - xp * yb) * oned
        inside = (-epsilon <= bb <= 1 + epsilon) &\
                 (-epsilon <= cc <= 1 + epsilon)
        if inside:
            nX.append(X[i])
            nY.append(Y[i])
    return {"X":nX, "Y":nY}

def rectangles(forme, subdivision):
    X, Y = forme
    nrows, ncols = subdivision
    Xmin, Xmax = min(X), max(X)
    Ymin, Ymax = min(Y), max(Y)
    lrects = []
    dx, dy = (Xmax-Xmin)/ncols, (Ymax-Ymin)/nrows
    for j in range(nrows):
        ymin, ymax = Ymax - (j+1) * dy, Ymax - j * dy
        for i in range(ncols):
            xmin, xmax = Xmin + i * dx, Xmin + (i+1) * dx
            xmin, xmax = round(xmin,precision), round(xmax,precision)
            ymin, ymax = round(ymin,precision), round(ymax,precision)
            lrects.append(((xmin, ymax), (xmin,ymin),
                           (xmax, ymin), (xmax, ymax)))
    return lrects

def parallelograms(forme, subdivision):
    X, Y = forme
    ncols, s = subdivision
    Xmin, Xmax = min(X), max(X)
    Ymin, Ymax = min(Y), max(Y)
    n = 1
    
    if s == "taillé":
        Xmin, Xmax = Xmax, Xmin

    diago = distance((Xmin, Ymin), (Xmax, Ymax))
    dly = diago * diago/ncols /(Ymax-Ymin)
    dlx = diago * diago/ncols /(Xmax-Xmin)
        
    lplgs = []
    for i in range(ncols):
        # Top and bottom limits
        xmin, xmax = round(Xmin+n*i*dlx,precision), round(Xmin+n*(i+1)*dlx,precision)
        ymin, ymax = round(Ymin+i*dly,precision), round(Ymin+(i+1)*dly,precision)
        lplgs.append(((xmin, Ymin), (xmax, Ymin),
                      (Xmin,ymax), (Xmin, ymin)))
    return lplgs

def position(point, liste):
    n = len(liste)
    indice = 0
    if n == 0:
        return -1
    for k in range(len(liste)):
        ak = angle(point, liste[k%n], liste[(k+1)%n])
        if ak < 0:
            indice  = k
    return indice

def new_is_in_blason(p, poly):
    x, y = p
    n = len(poly)
    cpt = 0
    inside = False
    p1x, p1y = poly[0]
    for i in range(1,n+1):
        p2x, p2y = poly[i%n]
        if abs(p1y - p2y) <= epsilon:
            if abs(y - p1y) <= epsilon:
                if min(p1x,p2x) < x < max(p1x, p2x):
                    return True
                elif x < min(p1x, p2x):
                    cpt += 1
                    inside = not inside
                    print(x, y, inside)
        elif min(p1y,p2y) < y < max(p1y,p2y):
            test = x - ((y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x)
            if abs(test) <= epsilon:
                return True
            elif test < epsilon:
                cpt += 1
                inside = not inside
        p1x, p1y = p2x, p2y
    return inside
              
    

def is_in_blason(p, poly):
    x, y = p
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(1, n + 1):
        p2x, p2y = poly[i % n]
        if abs(p1y - p2y) <= epsilon:
            if abs(y - p1y) <= epsilon:
                if min(p1x, p2x)+epsilon <= x <= max(p1x, p2x)-epsilon:
                    # point is on horisontal edge
                    return True
                elif x < min(p1x, p2x)-epsilon:  # point is to the left from current edge
                    inside = not inside
                    print(inside, x, y)
        else:  # p1y!= p2y
            if min(p1y, p2y)+epsilon <= y <= max(p1y, p2y)-epsilon:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if abs(x - xinters) <= epsilon:  # point is right on the edge
                    return True
                if x < xinters-epsilon:  # point is to the left from current edge
                    inside = not inside
                    print(inside, x, y)
        p1x, p1y = p2x, p2y
    return inside

def decoupe(forme, plgs):
    """forme:
    plgs : liste de quadruplets (hg, bg, bd, hd)"""
    (X, Y) = forme
    nforme = [(X[i], Y[i]) for i in range(len(X))]
    nforme = ajoute_points(nforme)
    forme = ([round(nforme[i][0],precision) for i in range(len(nforme))],
             [round(nforme[i][1],precision) for i in range(len(nforme))])
    lblasons = [] # liste des nouveaux blasons
    for p in plgs:
        # points du blason dans le rectangle
        nblason = is_in_square(forme, p)
        nblason = [(nblason["X"][i], nblason["Y"][i])
                   for i in range(len(nblason["X"]))]
        # sommets du rectangle dans le blason
        # Ajout des deux dans le bon ordre
        for sommet in p:
            if is_in_blason(sommet, nforme):
                if nblason == []:
                    nblason.append(sommet)
                else:
                    ind = position(sommet, nblason)
                    if ind > -1:
                        nblason[ind+1:ind+1] = [sommet]
        if nblason != []:
            lblasons.append(nblason)
    return lblasons

def ajoute_points(forme):
    N = 150
    dmin = 1
    n = len(forme)
    nforme = []
    p1 = forme[0]
    for i in range(len(forme)):
        nforme.append(p1)
        p2 = forme[(i+1)%n]
        if p1[0] != p2[0] and distance(p1, p2) > dmin:
            droite = lambda x:(p2[1]-p1[1])/(p2[0]-p1[0])*(x-p1[0]) + p1[1]
            dx = (p2[0] - p1[0])/N
            for k in range(1,N):
                x = p1[0]+k*dx
                y = droite(x)
                nforme.append((round(x,precision), round(y,precision)))
        elif p1[0] == p2[0] and distance(p1, p2) > dmin:
            dy = (p2[1] - p1[1])/N
            for k in range(1,N):
                x = p1[0]
                y = p1[1] + k * dy
                nforme.append((round(x,precision),round(y,precision)))
        p1 = p2
    return nforme
