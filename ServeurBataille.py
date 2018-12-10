import socket
import sys

winner = 0
tab = []
morp = ""
grille = ""
for i in range (10) :
    tab.append(['~'] * 10)

#Affichage graphique
def affichage():
    for i in range (10) :
        morp = str(i) +" | "
        for j in range (10) :
            morp += tab[i][j]
            morp += " | "
        print(morp)

def grille():
    grille = "    "
    for i in range(10):
        grille += str(i) + "   "
    print(grille)
def jouer(sens,c,l,j):
    if j == 0:
        if sens == "h" :
            for i in range (4) :
                tab[l][c] = 'X'
                l-=1      
        elif sens == "g" :
            for i in range (4) :
                tab[l][c] = 'X'
                c-=1
        elif sens == "d" :
            for i in range (4) :
                tab[l][c] = 'X'
                c+=1
        elif sens == "b" :
            for i in range (4) :
                tab[l][c] = 'X'
                l+=1
    elif j == 1:
        if sens == "h" :
            for i in range (4) :
                tab[l][c] = 'O'
                l-=1      
        elif sens == "g" :
            for i in range (4) :
                tab[l][c] = 'O'
                c-=1
        elif sens == "d" :
            for i in range (4) :
                tab[l][c] = 'O'
                c+=1
        elif sens == "b" :
            for i in range (4) :
                tab[l][c] = 'O'
                l+=1

def stop():
    if KeyboardInterrupt:
        sys.exit(0)

UDP_IP = "10.160.108.4"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("Client connecté, commencement de la partie")
    for j in range(2) :
        grille()
        affichage()
        print("Entrer le sens du bateau pour le joueur ", j+1)
        sens = str(input())
        print("Entrer les coordonées du bateau pour le joueur ", j+1)
        a = float(input())
        c, l = str(a).split(".")
        c = int(c)
        l = int(l)
        jouer(sens, c, l, j)
    while (1) :
        affichage()
        tirer()
        diagonale()
        horizontale()
        verticale()