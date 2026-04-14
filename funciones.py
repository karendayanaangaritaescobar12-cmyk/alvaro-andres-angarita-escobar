import csv
from datetime import datetime
from pathlib import Path

rutaBase = Path(__file__).parent
rutaArchivo = rutaBase/"DB"
iva=0.19
# crear archivos si no existen
open(rutaArchivo/"productos.csv", "a").close()
open(rutaArchivo/"clientes.csv", "a").close()
open(rutaArchivo/"mesas.csv", "a").close()
open(rutaArchivo/"facturas.csv", "a").close()

# ===== PRODUCTOS =====
def menu_productos():
    while True:
        print("\n--- PRODUCTOS ---")
        print("1. Agregar")
        print("2. Ver")
        print("3. Salir")

        op = input("Opcion: ")

        if op == "1":
            codigo = input("Codigo: ")
            nombre = input("Nombre: ")
            valor = input("Valor: ")
            


            file = open(rutaArchivo/"productos.csv", "a", newline="")
            writer = csv.writer(file)
            writer.writerow([codigo, nombre, valor, iva])
            file.close()

        elif op == "2":
            try:
                file = open(rutaArchivo/"productos.csv", "r")
                reader = csv.reader(file)
                for fila in reader:
                    print(fila)
                file.close()
            except:
                print("No hay datos")

        elif op == "3":
            break


# ===== MESAS =====
def menu_mesas():
    while True:
        print("\n--- MESAS ---")
        print("1. Agregar")
        print("2. Ver")
        print("3. Salir")

        op = input("Opcion: ")

        if op == "1":
            codigo = input("Codigo: ")
            nombre = input("Nombre: ")
            puestos = input("Puestos: ")

            file = open(rutaArchivo/"mesas.csv", "a", newline="")
            writer = csv.writer(file)
            writer.writerow([codigo, nombre, puestos])
            file.close()

        elif op == "2":
            try:
                file = open(rutaArchivo/"mesas.csv", "r")
                reader = csv.reader(file)
                for fila in reader:
                    print(fila)
                file.close()
            except:
                print("No hay datos")

        elif op == "3":
            break


# ===== CLIENTES =====
def menu_clientes():
    while True:
        print("\n--- CLIENTES ---")
        print("1. Agregar")
        print("2. Ver")
        print("3. Salir")

        op = input("Opcion: ")

        if op == "1":
            idc = input("ID: ")
            nombre = input("Nombre: ")
            tel = input("Telefono: ")
            email = input("Email: ")

            file = open(rutaArchivo/"clientes.csv", "a", newline="")
            writer = csv.writer(file)
            writer.writerow([idc, nombre, tel, email])
            file.close()

        elif op == "2":
            try:
                file = open(rutaArchivo/"clientes.csv", "r")
                reader = csv.reader(file)
                for fila in reader:
                    print(fila)
                file.close()
            except:
                print("No hay datos")

        elif op == "3":
            break


# ===== BUSCAR =====
def buscar(ruta, codigo):
    try:
        file = open(ruta, "r")
        reader = csv.reader(file)
        for fila in reader:
            if fila[0] == codigo:
                file.close()
                return fila
        file.close()
    except:
        return None


# ===== FACTURAR =====
def facturar():
    print("\n--- FACTURAR ---")

    mesa = buscar(rutaArchivo/"mesas.csv", input("Codigo mesa: "))
    if mesa is None:
        print("Mesa no existe")
        return

    cliente = buscar(rutaArchivo/"clientes.csv", input("ID cliente: "))
    if cliente is None:
        print("Cliente no existe")
        return

    total = 0
    fecha = datetime.now().strftime("%Y-%m-%d")

    while True:
        prod = buscar(rutaArchivo/"productos.csv", input("Codigo producto: "))
        if prod is None:
            print("No existe")
            continue

        cant = int(input("Cantidad: "))
        valor = float(prod[2])
        iva = float(prod[3])

        subtotal = (valor + valor * iva) * cant
        total += subtotal

        file = open(rutaArchivo/"facturas.csv", "a", newline="")
        writer = csv.writer(file)
        writer.writerow([fecha, mesa[0], cliente[0], prod[0], cant, subtotal])
        file.close()

        op = input("Otro producto? (s/n): ")
        if op != "s":
            break

    print("TOTAL:", total)


# ===== REPORTE =====
def reporte():
    fecha = input("Fecha (YYYY-MM-DD): ")
    total = 0

    try:
        file = open("facturas.csv", "r")
        reader = csv.reader(file)
        for fila in reader:
            if fila[0] == fecha:
                total += float(fila[5])
        file.close()

        print("Total vendido:", total)
    except:
        print("No hay datos")


# ===== MENU PRINCIPAL =====
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Productos")
        print("2. Mesas")
        print("3. Clientes")
        print("4. Facturar")
        print("5. Reporte")
        print("6. Salir")

        op = input("Opcion: ")

        if op == "1":
            menu_productos()
        elif op == "2":
            menu_mesas()
        elif op == "3":
            menu_clientes()
        elif op == "4":
            facturar()
        elif op == "5":
            reporte()
        elif op == "6":
            break


menu()
