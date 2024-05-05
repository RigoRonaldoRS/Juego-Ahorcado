import random

palabras = ["pyhton", "programacion", "talentotech"]
secreta = random.choice(palabras)
cadena = "-" * len(secreta)
print("Bienvenidos al juego del ahorcado")
intentos = 0



while True:
    print(cadena)
    letra = input("Ingresa una letra: ")
    if letra in secreta:
        for i in range(len(secreta)):
            if secreta[i] == letra:
                cadena = cadena[:i] + letra + cadena[i+1:]
    else:
        intentos += 1
        if intentos == 1:
            print("O")
        elif intentos == 2:
            print(" 0")
            print("/")

        elif intentos == 3:
            print(" 0")
            print("/|")
        elif intentos == 4:
            print(" 0")
            print("/|\\")
        elif intentos == 5:
            print(" 0")
            print("/|\\")
            print("/")
        elif intentos == 6:
            print(" 0")
            print("/|\\")
            print("/ \\")
            print(f"Has perdido el jueg, la palabra secreta era {secreta}")
            break

if cadena == secreta:
    print(f"Felicidades has ganado el juego, la palabra secreta era {secreta}")
    

     
        

    
    





