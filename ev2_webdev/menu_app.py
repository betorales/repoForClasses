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