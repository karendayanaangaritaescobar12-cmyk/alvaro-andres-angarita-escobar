print("=================================================")
print(      "productos                       precio"     )
print(       "papas                           2.500"     )
print(       "gaseosa                         3.000"     )
print(       "galletas                        1.800"     )
print(       "chocolate                       2.200"     )
print(       "jugo                            2.800"     )
print("=================================================")

productos = ["papas", "gaseosa", "galletas", "chocolate", "jugo"]
precios = [2500, 3000, 1800, 2200, 2800]

carrito = []

def ver_productos():
    print("Productos:")
    for i in range(len(productos)):
        print(productos[i], precios[i])

def agregar():
    p = input("Producto: ")
    if p in productos:
        carrito.append(p)
        print("Agregado")
    else:
        print("No existe")

def ver_carrito():
    if len(carrito) == 0:
        print("Vacio")
    else:
        total = 0
        for c in carrito:
            i = productos.index(c)
            print(c, precios[i])
            total = total + precios[i]
        print("Total", total)

def pagar():
    if len(carrito) == 0:
        print("Nada que pagar")
        return False
    total = 0
    for c in carrito:
        i = productos.index(c)
        total = total + precios[i]
    print("Total", total)
    r = input("Pagar si/no: ")
    if r == "si":
        print("Gracias")
        return True
    else:
        print("Cancelado")
        return False

while True:
    print("1 ver")
    print("2 agregar")
    print("3 carrito")
    print("4 pagar")
    print("0 salir")
    op = input("op: ")

    if op == "1":
        ver_productos()
    elif op == "2":
        agregar()
    elif op == "3":
        ver_carrito()
    elif op == "4":
        if pagar():
            break
    elif op == "0":
        break
    else:
        print("error")