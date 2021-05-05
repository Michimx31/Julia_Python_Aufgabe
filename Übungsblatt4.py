# ----------------------------
# ------- Aufgabe 2 ----------
# ----------------------------
from random import randint

ready = False

# -------------------------
# ------ Zahleraten -------
# -------------------------
def zahlenraten(n,k):
    versuche = []
    counter = 0
    gesucht = int(randint(1,n))
    versuch = 0    

    while versuch != gesucht and counter <k:
        versuch = int(input('Raten Sie eine Zahl zwischen 1 und {}: '.format(n)))
        if not versuch>1:
           print('Bitte geben Sie eine natürliche Zahl größer oder gleich 1 ein. ')  
    
        if versuch == gesucht:
            print("The game is finished.")
            break

        if versuch < gesucht:
            print("Die Zahl ist zu klein")
        if versuch > gesucht:
            print("Die Zahl ist zu gross")

        counter = counter + 1
        versuche.append(versuch)

    return versuche , gesucht

while ready ==False:
    n = int(input('Geben Sie eine Maximalzahl für das Ratespiel ein: '))
    if not n>1:
       print('Bitte geben Sie eine natürliche Zahl größer oder gleich 1 ein. ')  
           
    k = int(input('Wie viele Versuche möchten Sie (>2) ? '))
    if not k>2:
        print('Bitte geben Sie mehr als 2 Versuche ein!') 
    else: 
        ready = True
        
versuche , gesucht = zahlenraten(n,k)

print("Sie haben folgende Zahlen geraten: ",versuche, "Die gesuchte Zahl war: ", gesucht)






























