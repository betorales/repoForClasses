def agregar_compra(lista_precio, valor):
    lista_precio.append(valor)
    print('Se ha agregado el producto correctamente')

def mostrar_compras(lista_precio):
    if len(lista_precio) == 0:
        print('No hay compras registradas')
    else:
        for item in lista_precio:
            print(item)
            print('=========')

def mostrar_total(lista_precio):
    total = sum(lista_precio)
    total_formatomoneda = "${:,.0f}".format(total).replace(',', '.')
    print('EL total gastado es ', total_formatomoneda)

def main():
    compras = []
    total_gastado = 0

    while True:
        print('1. Agregar compras')
        print('2. Mostrar compras')
        print('3. Mostrar total gastado')
        print('4. Salir')
        opt = input('Por favor, seleccione una opción: ')

        if opt == '1':
            valor = input('Ingrese el monto de la compra: ')
            valor = int(valor)
            total_gastado = valor
            agregar_compra(compras, total_gastado)
        elif opt == '2':
            mostrar_compras(compras)
        elif opt == '3':
            mostrar_total(compras)
        elif opt == '4':
            break
        else:
            'Opción no válida'
main()