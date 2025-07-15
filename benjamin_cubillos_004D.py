productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca:str):
    stock_producto = 0
    for i in productos:
        if productos[i][0].lower() == marca.lower():
            for e in stock:
                if e == i:
                    stock_producto += int(stock[e][1])
                    break
    print(f"El stock es: {stock_producto}")
    

def busqueda_precio(p_min:int, p_max:int):
    notebooks = []
    while True:
        try:
            for i in stock:
                if p_min <= int(stock[i][0]) <= p_max:
                    notebooks.append(i)
            if notebooks == []:
                print("No hay notebooks en ese rango de precios.")
                break
            else:
                for i,e in enumerate(notebooks):
                    for j in productos:
                        if e == j:
                            notebooks[i] = productos[j][0] + "--" + e
                notebooks.sort()
                print(f"Los notebooks entre los precios consultas son: {notebooks}")
                break
        except ValueError as e:
            print(e)
            continue

def actualizar_precio(modelo:str, p:int):
    for i in stock:
        if i == modelo:
            stock[i][0] = p
            return True
    else:
        return False

def verificar_entero_positivo(entero):
    if entero <= 0:
        return False
    else:
        return True

def validar_max_min(min, max):
    if min > max:
        return False
    else: 
        return True

def menu():
    while True:
        try:
            print("*** Menú Principal ***")
            print("1. Stock marca.")
            print("2. Búsqueda por precio.")
            print("3. Actualizar precio.")
            print("4. Salir.")

            opcion = int(input("Ingresa una opción(1-4): "))

            if opcion == 1:
                marca = input("Ingrese marca a consultar: ").strip()
                stock_marca(marca)
                print("\n")
            elif opcion == 2:
                while True:
                    try:
                        p_min = int(input("Ingrese precio mínimo: "))
                        if not verificar_entero_positivo(p_min):
                            print("Debe ingresar un número positivo mayor a 0!\n")
                        else:
                            p_max = int(input("Ingrese precio máximo: "))
                            if not verificar_entero_positivo(p_max):
                                print("Debe ingresar un número positivo mayor a 0!\n")
                            else:
                                if not validar_max_min(p_min, p_max):
                                    print("Los precios ingresados están mal, asegurate de que el mínimo sea menor que el máximo.\n")
                                else:
                                    busqueda_precio(p_min, p_max)
                                    break
                    except ValueError:
                        print("Debe ingresar valores enteros!!\n")
                        continue
                print("\n")
            elif opcion == 3:
                while True:
                    try:
                        modelo = input("Ingrese modelo a actualizar: ").strip()
                        precio = int(input("Ingrese precio actualizado: "))
                        if not verificar_entero_positivo(precio):
                            print("Debe ingresar un número positivo mayor a 0!\n")
                        else:
                            actualizado = actualizar_precio(modelo, precio)
                            if actualizado:
                                print("Precio actualizado!!!\n\n\n")
                            else:
                                print("Ese modelo no existe!!\n")
                        reinicio = True
                        while True:
                            opcion2 = input("Desea actualizar otro precio(s/n): ").lower()
                            if opcion2 == "s" or opcion2 == "si":
                                break
                            elif opcion2 == "n" or opcion2 == "no":
                                reinicio = False
                                break
                            else:
                                print("Opción invalida, ingresa 's'/'si' o 'n'/'no' .\n")
                        if reinicio:
                            continue
                        else:
                            break
                    except ValueError:
                        print("Debe ingresar valores enteros!!")
                        continue
                print("\n")
            elif opcion == 4:
                print("Programa finalizado.")
                break
            else:
                print("Debe seleccionar una opción valida!!!\n")
        except ValueError:
            print("Debe seleccionar una opción valida!!!\n")
            continue

menu()

