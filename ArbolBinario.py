def nuevo_nodo(valor):
    return {"valor": valor, "izquierdo": None, "derecho": None}
def insertar(raiz, valor):
    if raiz is None:
        return nuevo_nodo(valor)
    if valor < raiz["valor"]:
        raiz["izquierdo"] = insertar(raiz["izquierdo"], valor)
    else:
        raiz["derecho"] = insertar(raiz["derecho"], valor)
    return raiz

def en_orden(raiz, resultado):
    if raiz is not None:
        en_orden(raiz["izquierdo"], resultado)
        resultado.append(raiz["valor"])
        en_orden(raiz["derecho"], resultado)

def pre_orden(raiz, resultado):
    if raiz is not None:
        resultado.append(raiz["valor"])
        pre_orden(raiz["izquierdo"], resultado)
        pre_orden(raiz["derecho"], resultado)

def post_orden(raiz, resultado):
    if raiz is not None:
        post_orden(raiz["izquierdo"], resultado)
        post_orden(raiz["derecho"], resultado)
        resultado.append(raiz["valor"])


raiz = None

print("Introduce los valores del árbol binario. Escribe 'f' para terminar.")
while True:
    entrada = input("Ingresa un número (o 'f'): ")
    if entrada.lower() == "f":
        break
    try:
        valor = int(entrada)
        raiz = insertar(raiz, valor)
    except ValueError:
        print("Por favor, ingresa un número válido.")

resultado_en_orden = []
en_orden(raiz, resultado_en_orden)

resultado_pre_orden = []
pre_orden(raiz, resultado_pre_orden)

resultado_post_orden = []
post_orden(raiz, resultado_post_orden)

print("Recorrido en orden:", resultado_en_orden)
print("Recorrido pre-orden:", resultado_pre_orden)
print("Recorrido pos-torden:", resultado_post_orden)