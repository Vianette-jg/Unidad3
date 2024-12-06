class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijo_izquierdo = None
        self.hijo_derecho = None

def agregar_hijo(nodo, nombre_hijo):
    if nodo.hijo_izquierdo is None:
        nodo.hijo_izquierdo = Nodo(nombre_hijo)
        return "Hijo izquierdo agregado."
    elif nodo.hijo_derecho is None:
        nodo.hijo_derecho = Nodo(nombre_hijo)
        return "Hijo derecho agregado."
    else:
        return "Este nodo ya tiene dos hijos."

def mostrar_arbol(nodo, nivel=0):
    if nodo is not None:
        print("    " * nivel + "- " + nodo.nombre)
        mostrar_arbol(nodo.hijo_izquierdo, nivel + 1)
        mostrar_arbol(nodo.hijo_derecho, nivel + 1)

def buscar_nodo(nodo, nombre):
    if nodo is None:
        return None
    if nodo.nombre == nombre:
        return nodo
    izquierdo = buscar_nodo(nodo.hijo_izquierdo, nombre)
    if izquierdo:
        return izquierdo
    return buscar_nodo(nodo.hijo_derecho, nombre)

def modificar_nodo(nodo, nombre_actual, nuevo_nombre):
    nodo_a_modificar = buscar_nodo(nodo, nombre_actual)
    if nodo_a_modificar:
        nodo_a_modificar.nombre = nuevo_nombre
        return "Nodo modificado con éxito."
    else:
        return "Nodo no encontrado."

def eliminar_nodo(nodo, nombre):
    if nodo is None:
        return None, "Nodo no encontrado."

    if nodo.hijo_izquierdo and nodo.hijo_izquierdo.nombre == nombre:
        nodo.hijo_izquierdo = None
        return nodo, "Nodo izquierdo eliminado."
    if nodo.hijo_derecho and nodo.hijo_derecho.nombre == nombre:
        nodo.hijo_derecho = None
        return nodo, "Nodo derecho eliminado."

    nodo.hijo_izquierdo, mensaje_izq = eliminar_nodo(nodo.hijo_izquierdo, nombre)
    if mensaje_izq != "Nodo no encontrado.":
        return nodo, mensaje_izq

    nodo.hijo_derecho, mensaje_der = eliminar_nodo(nodo.hijo_derecho, nombre)
    return nodo, mensaje_der

def mostrar_hijos(nodo):
    if nodo is None or (nodo.hijo_izquierdo is None and nodo.hijo_derecho is None):
        return "El nodo no tiene hijos."
    
    hijos = []
    if nodo.hijo_izquierdo:
        hijos.append(nodo.hijo_izquierdo.nombre)
    if nodo.hijo_derecho:
        hijos.append(nodo.hijo_derecho.nombre)
    return "Hijos: " + ", ".join(hijos)

# Programa principal
raiz = None

while True:
    print("\nÁrbol Genealógico")
    print("1. Crear raíz")
    print("2. Agregar hijo")
    print("3. Mostrar árbol")
    print("4. Modificar nodo")
    print("5. Eliminar nodo")
    print("6. Buscar nodo y mostrar hijos")
    print("7. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        if raiz is None:
            nombre_raiz = input("Ingresa el nombre de la raíz (tatarabuelo/a): ")
            raiz = Nodo(nombre_raiz)
            print("Raíz creada con éxito.")
        else:
            print("La raíz ya ha sido creada y no se puede modificar.")
    
    elif opcion == "2":
        if raiz is None:
            print("Primero debes crear la raíz.")
        else:
            nombre_buscar = input("Ingresa el nombre del progenitor al que deseas agregar un hijo: ")
            progenitor = buscar_nodo(raiz, nombre_buscar)
            if progenitor:
                if progenitor.hijo_izquierdo is not None and progenitor.hijo_derecho is not None:
                    print("Este nodo ya tiene dos hijos. No puedes agregar más.")
                else:
                    nombre_hijo = input("Ingresa el nombre del hijo: ")
                    print(agregar_hijo(progenitor, nombre_hijo))
            else:
                print("Progenitor no encontrado.")
    
    elif opcion == "3":
        if raiz is None:
            print("El árbol está vacío.")
        else:
            mostrar_arbol(raiz)

    elif opcion == "4":
        if raiz is None:
            print("Primero debes crear la raíz.")
        else:
            nombre_actual = input("Ingresa el nombre del nodo que deseas modificar: ")
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            print(modificar_nodo(raiz, nombre_actual, nuevo_nombre))

    elif opcion == "5":
        if raiz is None:
            print("Primero debes crear la raíz.")
        else:
            nombre_eliminar = input("Ingresa el nombre del nodo que deseas eliminar: ")
            raiz, mensaje = eliminar_nodo(raiz, nombre_eliminar)
            print(mensaje)

    elif opcion == "6":
        if raiz is None:
            print("Primero debes crear la raíz.")
        else:
            nombre_buscar = input("Ingresa el nombre del nodo que deseas buscar: ")
            nodo_buscado = buscar_nodo(raiz, nombre_buscar)
            if nodo_buscado:
                print("Nodo encontrado.")
                print(mostrar_hijos(nodo_buscado))
            else:
                print("Nodo no encontrado.")
    
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Intenta de nuevo.")