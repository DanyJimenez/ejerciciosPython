'''
1. Digitar 1 para recibir nombre de un producto (+0.4)
2. Digitar 2 para mostrar todos los productos registrados (+0.4)
3. Digitar 3 para permitir agregar un nuevo producto a la lista de
productos (+0.4)
4. Digitar 4 para permitir eliminar el ultimo producto de la lista
(+0.4)
5. Digitar 0 para SALIR
'''
productos = []
opcion = 100
print("Digite alguna de las siguientes opciones:")
print("1. para recibir nombre de un producto ")
print("2. para mostrar todos los productos registrados ")
print("3. para permitir agregar un nuevo producto a la lista de productos ")
print("4. para permitir eliminar el ultimo producto de la lista ")
print("0. Salir")

productos = []

while opcion !=0:
    opcion = int(input("Digite su opción: "))
    if opcion == 1 or opcion == 3:
        producto = input("Digite el producto que desea registrar: ")
        productos.append(producto)
    elif opcion == 2:
        print("PEDIDO:")
        for producto in productos:   
            print(f"Producto: {producto}")
    elif opcion == 4:
        if len(productos) > 1: #No permite que  la lista quede vacía
            productos.pop()
    elif opcion == 0:
        break
    else:
        print("Estimado usuario, digite una opción válida.")