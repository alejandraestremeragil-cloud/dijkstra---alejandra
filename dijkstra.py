import heapq


# =========================
# GRAFO
# =========================

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


# =========================
# DIJKSTRA
# =========================

def dijkstra(grafo, inicio, destino):

    cola = [(0, inicio, [inicio])]
    visitados = set()

    while cola:

        distancia, nodo, camino = heapq.heappop(cola)

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == destino:
            return distancia, camino

        for vecino, peso in grafo[nodo].items():

            if vecino not in visitados:

                heapq.heappush(
                    cola,
                    (
                        distancia + peso,
                        vecino,
                        camino + [vecino]
                    )
                )

    return float('inf'), []


# =========================
# PEDIDOS
# =========================

pedidos = [

    {
        "nombre": "Pedido 1",
        "productos": "Antitusivo + Chicles",
        "recogida": "F",
        "entrega": "T",
        "estado": "Pendiente"
    },

    {
        "nombre": "Pedido 2",
        "productos": "Supositorios + Vendas",
        "recogida": "F",
        "entrega": "E",
        "estado": "Pendiente"
    },

    {
        "nombre": "Pedido 3",
        "productos": "Antipsicóticos + Aspirinas",
        "recogida": "T",
        "entrega": "D",
        "estado": "Pendiente"
    }

]


# =========================
# RECORRIDO DEL EJERCICIO
# =========================

coste_total = 0

print("\n========== INICIO ==========")
print("Salimos desde S\n")


# -------------------------
# S -> F
# -------------------------

coste, ruta = dijkstra(grafo, "S", "F")
coste_total += coste

print("Ir a farmacia F")
print("Ruta:", " -> ".join(ruta))
print("Coste:", coste)

for pedido in pedidos:
    if pedido["recogida"] == "F":
        pedido["estado"] = "Recogido"
        print(f"\nRecogido {pedido['nombre']}")
        print("Productos:", pedido["productos"])
        print("Destino:", pedido["entrega"])

print("\nEstado pedidos:")
for p in pedidos:
    print(f"{p['nombre']} --> {p['estado']}")


# -------------------------
# F -> E
# -------------------------

coste, ruta = dijkstra(grafo, "F", "E")
coste_total += coste

print("\n============================")
print("Ir a cliente E")
print("Ruta:", " -> ".join(ruta))
print("Coste:", coste)

for pedido in pedidos:
    if pedido["entrega"] == "E" and pedido["estado"] == "Recogido":

        pedido["estado"] = "Entregado"

        print(f"\nEntregado {pedido['nombre']}")
        print("Productos:", pedido["productos"])

print("\nEstado pedidos:")
for p in pedidos:
    print(f"{p['nombre']} --> {p['estado']}")


# -------------------------
# E -> T
# -------------------------

coste, ruta = dijkstra(grafo, "E", "T")
coste_total += coste

print("\n============================")
print("Ir a T")
print("Ruta:", " -> ".join(ruta))
print("Coste:", coste)

for pedido in pedidos:

    if pedido["entrega"] == "T" and pedido["estado"] == "Recogido":

        pedido["estado"] = "Entregado"

        print(f"\nEntregado {pedido['nombre']}")
        print("Productos:", pedido["productos"])

for pedido in pedidos:

    if pedido["recogida"] == "T" and pedido["estado"] == "Pendiente":

        pedido["estado"] = "Recogido"

        print(f"\nRecogido {pedido['nombre']}")
        print("Productos:", pedido["productos"])
        print("Destino:", pedido["entrega"])

print("\nEstado pedidos:")
for p in pedidos:
    print(f"{p['nombre']} --> {p['estado']}")


# -------------------------
# T -> D
# -------------------------

coste, ruta = dijkstra(grafo, "T", "D")
coste_total += coste

print("\n============================")
print("Ir a cliente D")
print("Ruta:", " -> ".join(ruta))
print("Coste:", coste)

for pedido in pedidos:

    if pedido["entrega"] == "D" and pedido["estado"] == "Recogido":

        pedido["estado"] = "Entregado"

        print(f"\nEntregado {pedido['nombre']}")
        print("Productos:", pedido["productos"])

print("\n========== FINAL ==========")

for p in pedidos:
    print(f"{p['nombre']} --> {p['estado']}")

print("\nCoste total =", coste_total)