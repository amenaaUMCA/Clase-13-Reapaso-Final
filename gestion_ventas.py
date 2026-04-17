from datetime import date


def ingresar_ventas():
    """Función para ingresar nuevas ventas y guardarls en un archivo CSV."""
    Ventas = []  # Lista para almacenar las ventas ingresadas
    IVA = 0.13  # Tasa de IVA del 13%
    fecha = ""
    cliente = ""
    while True:
        try:
            nombre_producto = input("Ingrese el nombre del producto: ").upper()
            cantidad = int(input("Ingrese la cantidad vendida: "))
            precio = float(input("Ingrese el precio unitario: "))
            if fecha == "" or cliente == "":
                fecha = date.strptime(
                    input("Ingrese la fecha de la venta (YYYY-MM-DD): "), "%Y-%m-%d"
                )
                cliente = input("Ingrese el nombre del cliente: ")

            # Validaciones de datos
            if cantidad <= 0:
                print("❌ La cantidad debe ser un número positivo.")
                continue
            if precio < 0:
                print("❌ El precio debe ser un número positivo.")
                continue
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingrese los datos correctamente.")
            continue

        # Crear un diccionario con los datos de la venta
        venta = {
            "Producto": nombre_producto,
            "Cantidad": cantidad,
            "Precio": precio,
            "Fecha": fecha,
            "Cliente": cliente,
        }
        Ventas.append(venta)
        continuar = input("¿Desea ingresar otra venta? (s/n): ").lower()
        if continuar != "s":
            print("Guardando ventas en ventas.csv...")

            print("\n-- Ticket de Venta --")
            print(f"Cliente: {Ventas[0]['Cliente']} | Fecha: {Ventas[0]['Fecha']} ")
            for venta in Ventas:
                # Imprime los detalles de cada venta ingresada en un sola linea con formato de ticket
                print("-" * 30)
                print(
                    f"Producto: {venta['Producto']} | Cantidad: {venta['Cantidad']} | Precio: ${venta['Precio']:.2f}"
                )
            subtotal = sum(
                v["Cantidad"] * v["Precio"] for v in Ventas
            )  # Calcula el subtotal sumando el precio total de cada venta (cantidad * precio)
            iva = (
                subtotal * IVA
            )  # Calcula el IVA multiplicando el subtotal por la tasa de IVA (13%)
            print("""Subtotal: ${:.2f}""".format(subtotal))
            print("""IVA (13%): ${:.2f}""".format(iva))
            print("Total a pagar: ${:.2f}".format(subtotal + iva))
            break


if __name__ == "__main__":
    ingresar_ventas()
