from tabulate import tabulate

def visualizar(listaCampers):
    datos_tabla = []
    for i, persona in enumerate(listaCampers, start=1):
        datos_tabla.append([i] + [persona[key] for key in persona])

    encabezado = ['#'] + list(listaCampers[0].keys())

    print(tabulate(datos_tabla, headers=encabezado))

