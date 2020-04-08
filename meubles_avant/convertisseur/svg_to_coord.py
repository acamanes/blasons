fichier = "vair.svg"

with open(fichier,"r") as f:
    s = f.read()
    l = s.split("id=")
    numeros = []
    for i in range(len(l)):
        if l[i][1] in ["l","f"]:
            try:
                int(l[i][2])
                numeros.append((l[i].split("\""))[1])
            except:
                pass
    print(numeros)

with open("test.html","w") as g:
    with open("file_to_open.txt","r") as f1:
        s = f1.read()
    g.write(s)

    with open(fichier, "r") as f2:
        s = f2.read()
    g.write(s)

    with open("js.txt","r") as f3:
        s = f3.read()
        s = s.replace("chemins_toto",str(numeros))
    g.write(s)
