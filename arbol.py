# Este archivo nos ayudara a administrar el arbol genealogico.

class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.cose = None
        self.set_hijos(hijos)

    # Asigna al nodo la lista de hijos que son pasados como parametro
    def set_hijos(self,hijos):
        self.hijos = hijos
        if self.hijos != None:
            for i in self.hijos:
                i.padre = self

    # Retorna una lista con los hijos del nodo
    def get_hijos(self):
        return self.hijos

    # Retorna el nodo padre
    def get_padre(self):
        return self.padre

    # Asignar el nodo padre de este nodo
    def set_padre(self, padre):
        self.padre = padre

    # Asignar un dato al nodo
    def set_datos(self,datos):
        self.datos = datos

    # Asignar coste
    def set_coste(self, coste):
        self.coste = coste
    
    # Devuelve coste
    def get_coste(self):
        return self.coste

    # Devuelve el dato almacenado en el nodo
    def get_datos(self):
        return self.datos

    # Devuelve True si el dato contenido en el nodo es igual al nodo pasado como parametro
    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    # Devuelve True si el dato contenido en el nodo es igual a alguno de los nodos contenidos en la lista de nodos pasada como parámetro.
    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista

    def en_lista_no_object(self, lista):
        en_la_lista = False
        if self.get_datos() in lista:
            en_la_lista = True
        return en_la_lista

    def __str__(self):
        return str(self.get_datos())