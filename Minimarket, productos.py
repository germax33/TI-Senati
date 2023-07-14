# TI-Senatidef del producto: ")
            costo = None
            cantidad = Nonedef listar_productos(productos):
    print("Lista de productos:")
    print("Producto, Marca, Precio, Cantidad")
#escribir imprimir para el producto, marca, precio, cantidad
    for nombre, detalles in productos.items():
        print(f"{nombre} | {detalles['marca']} | {detalles['costo']} | {detalles['cantidad']}")

    print() #imprimir el costo y la cantidad del producto




def agregar_producto(productos):  #agregar el producto
    while True:  #cuando levanta la bandera
        nombre = input("Ingrese el nombre del producto: ")
        
        if nombre in productos:
            opcion = input("Este producto ya existe. ¿Desea añadir más cantidad? (SI/NO): ")
            if opcion.upper() == "SI":
                cantidad = None
                while not cantidad:
                    try:
                        cantidad = int(input("Ingrese la cantidad adicional del producto: "))
                    except ValueError:
                        print("Valor inválido. Ingrese un número entero válido.")
                productos[nombre]["cantidad"] += cantidad
                print("Se ha añadido más cantidad al producto existente.")
            else:
                print("No se ha añadido más cantidad al producto existente.")
        else:
            marca = input("Ingrese la marc

            while not costo:
                try:
                    costo = float(input("Ingrese el costo del producto: "))
                except ValueError:
                    print("Valor inválido. Ingrese un número válido.")

            while not cantidad:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                except ValueError:
                    print("Valor inválido. Ingrese un número entero válido.")

            productos[nombre] = {"marca": marca, "costo": costo, "cantidad": cantidad}
            print("Producto agregado correctamente.")

        desea_continuar = input("¿Desea ingresar más productos? (SI/NO): ")
        if desea_continuar.upper() != "SI":
            break

    print("Productos agregados correctamente.")





def hacer_venta(productos):
    while True:
        nombre = input("Ingrese el nombre del producto a vender: ")

        if nombre in productos:
            cantidad_disponible = productos[nombre]["cantidad"]
            if cantidad_disponible > 0:
                cantidad_venta = None
                while not cantidad_venta:
                    try:
                        cantidad_venta = int(input("Ingrese la cantidad a vender: "))
                        if cantidad_venta < 1 or cantidad_venta > cantidad_disponible:
                            raise ValueError
                    except ValueError:
                        print("Cantidad inválida. Ingrese un número válido entre 5 y", cantidad_disponible)
                        cantidad_venta = None

                productos[nombre]["cantidad"] -= cantidad_venta
                print("Venta realizada correctamente.")
                break  # Se sale del bucle si la venta se realizó correctamente
            else:
                print("No hay suficiente cantidad del producto.")
        else:
            print("El producto no existe en el inventario. Intente nuevamente.")



def menu():
    lista_productos = {}

    while True:
        print("Supermercado")
        print("Elija la opción:")
        print("1. Listar los productos")
        print("2. Agregar más productos")
        print("3. Hacer una venta")
        print("4. Salir")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            listar_productos(lista_productos)
        elif opcion == "2":
            agregar_producto(lista_productos)
        elif opcion == "3":
            hacer_venta(lista_productos)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

        print()

menu())
