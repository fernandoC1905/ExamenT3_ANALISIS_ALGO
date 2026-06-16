# ==========================================
# EXAMEN T3 - PROBLEMA 1
# BACKTRACKING LABERINTO CON VIDAS
# ==========================================

def imprimir(mat):
    for f in mat:
        print(f)
    print()


def validar(lab, f, c, res, vidas):

    if f < 0 or f >= len(lab):
        return False

    if c < 0 or c >= len(lab[0]):
        return False

    if lab[f][c] == 0:
        return False

    if res[f][c] == 1:
        return False

    vidasRestantes = vidas

    if lab[f][c] == -1:
        vidasRestantes -= 1

    elif lab[f][c] == -2:
        vidasRestantes -= 2

    if vidasRestantes <= 0:
        return False

    return True


def laberinto(lab, res, f, c, vidas):

    if f == 0 and c == 0:

        res[f][c] = 1

        print("Llego a la salida F")
        imprimir(res)

        return True

    if validar(lab, f, c, res, vidas):

        vidasActuales = vidas

        if lab[f][c] == -1:
            vidasActuales -= 1

        elif lab[f][c] == -2:
            vidasActuales -= 2

        res[f][c] = 1

        print("Posicion:", (f, c),
              " Valor:", lab[f][c],
              " Vidas:", vidasActuales)

        imprimir(res)

        if laberinto(lab, res, f + 1, c, vidasActuales):
            return True

        elif laberinto(lab, res, f, c + 1, vidasActuales):
            return True

        elif laberinto(lab, res, f - 1, c, vidasActuales):
            return True

        elif laberinto(lab, res, f, c - 1, vidasActuales):
            return True

        else:           
            res[f][c] = 0
            return False

    else:
        return False

lab = [
    ["F", 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    ["I", 1, -1, 1, 1, 1, 0, 1, 1]
]

res = [[0 for _ in range(9)] for _ in range(9)]

print("LABERINTO ORIGINAL")
imprimir(lab)

print("INICIO EN I (8,0)")
print("VIDAS INICIALES = 3")
print()

if laberinto(lab, res, 8, 0, 3):

    print("================================")
    print("SALIDA ENCONTRADA")
    print("================================")
    print("CAMINO FINAL:")

    imprimir(res)

else:

    print("================================")
    print("NO EXISTE CAMINO VALIDO")
    print("================================")