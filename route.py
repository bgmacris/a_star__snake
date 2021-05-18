from arbol import Nodo
import sys


def algoritmo(conexiones, snake_list, estado_inicial, solucion, pop=0, ignore=None,):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)
    resultado = []
    while (not solucionado) and len(nodos_frontera) != 0:
        nodos_frontera = sorted(nodos_frontera, reverse=False, key=comparar)
        nodo = nodos_frontera.pop(pop)
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            solucionado = True
            while nodo.get_padre() != None:
                resultado.append(nodo.get_datos())
                nodo = nodo.get_padre()
            return resultado[::-1]
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                # coste = calcular_coste(nodo_inicial, hijo, solucion)
                hijo.set_coste(nodo.get_coste() + 10)
                lista_hijos.append(hijo)
                if not hijo.en_lista_no_object(snake_list) or hijo.get_datos() == ignore:
                    if not hijo.en_lista(nodos_visitados):
                        if dato_nodo == nodo_inicial and hijo.get_datos() == solucion and solucion == snake_list[-1]:
                            pass
                        elif hijo.en_lista(nodos_frontera):
                            for n in nodos_frontera:
                                if n.igual(hijo) and n.get_coste() < hijo.get_coste():
                                    nodos_frontera.remove(n)
                                    nodos_frontera.append(hijo)
                        else:
                            nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)
        


def comparar(x):
    return x.get_coste()


################################################################################################
def dijkstra(grafo, nodo_inicial, snake_list, mayor, ignore):
    etiquetas = {}
    visitados = []
    pendientes = [nodo_inicial]
    nodo_actual = nodo_inicial

    # Nodo inicial
    etiquetas[nodo_actual] = [0, '']

    # Seleccionar el siguiente nodo de menor peso acumulado
    while len(pendientes) > 0:
        nodo_actual = nodo_menor_peso(etiquetas, visitados, mayor)
        visitados.append(nodo_actual)

        # Obtener conexiones
        for conexion, peso in grafo[nodo_actual].items():
            # print("conexion ->", conexion, "ignore ->", ignore)
            if conexion not in snake_list or conexion == ignore:
                if conexion not in pendientes and conexion not in visitados:
                    pendientes.append(conexion)
                nuevo_peso = etiquetas[nodo_actual][0] + peso

                # Etiquetar
                if conexion not in visitados:
                    if conexion not in etiquetas:
                        etiquetas[conexion] = [nuevo_peso, nodo_actual]
                    else:
                        if mayor:
                            if etiquetas[conexion][0] < nuevo_peso:
                                etiquetas[conexion] = [nuevo_peso, nodo_actual]
                        else:
                            if etiquetas[conexion][0] > nuevo_peso:
                                etiquetas[conexion] = [nuevo_peso, nodo_actual]
            else:
                pass

        pendientes.remove(nodo_actual)
    return etiquetas


def nodo_menor_peso(etiquetas, visitados, mayor):
    # menor = sys.maxsize   # max
    if mayor:
        valor = -sys.maxsize - 1    # min
        for nodo, etiqueta in etiquetas.items():
            if etiqueta[0] > valor and nodo not in visitados:
                valor = etiqueta[0]
                nodo_menor = nodo
        return nodo_menor
    else:
        valor = sys.maxsize
        for nodo, etiqueta in etiquetas.items():
            if etiqueta[0] < valor and nodo not in visitados:
                valor = etiqueta[0]
                nodo_menor = nodo
        return nodo_menor


def ruta(map, nodo_inicial, solucion, snake_list, mayor=0, ignore=None):
    etiquetas = dijkstra(map, nodo_inicial, snake_list, mayor, ignore)

    resultado = []
    nodo_visitar = solucion
    # Si no se encuentra la etiqueta, buscar el punto mas lejano y accesible.
    nodo = etiquetas[nodo_visitar]
    while nodo[0] != 0:

        resultado.append(nodo_visitar)
        nodo_visitar = nodo[1]
        nodo = etiquetas[nodo[1]]

    return resultado[::-1]
