# Integrantes:
# - Juan David Mejia Fragoso - 
# - Miguel Angel Aguilar Rodriguez - 2240030

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self, valor_raiz):
        self.raiz = Nodo(valor_raiz)

    def buscar_nodo(self, nodo, valor):
        if nodo.valor == valor:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self.buscar_nodo(hijo, valor)
            if encontrado:
                return encontrado
        return None

    def agregar_nodo(self, valor_padre, valor_hijo):
        padre = self.buscar_nodo(self.raiz, valor_padre)
        if padre:
            padre.hijos.append(Nodo(valor_hijo))
        else:
            print(f"No se encontró el nodo con valor {valor_padre}.")

    def peso(self):
        return self._contar_nodos(self.raiz)

    # Cuenta los hijos de los nodos
    def _contar_nodos(self, nodo):
        total = 1  # contar el mismo nodo
        for hijo in nodo.hijos:
            total += self._contar_nodos(hijo)
        return total
    # Halla el orden del árbol - RECURSIVA
    def _orden(self, nodo):
        maximo = len(nodo.hijos)
        for hijo in nodo.hijos:
            maximo = max(maximo, self._orden(hijo))
        return maximo
    # Halla la altura de un nodo - RECURSIVA
    def _altura(self, nodo):
        if not nodo.hijos:
            return 1
        return 1 + max(self._altura(hijo) for hijo in nodo.hijos)



raiz = input("Valor de la raíz del árbol: ")
arbol = Arbol(raiz)

while True:
    opc = input("¿Agregar nodo? (s/n): ").lower()
    if opc != 's':
        break
    padre = input("Valor del nodo padre: ")
    hijo = input("Valor del nuevo nodo hijo: ")
    arbol.agregar_nodo(padre, hijo)

print("\n--- Resultados ---")
print("Peso del árbol:", arbol._altura(arbol.raiz))
print("Altura del árbol:", arbol._altura(arbol.raiz))
print("orden del arbol: ", arbol._orden(arbol.raiz))


