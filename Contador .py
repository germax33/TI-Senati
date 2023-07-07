def pedir_nombres():
    nombres = []
    cantidad = int(input("ingrese la cantidad de nombres: "))

    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre {i+1}: ").capitalize()

        while nombre in nombres:
            print("El nombre ya ha sido ingresado. intente nuevamente.")
            nombre = input(f"ingrese el nombre {i+1}: ").capitalize()

        nombres.append(nombre)

    return nombres

def imprimir_resultados(nombres):
    print(f"Se ingresaron {len(nombres)} nombres.")
    print(f"Los nombres ingresados son: {nombres}")
    for nombre in nombres:
        num_vocales  = sum(1 for letra in nombre if letra.lower() in 'aeiouáéíóú')
        num_consonantes  = sum(1 for letra in nombre if not (letra.lower() in 'aeiouáéíóú'))
        r= f"""
            nombre: {nombre.capitalize()}
            numero de vocales: { num_vocales }
            numero de consonantes: {num_consonantes}
            numero de letras: {len(nombre)}
        """
        print(r)

lista_nombres = pedir_nombres()
imprimir_resultados(lista_nombres)


    # def pedir_nombres():
    #         nombres = []
    #         cantidad = int(input("Ingrese la cantidad de nombres: "))

    #         for i in range(cantidad):
    #             nombre = input(f"ingrese el nombre {i+1}: ").capitalize()

    #             while nombre in nombres:
    #                 print("El nombre ya ha sido ingresado. intente nuevamente.")
    #                 nombre = input(f"Ingrese el nombre {i+1}: ").capitalize()

    #             nombres.append(nombre)


            # resultados = []
            # for nombre in nombres:
            #     num_vocales  = sum(1 for letra in nombre if letra.lower() in 'aeiouáéíóú')
            #     num_consonantes = len(nombre) - num_vocales
            #     num_letras = len(nombre)
            #     resultados.append((nombre, num_vocales, num_consonantes,))
                
#   def procesador_nombres():
#          nombres=[] 
#          flag=True
#         while flag:
#     nombre = input("Ingrese un nombre o X para terminar):".capitalize())
#     if nombre == "x":
#      flag=False
#     nombre=nombre.lower()
               

