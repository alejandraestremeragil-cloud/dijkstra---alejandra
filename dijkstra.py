import heapq

# Grafo
grafo = {
    'S': {'A': 5, 'N': 4, 'C': 2},
    'A': {'S': 5, 'G': 9},
    'G': {'A': 9},

    'N': {'S': 4, 'B': 4},
    'B': {'N': 4, 'C': 1, 'I': 3, 'D': 5},

    'C': {'S': 2, 'B': 1, 'D': 8, 'E': 10, 'P': 21},

    'I': {'B': 3, 'F': 7},

    'F': {'I': 7, 'E': 12},

    'D': {'B': 5, 'C': 8, 'Q': 7, 'O': 13, 'E': 2, 'T': 6},

    'Q': {'D': 7},

    'O': {'D': 13},

    'E': {'D': 2, 'F': 12, 'T': 2, 'P': 7},

    'P': {'C': 21, 'E': 7},

    'T': {'D': 6, 'E': 2, 'J': 9},

    'J': {'T': 9}
}


def dijkstra(grafo, inicio, destino):
    cola = [(0, inicio, [])]
    visitados = set()

    while cola:
        coste, nodo, camino = heapq.heappop(cola)

        if nodo in visitados:
            continue

        camino = camino + [nodo]
        visitados.add(nodo)

        if nodo == destino:
            return coste, camino

        for vecino, peso in grafo[nodo].items():
            if vecino not in visitados:
                heapq.heappush(
                    cola,
                    (coste + peso, vecino, camino)
                )

    return float('inf'), []


# Pedido 1: recoger en F -> entregar en T
coste1a, ruta1a = dijkstra(grafo, 'S', 'F')
coste1b, ruta1b = dijkstra(grafo, 'F', 'T')

# Pedido 2: recoger en F -> entregar en E
coste2, ruta2 = dijkstra(grafo, 'F', 'E')

# Pedido 3: recoger en T -> entregar en D
coste3, ruta3 = dijkstra(grafo, 'T', 'D')

print("S -> F")
print(ruta1a, "Coste:", coste1a)

print("\nF -> E")
print(ruta2, "Coste:", coste2)

print("\nE -> T")
coste_et, ruta_et = dijkstra(grafo, 'E', 'T')
print(ruta_et, "Coste:", coste_et)

print("\nT -> D")
print(ruta3, "Coste:", coste3)

coste_total = coste1a + coste2 + coste_et + coste3

print("\nRuta final:")
print("S -> F -> E -> T -> D")
print("Coste total =", coste_total)