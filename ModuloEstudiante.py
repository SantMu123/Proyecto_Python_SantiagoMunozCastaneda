import menu
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

def agregar_estudiante(lista_estudiantes, info):
    lista_estudiantes.append(info)

def ModuloCamper():
    comando = "A"
    while comando != "E":
        comando = menu.MenuCamper()
        if comando == "A":
            
            try: 
                nombre = input("Digita tu nombre: ")
                apellido = input("Digita tu apellido: ")
                direccion = input("Digita tu direccion: ")
                asistente = input("Digita tu attendant: ")
                numeroCel = input("Digita tu numero CEL: ")
                numeroTel = input("Digita tu numero TEl: ")
                
                info = {
                "name": nombre,
                "Second name": apellido,
                "Adress": direccion,
                "attendant": asistente,
                "Number Contact #1": numeroCel,
                "Number Contact #2": numeroTel,
                "Status": "Inscrito",
                "Risk": "None",
                "Teoric Note": "None",
                "Practical Note": "None",
                "Average Note": "None"
                }

                campers = cargar_lista_estudiantes()
                bandera1 = True
                for camper in campers:
                    if camper['name'] == info['name'] and camper['Second name'] == info['Second name']:
                        print("Ya se encuentra registrado")
                        break
                    else:
                        bandera1 = False
                if not bandera1:
                    agregar_estudiante(campers, info)
                    guardar_lista_estudiantes(campers)
            except Exception as e:
                print("Registro Fallido, Vuleve a intentarlo!!!")
                print(e)
                comando = menu.MenuCamper()
        if comando == "B":
            comando2b = "A"
            while comando2b != "B":
                print("Entraste a la opción de Ver Notas!!!")
                nombre = input("Ingresa tu nombre: ")
                apellido = input("Ingresa tu apellido: ")
                campers = cargar_lista_estudiantes()
                bandera = True
                for camper in campers:
                        if camper['name'] == nombre and camper['Second name'] == apellido:
                            print("Tus notas son: ")


                            break
                        else:
                            bandera = False
                if not bandera:
                    print("No se ha encontrado Camper en la base de datos")
                comando2b = menu.subMenuNotasCamper()
        if comando == "E":
            break
    return comando
            
            
        
        
        
        