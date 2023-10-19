import menu_app

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
        menu_app.agregar_compra(compras, total_gastado)
    elif opt == '2':
        menu_app.mostrar_compras(compras)
    elif opt == '3':
        menu_app.mostrar_total(compras)
    elif opt == '4':
        break
    else:
        'Opción no válida'
