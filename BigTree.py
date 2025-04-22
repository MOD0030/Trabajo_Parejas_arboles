#Juan David Mejia Fragoso - 2240085
#Miguel Angel Aguilar Rodriguez - 2240030

from bigtree import Node, print_tree

jefe = Node("Jefe de la Empresa")

subjefe1 = Node("Subjefe pedro", parent=jefe)
subjefe2 = Node("Subjefe Juan", parent=jefe)
subjefe3 = Node("Subjefe Miguel", parent=jefe)

empleado1 = Node("Carlitos", parent=subjefe1)
empleado2 = Node("Andres", parent=subjefe1)

empleado3 = Node("Luchito", parent=subjefe2)
empleado4 = Node("Danielito", parent=subjefe2)

empleado5 = Node("Pepito", parent=subjefe3)
empleado6 = Node("Fulanito", parent=subjefe3)

print_tree(jefe)
