import heapq

# Grafo del ejercicio 2
# Cada conexión es bidireccional: (nodo, coste)

grafo = {
    "A": {"N": 5, "G": 9},
    "B": {"S": 4, "N": 4, "C": 1, "D": 5, "I": 3},
    "C": {"S": 2, "B": 1, "D": 8, "F": 8, "E": 10, "P": 21},
    "D": {"B": 5, "O": 13, "T": 6, "E": 2, "C": 8},
    "E": {"D": 2, "T": 2, "F": 12, "P": 10, "L": 7},
    "F": {"I": 7, "C": 8, "E": 12},
    "G": {"A": 9},
    "H": {},
    "I": {"B": 3, "F": 7},
    "J": {"T": 9},
    "K": {},
    "L": {"E": 7},
    "M": {},
    "N": {"A": 5, "B": 4, "Q": 4},
    "O": {"Q": 7, "D": 13},
    "P": {"C": 21, "E": 10},
    "Q": {"N": 4, "O": 7},
    "R": {},
    "S": {"B": 4, "C": 2},
    "T": {"D": 6, "E": 2, "J": 9}
}


def dijkstra(grafo, origen):
    dist = {nodo: float("inf") for nodo in grafo}
    anterior = {nodo: None for nodo in grafo}

    dist[origen] = 0

    cola = [(0, origen)]

    while cola:
        distancia, nodo = heapq.heappop(cola)

        # Si ya tenemos una distancia mejor, ignoramos esta
        if distancia > dist[nodo]:
            continue

        for vecino, peso in grafo[nodo].items():
            nueva_distancia = distancia + peso

            if nueva_distancia < dist[vecino]:
                dist[vecino] = nueva_distancia
                anterior[vecino] = nodo

                heapq.heappush(
                    cola,
                    (nueva_distancia, vecino)
                )

    return dist, anterior

distancias, anteriores = dijkstra(grafo, "S")

for nodo, distancia in distancias.items():
    print(nodo, "->", distancia)

def obtener_ruta(anterior, origen, destino):
    ruta = []
    actual = destino

    while actual is not None:
        ruta.append(actual)

        if actual == origen:
            break

        actual = anterior[actual]

    ruta.reverse()

    return ruta


distancias, anteriores = dijkstra(grafo, "S")

for destino in ["B", "C", "F", "T", "D", "E"]:
    ruta = obtener_ruta(anteriores, "S", destino)

    print(
        f"S -> {destino}: "
        f"{ruta} = {distancias[destino]} minutos"
    )