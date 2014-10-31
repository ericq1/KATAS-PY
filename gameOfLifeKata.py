fila = 0
columna = 0
celdafila = 0
celdacolumna = 0

def numincremento(tabla):
    global celdacolumna
    global celdafila
    global columna
    global fila
    incremento = 0
    if celdacolumna == 0:
        if celdafila == 0:
            if tabla[celdacolumna][celdafila+1] == "*":
                incremento += 1
            if tabla[celdacolumna+1][celdafila] == "*":
                incremento += 1
            if tabla[celdacolumna+1][celdafila+1] == "*":
                incremento += 1
        elif celdafila == (fila-1):
            if tabla[celdacolumna][celdafila-1] == "*":
                incremento += 1
            if tabla[celdacolumna-1][celdafila] == "*":
                incremento += 1
            if tabla[celdacolumna-1][celdafila-1] == "*":
                incremento += 1
        else:
            if tabla[celdacolumna][celdafila-1] == "*":
                incremento += 1
            if tabla[celdacolumna][celdafila+1] == "*":
                incremento += 1
            for fila2 in range(-1,2):
                if tabla[celdacolumna+1][celdafila+fila2] == "*":
                    incremento += 1
    elif celdacolumna == (columna-1):
        if celdafila == 0:
            if tabla[celdacolumna][celdafila+1] == "*":
                incremento += 1
            if tabla[celdacolumna-1][celdafila] == "*":
                incremento += 1
            if tabla[celdacolumna-1][celdafila+1] == "*":
                incremento += 1
        elif celdafila == (fila-1):
            if tabla[celdacolumna-1][celdafila] == "*":
                incremento += 1
            if tabla[celdacolumna-1][celdafila-1] == "*":
                incremento += 1
            if tabla[celdacolumna][celdafila-1] == "*":
                incremento += 1
        else:
            if tabla[celdacolumna][celdafila-1] == "*":
                incremento += 1
            if tabla[celdacolumna][celdafila+1] == "*":
                incremento += 1
            for fila3 in range(-1,2):
                if tabla[celdacolumna-1][celdafila+fila3] == "*":
                    incremento += 1
    else:
        if celdafila == 0:
            for fila4 in range(0,2):
                if tabla[celdacolumna-1][celdafila+fila4] == "*":
                    incremento += 1
            for fila5 in range(0,2):
                if tabla[celdacolumna+1][celdafila+fila5] == "*":
                    incremento += 1
            if tabla[celdacolumna][celdafila+1] == "*":
                incremento += 1                
        elif celdafila == (fila-1):
            for fila6 in range(-1,1):
                if tabla[celdacolumna-1][celdafila+fila6] == "*":
                    incremento += 1
            for fila7 in range(-1,1):
                if tabla[celdacolumna+1][celdafila+fila7] == "*":
                    incremento += 1
            if tabla[celdacolumna][celdafila-1] == "*":
                incremento += 1
        else:
            for fila8 in range(-1,2):
                if tabla[celdacolumna-1][celdafila+fila8] == "*":
                    incremento += 1
            for fila8 in range(-1,2):
                if tabla[celdacolumna+1][celdafila+fila8] == "*":
                    incremento += 1
            if tabla[celdacolumna][celdafila-1] == "*":
                incremento += 1
            if tabla[celdacolumna][celdafila+1] == "*":
                incremento += 1
    return incremento

def NextOfspring(u):
    global celdafila
    global celdacolumna
    global columna
    global fila
    u2 = GetUniverse(u)
    splt = u2.split("\n")
    del splt[-1]
    copy = u2.split("\n")
    del copy[-1]
    celdacolumna = -1
    for line in splt:
        celdafila = 0
        celdacolumna += 1
        copy[celdacolumna] = ""
        for celda in line:
            tot = numincremento(splt)
            if tot == 3 and celda == ".":
                copy[celdacolumna] += "*"
            elif (tot == 1 or tot == 0) and celda == "*":
                copy[celdacolumna] += "."
            elif (tot == 2 or tot == 3) and celda == "*":
                copy[celdacolumna] += "*"
            elif tot > 3 and celda == "*":
                copy[celdacolumna] += "."
            else:
                copy[celdacolumna] += "."
            celdafila += 1
    final = ""
    for item in copy:
        final += item
    return (str(columna)+str(fila)+final)
    
    raise NotImplementedError

def GetUniverse(u):
    global fila
    global columna
    if u[0:2].isdigit() == True:
        fila = int(u[1])
        columna = int(u[0])
    u2 = ""
    for fila2 in range(0,columna):
        u2 += u[(fila2*fila)+2:(fila2*fila)+2+fila] + "\n"
    u = u2
    return u
    
    raise NotImplementedError

if __name__ == '__main__':
    print("Captura un universo (Linea por linea segun el formato y vacio para terminar)")
    u = ""
    line = input()
    while(line != ""):
        u += line
        line = input()
    option = input("Teclee n para ver la siguiente generacion y s para deter la simulacion")
    while(option == "n"):
        u = NextOfspring(u)
        print(GetUniverse(u))
        option = input()
