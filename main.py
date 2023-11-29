def cal() :
    l = []
    prompt = input("")
    print(prompt)
    l = prompt.split(" ")

    a = float(l[0])
    b = float(l[2])

    for i in l :
        if i == "+" :
            r = a + b
            print(a + b)
        elif i == "x" :
            r = a * b
            print(a * b)
        elif i == "-" :
            r = a - b
            print(a - b)
        elif i == "/" :
            if b == 0 :
                print("Erreur, on ne peut diviser par zero.")
            else :
                r = a / b
                print(a / b)
        elif i == "^" or i == "**" :
            r = a ** b
            print(a ** b)
    file = open("hist.txt", "a")
    file.write(str(r)+"\n")

def histo() :
    file = open("hist.txt", "r")
    for line in file :
        print(line)
    

while True :
    print("Menu Principal:\n 1. Calcul\n 2. Consulter l'historique\n 3. Quitter")
    try :
        u = int(input(""))
        if u < 1 or u > 3 :
            print("Choississez un chiffre entre 1 et  3 inclus.")
        if u == 1 : 
            r = cal()
        elif u == 2 :
            histo()
        elif u == 3 :
            print("Au revoir !")
            break
    except ValueError :
        print("Entrez un caractere numerique.")
        continue
