import utils

print("\nSistema de Compra de Libros")

for i in range(0, 5):
    numero_copias = int(input("Cuántas copias quiere comprar?: "))
    if numero_copias > 10:
        precio_libro = utils.precio_lista * 0.6
    else:
        precio_libro = utils.precio_lista
    precio_total_libros = numero_copias * precio_libro
    costo_envio = 3 + 0.75 * (numero_copias-1)
    costo_total = precio_total_libros + costo_envio
    print("\nEl costo total de tu compra de libros es:", costo_total)