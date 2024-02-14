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

def visualizarNotasModulos(lista):
    # Crear la lista para contener la tabla acumulativa
    tabla_acumulativa = []

    for camper in lista:
        # Extraer los valores del diccionario
        nombre = camper["name"]
        notas_modulo = camper["Modulo 1"]
        notas_teorica = notas_modulo["Nota Teorica"]
        notas_practica = notas_modulo["Nota Practica"]
        actividades = notas_modulo["Actividades"]
        final = notas_modulo["Final"]

        # Agregar una fila a la tabla acumulativa para este estudiante
        tabla_acumulativa.append([nombre, notas_teorica, notas_practica, actividades, final])

    # Imprimir la tabla acumulativa
    print(tabulate(tabla_acumulativa, headers=["Nombre", "Nota Teorica", "Nota Practica", "Actividades", "Final"]))