def GetTablero():
    global interpretevalor1
    template = (" "+str(interpretevalor1[0])+" │ "+str(interpretevalor1[1])+" │ "+str(interpretevalor1[2])+" \n───┼───┼───\n "+str(interpretevalor1[3])+" │ "+str(interpretevalor1[4])+" │ "+str(interpretevalor1[5])+" \n───┼───┼───\n "+str(interpretevalor1[6])+" │ "+str(interpretevalor1[7])+" │ "+str(interpretevalor1[8])+" ")
    return template

def JuegoContinua():
    global mensageg1
    if mensageg1==("Felicidades X as ganado. weeee"):
        return False
    elif mensageg1==("Felicidades O as ganado. weeee"):
        return False
    elif mensageg1==("Juego empatado. :("):
        return False
    else:
        return True

def IntentarTirada(casilla):
    global numero1,interpretevalor1
    if casilla>9 or casilla<1:
        return('La tirada debe de estar entre 1 y 9')
    elif interpretevalor1[casilla-1]=='X' or interpretevalor1[casilla-1]=='O':
        return ('La casilla ya esta ocupada')
    else:
        if numero1%2==0:
            interpretevalor1[casilla-1]='X'
        else:
            interpretevalor1[casilla-1]='O'
        numero1+=1
        if interpretevalor1[0]=='X' and interpretevalor1[1]=='X' and interpretevalor1[2]=='X':
            return ("Felicidades X as ganado. weeee")
        elif interpretevalor1[3]=='X' and interpretevalor1[4]=='X' and interpretevalor1[5]=='X':
            return ("Felicidades X as ganado. weeee")
        elif interpretevalor1[6]=='X' and interpretevalor1[7]=='X' and interpretevalor1[8]=='X':
            return ("Felicidades X as ganado. weeee")
        elif interpretevalor1[0]=='X' and interpretevalor1[3]=='X' and interpretevalor1[6]=='X':
            return ("Felicidades X as ganado. weeee")
        elif interpretevalor1[1]=='X' and interpretevalor1[4]=='X' and interpretevalor1[7]=='X':
            return ("Felicidades X as ganado. weeee")
        elif interpretevalor1[2]=='X' and interpretevalor1[5]=='X' and interpretevalor1[8]=='X':
            return ("Felicidades X as ganado. weeee")
        elif interpretevalor1[0]=='X' and interpretevalor1[4]=='X' and interpretevalor1[8]=='X':
            return ("Felicidades X as ganado. weeee")
        elif interpretevalor1[2]=='X' and interpretevalor1[4]=='X' and interpretevalor1[6]=='X':
            return ("Felicidades X as ganado. weeee")
        elif interpretevalor1[0]=='O' and interpretevalor1[1]=='O' and interpretevalor1[2]=='O':
            return ("Felicidades O as ganado. weeee")
        elif interpretevalor1[3]=='O' and interpretevalor1[4]=='O' and interpretevalor1[5]=='O':
            return ("Felicidades O as ganado. weeee")
        elif interpretevalor1[6]=='O' and interpretevalor1[7]=='O' and interpretevalor1[8]=='O':
            return ("Felicidades O as ganado. weeee")
        elif interpretevalor1[0]=='O' and interpretevalor1[3]=='O' and interpretevalor1[6]=='O':
            return ("Felicidades O as ganado. weeee")
        elif interpretevalor1[1]=='O' and interpretevalor1[4]=='O' and interpretevalor1[7]=='O':
            return ("Felicidades O as ganado. weeee")
        elif interpretevalor1[2]=='O' and interpretevalor1[5]=='O' and interpretevalor1[8]=='O':
            return ("Felicidades O as ganado. weeee")
        elif interpretevalor1[0]=='O' and interpretevalor1[4]=='O' and interpretevalor1[8]=='O':
            return ("Felicidades O as ganado. weeee")
        elif interpretevalor1[2]=='O' and interpretevalor1[4]=='O' and interpretevalor1[6]=='O':
            return ("Felicidades O as ganado. weeee")
        elif interpretevalor1[0]!=1 and interpretevalor1[1]!=2 and interpretevalor1[2]!=3 and interpretevalor1[3]!=4 and interpretevalor1[4]!=5 and interpretevalor1[5]!=6 and interpretevalor1[6]!=7 and interpretevalor1[7]!=8 and interpretevalor1[8]!=9:
            return ("Juego empatado. :(")
        else:
            return ("")
    
def IniciaJuego():
    global numero1,casilla,interpretevalor1,mensageg1
    numero1=0
    casilla=0
    mensageg1 = ""
    interpretevalor1=[1,2,3,4,5,6,7,8,9]
    return numero1, casilla, mensageg1, interpretevalor1

if __name__ == '__main__':
    global casilla,mensageg1
    IniciaJuego() 
    while(JuegoContinua()):
        print(GetTablero())
        casilla = int(input("Escoge una casilla: "))
        mensageg1 = IntentarTirada(casilla)
        if mensageg1 != "":
            print(mensageg1)
