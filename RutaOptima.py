from collections import deque   # Para usar una cola eficiente (doble extremo)

# Constantes para identificar espacios libres y obstáculos
libre = 0
bloque = 1

# ============================
# Crear un mapa vacío
# ============================
def crear_mapa(filas, columnas):
    return[[libre for _ in range(columnas)] for _ in range(filas)]

# ============================
# Mostrar el mapa en consola
# ============================
def mostrar_mapa(mapa, camino =[], inicio=None, fin=None,):
    for f in range(len(mapa)):
        for c in range(len(mapa[0])):
            if inicio == (f, c):
                print("I", end=" ")     # Punto de inicio
            elif fin == (f, c):      
                print("F", end=" ")     # Punto de fin
            elif (f, c) in camino:
                print("*", end=" ")     # Punto de fin
            elif mapa[f][c] == libre:
                print(".", end=" ")     # Espacio libre
            elif mapa[f][c] == bloque:
                print("x", end=" ")     # Obstáculo
        print()

# ============================
# Colocar obstáculos manualmente
# ============================
def colocar_obstaculos(mapa):
    cantidad = int(input("Ingrese la cantidad de obstaculos que quieres colocar"))
    for _ in range(cantidad):
        f = int(input( "Ingrese la fila"))
        c = int(input( "Ingrese la columna"))

        if 0 <= f < len(mapa) and 0 <= c < len(mapa[0]):
            mapa[f][c] = bloque
            mostrar_mapa(mapa)
        else:
            print("Coodenadas fuera del rango")

# ============================
# Pedir coordenadas al usuario (validar)
# ============================
def obtener_coodernadas(mapa):
    while True:
        f = int(input( "Ingrese la fila"))
        c = int(input( "Ingrese la columna"))
        
        # Validar si la posición está en rango y libre
        if 0 <= f < len(mapa) and 0 <= c < len(mapa[0]) and mapa[f][c] == libre:
            return (f, c)
        else:
            print("Coodenadas invalidas o en obstaculo")

# ============================
# Algoritmo BFS para buscar el camino más corto
# ============================
def bfs(mapa, inicio, fin):
    filas, columnas = len(mapa), len(mapa[0])

    # Matrices auxiliares para rastrear el recorrido
    anterior = [[None for _ in range(columnas)] for _ in range(filas)]
    visitado = [[None for _ in range(columnas)] for _ in range(filas)]

    # Movimientos posibles (arriba, abajo, izquierda, derecha)
    movimientos = [(-1,0), (1,0), (0,-1), (0,1)]

    # Inicializar la cola con el punto de inicio
    queue = deque()
    queue.appendleft(inicio)
    visitado[inicio[0]][inicio[1]] = True

    # Comenzar búsqueda BFS
    while queue:
        actual = queue.popleft()

        # Si llegamos al punto final, terminar búsqueda
        if actual == fin:
            break

        # Explorar posiciones adyacentes
        for dx, dy in movimientos:
            nx, ny = actual[0] + dx, actual[1] + dy

            # Validar si es una posición válida para moverse
            if 0 <= nx < filas and 0 <= ny < columnas:
                if not visitado[nx][ny] and mapa[nx][ny] == 0:
                    queue.append((nx, ny))
                    visitado[nx][ny] = True
                    anterior[nx][ny] = actual   # Guardar de dónde llegamos a esta posición

    # Reconstruir el camino desde 'anterior'
    return reconstruir_camino(anterior, inicio, fin)

# ============================
# Reconstruir el camino encontrado por BFS
# ============================
def reconstruir_camino(anterior, inicio, fin):
    camino = []
    actual = fin

    while actual!= inicio:
        camino.append(actual)
        actual = anterior[actual[0]][actual[1]]

        # Si llegamos a un punto sin anterior, no hay camino posible
        if actual is None:
            return []
        
    camino.append(inicio)   # Añadir el punto de inicio
    camino.reverse()        # Invertir la lista (está de fin a inicio)
    return camino

# ============================
# Programa principal
# ============================
def main():
    # Crear mapa
    filas = int(input("Ingrese la cantidad de filas"))
    columnas = int(input("Ingrese la cantidad de columnas"))

    mapa = crear_mapa(filas, columnas)
    mostrar_mapa(mapa)

    # Colocar obstáculos
    colocar_obstaculos(mapa)
    mostrar_mapa(mapa)
    
    # Elegir punto de inicio
    print("Elige el punto de inicio")
    inicio = obtener_coodernadas(mapa)

    # Elegir punto de fin
    print("Elige el punto de fin")
    fin = obtener_coodernadas(mapa)

    # Ejecutar búsqueda de camino
    camino = bfs(mapa, inicio, fin)

    # Mostrar resultado
    if not camino:
        print("No hay camino posible")
    else:
        #marcar_camino(mapa, camino)
        print("El camino mas corto es:")
        mostrar_mapa(mapa,camino, inicio, fin)


# ============================
# Iniciar el programa
# ============================ 
if __name__ == "__main__":
    main()

