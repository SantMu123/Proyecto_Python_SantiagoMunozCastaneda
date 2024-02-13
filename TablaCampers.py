from tabulate import tabulate

def visualizar(listaCampers):
    datos_tabla = []
    for i, persona in enumerate(listaCampers, start=1):
        datos_tabla.append([i] + [persona[key] for key in persona])

    encabezado = ['#'] + list(listaCampers[0].keys())

    print(tabulate(datos_tabla, headers=encabezado))

def visualizarRutas(listaRutas):
    datos_rutas = []
    for i, ruta in enumerate(listaRutas, start=1):
        datos_rutas.append([i] + list(ruta))

    encabezado_rutas = ['#', 'Profesor', 'Ruta', 'Salon']
    
    print(tabulate(datos_rutas, headers=encabezado_rutas))
