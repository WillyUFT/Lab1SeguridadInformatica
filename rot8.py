abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def rotpositivo():
    contador=0
    while(True):
        if contador == len(contraseña):
            break
        elif contraseña[contador] in abc:
            for b in range(len(abc)):
                if abc[b] == contraseña[contador]:
                    if b + valorrot > 26:
                        contraseña1.append(abc[b+valorrot-27])
                    else:
                        contraseña1.append(abc[b+valorrot])
        else:
            contraseña1.append(contraseña[contador])
        contador=contador+1

def rotnegativo():
    contador=0
    while(True):
        if contador == len(contraseña):
            break
        elif contraseña[contador] in abc:
            for b in range(len(abc)):
                if abc[b] == contraseña[contador]:
                    if b - valorrot < 0:
                        contraseña1.append(abc[b-valorrot+27])
                    else:
                        contraseña1.append(abc[b-valorrot])
        else:
            contraseña1.append(contraseña[contador])
        contador=contador+1

#contraseña1=['H','O','L','A',' ','M','U','N','D','O']
#passwordvigenere1=['P','Y','T','H','O','N']



def vigenere():
    contador = 0
    while(True):
        if contador == len(contraseña1):
            break
        elif contraseña1[contador] in abc:
            for d in range(len(abc)):
                if abc[d] == contraseña1[contador]:
                    lencontraseña1.append(d)
        else:
            lencontraseña1.append(contraseña1[contador])
        contador=contador+1

    contador = 0
    while(True):
        if contador == len(passwordvigenere1):
            break
        elif passwordvigenere1[contador] in abc:
            for e in range(len(abc)):
                if abc[e] == passwordvigenere1[contador]:
                    lenpasswordvigenere1.append(e)
        else:
            lenpasswordvigenere1.append(passwordvigenere1[contador])
        contador=contador+1

    contador = 0
    contador1 = 0
    while(True):
        if contador == len(lencontraseña1):
            break
        elif type(lencontraseña1[contador]) == int:
            if lencontraseña1[contador] + lenpasswordvigenere1[contador1] > 26:
                contraseña2.append(abc[lencontraseña1[contador] + lenpasswordvigenere1[contador1] - 27])
                contador=contador+1
                contador1=contador1+1
                if contador1 == len(passwordvigenere1):
                    contador1=contador1-6
            else:
                contraseña2.append(abc[lencontraseña1[contador] + lenpasswordvigenere1[contador1]])
                contador=contador+1
                contador1=contador1+1
                if contador1 == len(passwordvigenere1):
                    contador1=contador1-6
        else:
            contraseña2.append(contraseña1[contador])
            contador=contador+1

#Main
Main=True
while(Main):
    lencontraseña1=[]
    lenpasswordvigenere1=[]
    contraseña2=[]
    print("Ingrese un número según la opción requerida")
    print("1 = Desafio 1")
    print("2 = Desafio 2")
    print("Otro número o letra = Salir del programa")
    opcion=input()
    if opcion == "1":
        print()
        print("Desafio 1")
        password=input('Ingrese una contraseña: ')
        password=password.upper()
        contraseña=[]
        contraseña1=[]
        for a in range(len(password)):
            contraseña.append(password[a])

        #Rot8
        valorrot=8
        rotpositivo()

        #Vigenere
        passwordvigenere='heropassword'
        passwordvigenere=passwordvigenere.upper()
        passwordvigenere1=[]
        for c in range(len(passwordvigenere)):
            passwordvigenere1.append(passwordvigenere[c])
            
        vigenere()
        
        #Rot12
        contraseña=contraseña2
        contraseña1=[]
        
        valorrot=12
        rotpositivo()

        print("El mensaje cifrado es:", ''.join(contraseña1))
        print()
        
    elif opcion == "2":
        print()
        print("Desafio 2")
        password=input('Ingrese una contraseña: ')
        #password=""
        password=password.upper()
        contraseña=[]
        contraseña1=[]
        for a in range(len(password)):
            contraseña.append(password[a])
        #Rot-12
        valorrot=12
        rotnegativo()
        
        #Vigenere
        passwordvigenere='finispasswd'
        passwordvigenere=passwordvigenere.upper()
        passwordvigenere1=[]
        for c in range(len(passwordvigenere)):
            passwordvigenere1.append(passwordvigenere[c])

        vigenere()

        
        #Rot-8
        contraseña=contraseña2
        contraseña1=[]
        
        valorrot=8
        rotnegativo()

        print("El mensaje descifrado es:", ''.join(contraseña1))
        print()
    else:
        Main=False
