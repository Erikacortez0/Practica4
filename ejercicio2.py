productos = {
    "Galletas": 2.0,
    "Chorizo": 35,
    "Tomates": 7,
    "Pollo": 11,
    "Consome": 0.65
}

nombre_producto = input("Ingresa el nombre del un producto: ")

if nombre_producto in productos:
    cantidad_producto = int(input("Ingrese la cantidad de compra: "))
    precio = productos[nombre_producto]
    total = precio * nombre_producto
    print(f"El total a pagar por {cantidad_producto} {nombre_producto} es: ${total:.2f}")
else:
    print(f"El producto {nombre_producto} no se encuentra disponible en la tienda.")