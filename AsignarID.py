import json
def cargar_lista_estudiantes():
    try:
        with open('Campers.json', 'r') as file:
            lista_estudiantes = json.load(file)
    except FileNotFoundError:
        print("Error")
    return lista_estudiantes

def guardar_lista_estudiantes(lista_estudiantes):
    with open('Campers.json', 'w') as file:
        file.write(json.dumps(lista_estudiantes, indent=4))

lista = cargar_lista_estudiantes()
for i, camper in enumerate(lista, start=1):
    camper['ID'] = i

guardar_lista_estudiantes(lista)

