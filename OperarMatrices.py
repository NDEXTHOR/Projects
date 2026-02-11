import os

# Funciones para mostrar y eso...
def IngresarMatriz(T1, T2=None):
    # Ya funciona tambien para matrices que no son cuadradas, en C# en lugar de None se usa NULL, pero es basicamente lo mismo
    if T2 == None:
        matriz = [[0 for _ in range(T1)] for _ in range(T1)]# Se debe incializar, ¿Por que?... no se jajajajajaja
        for i in range(T1):
            for j in range(T1):
                matriz[i][j] = int(input(f"Ingrese la matriz en ({i},{j}): "))
    else:
        matriz = [[0 for _ in range(T2)] for _ in range(T1)]# T1 filas, T2 columnas
        for i in range(T1):
            for j in range(T2):
                matriz[i][j] = int(input(f"Ingrese la matriz en ({i},{j}): "))
    return matriz
def MostrarMatriz(matriz):
    print("*   Matriz resultante   *")
    for m in matriz:
        print(*m)# El apuntador es para el formato (No se imprimen las , ni los [])

# Operaciones
def SumarMatriz(matriz):
    for i in range(T):
        for j in range(T):
            matrizRes[i][j] += matriz[i][j]
def RestarMatriz(matriz):
    for i in range(T):
        for j in range(T):
            matrizRes[i][j] -= matriz[i][j]
def MultiplicarMatriz(matriz, T1, T2):
    # La regla es que el numero de columnas de la primera sea igual al numero de filas de la segunda
    # T1 = filas de primera, T2 = columnas de segunda, T2P = columnas de primera = filas de segunda
    for i in range(T1):# Filas de la primera matriz
        for j in range(T2):# Columnas de la segunda matriz
            res = 0# Aqui se guarda el acumulado de las multiplicaciones de fila x columna
            for k in range(T2P):
                res += Pmatriz[i][k] * matriz[k][j]# Indices correctos
            matrizRes[i][j] = res

# Menu de operaciones
menu = '"     Operaciones con matrices     "\n\n' \
       '"  1) Sumar                        "\n' \
       '"  2) Restar                       "\n' \
       '"  3) Multiplicar                  "\n' \
       '"  0) Salir                        "\n' 
while True:
    print(menu)
    Op = int(input("Seleccione una opcion: "))

    if Op == 0:
        print("Saliendo...")
        break

    if Op == 1 or Op == 2:# Sumar y restar (Solo se hace una, obviamente, esto es para ahorrar un poco de codigo)
        # Validacion de N
        N = int(input("Ingrese el numero de matrices: "))
        while N < 2:
            N = int(input("Error: El numero debe ser al menos 2: "))# Validamos que no se ingresen menos de 2 matrices

        # Este if me lo dio copilot, en c++ se puede hacer algo parecido por eso se me ocurrio
        print("Suma de matrices..." if Op == 1 else "Resta de matrices...")
        T = int(input("Ingrese el tamaño: "))

        matrizRes = [[0 for _ in range(T)] for _ in range(T)]# La inicializamos vacia

        # Sumamos o restamos con forme van entrando las matrices para no tener que guardarlas en alguna lista o algo asi
        for i in range(N):
            print(f"Ingrese la matriz No. {i+1}: ")
            matriz = IngresarMatriz(T)

            if i == 0:
                # La primera matriz siempre se suma (para que la resta sea matriz1 - matriz2 - ...)
                # Si no se hace esto la primer matriz con la que se opera es una matriz en 0s, entonces es como si la contemplara en la resta
                SumarMatriz(matriz)
            else:
                # Las demás se suman o restan según la operación
                SumarMatriz(matriz) if Op == 1 else RestarMatriz(matriz)

    if Op == 3:# Multiplicacion
        print("Multiplicacion de matrices...")
        # Aqui no se pide numero de matrices, lo limitare a 2 y tañvez de la opcion de multiplicar otra matriz mas al resultado, chance jaja

        T1P = int(input("Ingrese el numero de filas de la primer matriz: "))
        T2P = int(input("Ingrese el numero de columnas de la primer matriz: "))

        T1S = int(input("Ingrese el numero de filas de la segunda matriz: "))
        T2S = int(input("Ingrese el numero de columnas de la segunda matriz: "))

        #Validacion para que si se puedan multiplicar
        if T2P == T1S:
            # Para el resultado vamos a usar la misma de las demas operaciones con un cambio ligero
            matrizRes = [[0 for _ in range(T2S)] for _ in range(T1P)]# T1P filas x T2S columnas

            print("Matriz donde se guardara el resultado: ")
            MostrarMatriz(matrizRes)

            # Ingresamos la primer matriz ya que vamos a ir operando sobre esa
            print("Ingrese la primer matriz: ")
            Pmatriz = IngresarMatriz(T1P, T2P)
            # Ahora la segunda
            print("Ingrese la segunda matriz: ")
            matriz = IngresarMatriz(T1S, T2S)

            MultiplicarMatriz(matriz, T1P, T2S)
        else:
            print("Eror: La matrices no se pueden multiplicar...")

    # Ya solo mostramos el resultado
    MostrarMatriz(matrizRes)
    print("\n")
    input("Presione enter para volver al menu... \n La terminal se limpiara...")# Es basicamente un "system("pause");"
    os.system('cls')# Limpia la terminal