import json
import menu
import random
import AsignarCampersRutas
import TablaCampers
import NotasModulos
from ModuloEstudiante import ModuloCamper
from tabulate import tabulate

def guardar_lista_estudiantes(lista_estudiantes):
    with open('Campers.json', 'w') as file:
        file.write(json.dumps(lista_estudiantes, indent=4))
def guardar_lista_Trainers(lista_trainers):
    with open('Trainers.json', 'w') as file:
        file.write(json.dumps(lista_trainers, indent=4))
def guardar_lista_RutaNode(lista_RutaNode):
    with open('RutaNode.json', 'w') as file:
        file.write(json.dumps(lista_RutaNode, indent=4))
def guardar_lista_RutaJava(lista_RutaJava):
    with open('RutaJava.json', 'w') as file:
        file.write(json.dumps(lista_RutaJava, indent=4))
def guardar_lista_RutaNet(lista_RutaNet):
    with open('RutaNet.json', 'w') as file:
        file.write(json.dumps(lista_RutaNet, indent=4))

Ingreso = []
Inscrito = []
Aprobado = []
Cursando = []
Graduado = []
Expulsado = []
Retirado = []
datos = []
with open('Trainers.json') as f:
    datos_clases = json.load(f)
    
with open('Campers.json') as f:
    datos = json.load(f)
    
with open('RutaNode.json') as f:
    ListaRutaNode = json.load(f)
    
with open('RutaJava.json') as f:
    ListaRutaJava = json.load(f)
    
with open('RutaNet.json') as f:
    ListaRutaNet = json.load(f)
    
comando1 = "A"
#datos_tabla = []
while comando1 != "D":
    comando1 = menu.principal()
    if comando1 == "C":
        comando2 = "A"
        while comando2 != "G":
            comando2 = menu.menuCoordinador()
            if comando2 == "A":
                comando3 = menu.subMenuAsignarNotas()
                while comando3 != "C":
                    if comando3 == "A":
                        print("Los siguientes son los estudiantes inscritos: ")
                        TablaCampers.visualizar(datos)

                        print("**********************************************")

                        ID = int(input("Digite el ID del estudiante al que desea digitar notas: "))
                        notaTeorica = int(input("Digite la nota teorica: "))
                        notaPractica = int(input("Digite la nota practica: "))

                        promedio = (notaTeorica + notaPractica) / 2

                        print("El promedio del estudiante es: ", promedio)

                        encontrado = False
                        
                        for i in range(len(datos)):
                            if datos[i]['ID'] == ID:
                                camper = datos[i]  # Comparar ID como cadenas
                                camper['Teoric Note'] = notaTeorica
                                camper['Practical Note'] = notaPractica
                                camper['Average Note'] = promedio
                                if promedio >= 60:
                                    camper['Status'] = "Aprobado"
                                else:
                                    camper['Status'] = "No Aprobado"                                
                                encontrado = True                                
                                datos.pop(i)
                                datos.append(camper) 

                        if not encontrado:
                            print("No se encontró ningún estudiante con ese ID.")
                        else:
                            guardar_lista_estudiantes(datos)
                            print("Los datos del estudiante han sido actualizados.")
                            TablaCampers.visualizar(datos)

                    elif comando3 == "B":
                        for camper in datos:
                            notaTeorica = random.randint(20,100)
                            notaPractica = random.randint(20,100)
                            promedio = (notaTeorica + notaPractica) / 2

                            camper['Teoric Note'] = notaTeorica
                            camper['Practical Note'] = notaPractica  # Corregir aquí
                            camper['Average Note'] = promedio

                            if promedio >= 60:
                                camper['Status'] = "Aprobado"
                            else:
                                camper['Status'] = "No Aprobado"

                        TablaCampers.visualizar(datos)
                    comando3 = menu.subMenuAsignarNotas()
                    
            if comando2 == "B":
                comando2B = "A"
                while comando2B != "B":
                    TablaCampers.visualizar(datos)

                    print("*******************************************************")
                    estado = menu.subMenuEstado()
                    print("*******************************************************")
                    
                    ID = int(input("Digite el ID del estudiante al que deseas cambiar de estado: "))
                    encontrado = False
                    for i in range(len(datos)):
                        if datos[i]['ID'] == ID:
                            camper = datos[i]
                            estados = {"A": "Ingreso", "B": "Inscrito", "C": "Aprobado", "D": "Cursando", "E": "Graduado", "F": "Expulsado", "G": "Retirado"}
                            camper['Status'] = estados[estado]
                            #estados[estado].append(camper)
                            encontrado = True                                
                            datos.pop(i)
                            datos.append(camper) 
                            #camper['Status'] = estados[estado]
                        if estado == "F":
                            datos.remove(camper)
                            print("Se ha eliminado correctamente!!!!")
                    if not encontrado:
                        print("No se encontró ningún estudiante con ese ID.")
                    else:
                        guardar_lista_estudiantes(datos)
                        print("Los datos del estudiante han sido actualizados.")
                        TablaCampers.visualizar(datos)
                    #CambioEstado.NuevoEstado(nombre, estado, datos) #Añade camper a la lista de estado especificada
                    #TablaCampers.visualizar(datos)
                    comando2B = menu.subMenuInternodeEstado()

            if comando2 == "H":
                comandoTra4 = "A"
                while comandoTra4 != "C":
                    comandoTra4 = menu.AñadirEliTrainer()
                    if comandoTra4 == "A":
                        nombreTrainer = input("Digita el nombre del nuevo trainer: ")
                        IDTrainer = input("Digita la ID del nuevo trainer: ")
                        for i in range(len(datos_clases)):
                            trainer = datos_clases[i]
                            if trainer['ID'] == IDTrainer: 
                                print("El trainer ya se encuentra registrado") 
                            else:
                                info = {   
                                        "ID": IDTrainer,
                                        "Profesor": nombreTrainer,
                                        "Hora": "None",
                                        "Ruta": "None",
                                        "Salon": "None"
                                    }
                                datos_clases.append(info)
                                guardar_lista_Trainers(datos_clases)
                                break
                    elif comandoTra4 == "B":
                        IDTrainer = input("Digita la ID del trainer a Eliminar: ")
                        for i in range(len(datos_clases)):
                            trainer = datos_clases[i]
                            if trainer['ID'] == IDTrainer: 
                                datos_clases.pop(i)
                                guardar_lista_Trainers(datos_clases)
                                print("Eliminacion Exitosa!!!")
                                break
            if comando2 == "C":
                def mostrar_clases(datos):
                    print("Se tienen los siguientes profesores, rutas y salones")
                    print("***************************************************")

                    tabla = []
                    for fila in datos:
                        IDProfesor = fila['ID']
                        nombre_profesor = fila["Profesor"]
                        hora = fila["Hora"]
                        ruta = fila["Ruta"]
                        salon = fila["Salon"]

                        tabla.append([nombre_profesor, hora, ruta, salon])

                    encabezados = ["Profesor", "Hora", "Ruta", "Salon"]
                    
                    print(tabulate(tabla, headers=encabezados))

                def crear_rutas():
                    bandera = True
                    rutas = set()
                    profesores_seleccionados = set()
                    rutas_seleccionadas = set()
                    salones_seleccionados = set()

                    while bandera:
                        comando_ruta = menu.subMenuCreacionRuta()
                        if comando_ruta.upper() == "B":
                            bandera = False
                            continue

                        profesor = input("Digite el nombre del profesor de la Ruta: ")
                        if profesor in profesores_seleccionados:
                            print("Este profesor ya ha sido seleccionado anteriormente.")
                            continue
                        ruta = input("Digite la ruta: ")
                        if ruta in rutas_seleccionadas:
                            print("Esta ruta ya ha sido seleccionada anteriormente.")
                            continue

                        salon = input("Digite el salon: ")
                        if salon in salones_seleccionados:
                            print("Este salon ya ha sido seleccionado anteriormente.")
                            continue
                        
                        
                        if ruta == "Node":
                            for i in range(len(datos_clases)):
                                trainer = datos_clases[i]
                                if trainer['Profesor'] == profesor:
                                    ListaRutaNode.append(trainer)
                                    guardar_lista_RutaNode(ListaRutaNode)
                                    break
                        if ruta == "Java":
                            for i in range(len(datos_clases)):
                                trainer = datos_clases[i]
                                if trainer['Profesor'] == profesor:
                                    ListaRutaJava.append(trainer)
                                    guardar_lista_RutaNode(ListaRutaJava)
                                    break
                        if ruta == "NetCore":
                            for i in range(len(datos_clases)):
                                trainer = datos_clases[i]
                                if trainer['Profesor'] == profesor:
                                    ListaRutaNet.append(trainer)
                                    guardar_lista_RutaNode(ListaRutaNet)
                                    break

                        profesores_seleccionados.add(profesor)
                        rutas_seleccionadas.add(ruta)
                        salones_seleccionados.add(salon)

                        nueva_ruta = (profesor, ruta, salon)
                        rutas.add(nueva_ruta)

                    return rutas
                """
                datos_clases = [
                    {"Profesor": "Oscar", "Hora": "08:00 - 12:00", "Ruta": "Node JS", "Salon": "A Kepler"},
                    {"Profesor": "Sofia", "Hora": "12:00 - 16:00", "Ruta": "Java", "Salon": "B Apolo"},
                    {"Profesor": "Santiago", "Hora": "16:00 - 20:00", "Ruta": "NetCore", "Salon": "C Artemis"}
                ]
                """
                mostrar_clases(datos_clases)

                nuevas_rutas = crear_rutas()
                print(nuevas_rutas)
                
                comando2 = menu.menuCoordinador()
                
                
            if comando2 == "D":
                print("Se tienen los siguientes Campers: ")
                TablaCampers.visualizar(datos)

                print("******************************************")
                print("Se tienen las siguientes Rutas Establecidas: ")
                print("******************************************")
                try:
                    TablaCampers.visualizarRutas(nuevas_rutas)
                except Exception:
                    print("No Hay Trainers registrados: ")
                    continue
                
                comandoAsignarCamper = "A"
                while comandoAsignarCamper != "C":
                    comandoAsignarCamper = menu.subMenuAsignarRutas()
    
                    if comandoAsignarCamper == "A":
                        nom = input("Digita el nombre del camper al que quieres asignar a una ruta: ")
                        rut = input("Selecciona la Ruta, recuerda que hay capacidad de 33 estudiantes: ")
                        tabla = AsignarCampersRutas.asignar(rut, datos, nom)
                        for i, ruta in enumerate(tabla, start=1):
                            print(f"Grupo {i}:")
                            print(tabulate(ruta, headers="keys"))
                            print()

                    elif comandoAsignarCamper == "B":
                        ruta1, ruta2, ruta3 = AsignarCampersRutas.asignarAleatorio(datos)
                        print("Ruta Node JS:")
                        print(tabulate(ruta1, headers="keys"))
                        print()
                        print("Ruta Java:")
                        print(tabulate(ruta2, headers="keys"))
                        print()
                        print("Ruta NetCore:")
                        print(tabulate(ruta3, headers="keys"))
                        print()
                        break
                    
                #comando2 = menu.menuCoordinador()
                
            if comando2 == "E":
                RutaSelec = input("Digita la Ruta aa la cual quieres acceder para colocar Nota a un estudiante: ")
                
                if RutaSelec == "Node":
                    print("Se tienen los siguientes estudiantes: ")
                    print(tabulate(ruta1, headers="keys"))
                    NotasModulos.VisualizarGrupos(RutaSelec, ruta1)
                elif RutaSelec == "Java":
                    print("Se tienen los siguientes estudiantes: ")
                    print(tabulate(ruta2, headers="keys"))
                    NotasModulos.VisualizarGrupos(RutaSelec, ruta2)
                elif RutaSelec == "NetCore":
                    print("Se tienen los siguientes estudiantes: ")
                    print(tabulate(ruta3, headers="keys"))
                    NotasModulos.VisualizarGrupos(RutaSelec, ruta3)

            if comando2 == "F":
                comando3B = "A"
                while comando3B != "H":
                    estado_ = menu.subMenuVisualizarEstado()
                    if estado_ == "A":
                        print(" Se encuentran los siguientes estudiantes:  \n")
                        TablaCampers.visualizar(Ingreso)                
                    if estado_ == "B":
                        print(" Se encuentran los siguientes estudiantes:  \n")
                        TablaCampers.visualizar(Inscrito)  
                    if estado_ == "C":
                        print(" Se encuentran los siguientes estudiantes:  \n")
                        TablaCampers.visualizar(Aprobado)  
                    if estado_ == "D":
                        print(" Se encuentran los siguientes estudiantes:  \n")
                        TablaCampers.visualizar(Cursando)   
                    if estado_ == "E":
                        print(" Se encuentran los siguientes estudiantes:  \n")
                        TablaCampers.visualizar(Graduado)  
                    if estado_ == "F":
                        print(" Se encuentran los siguientes estudiantes:  \n")
                        TablaCampers.visualizar(Expulsado)  
                    if estado_ == "G":
                        print(" Se encuentran los siguientes estudiantes:  \n")
                        TablaCampers.visualizar(Retirado)  
                        
    elif comando1 == "A":
        comando1 = "A"
        while comando1 != "C":
            comando1 = menu.MenuCamper()
            if comando1 == "A":
                comandoCam = ModuloCamper()
            if comando1 == "B":
                print("Notas")

    elif comando1 == "B":
        comandoTra = "A"
        while comandoTra != "C":
            print("Modulo trainer")
            comandoTra = menu.subMenuTrainer()
            #menu.MenuTrainer(datos_clases)
            listaHorasNoDis = []
            if comandoTra == "A":
                print("¡Regístrate como Nuevo Trainer!")

                idTrain = input("Ingresa tu ID: ")
                nombre = input("Ingresa tu nombre: ")
                apellido = input("Ingresa tu apellido: ")

                infoHora = {"A": "2:00 PM", "B": "6:00 PM", "C": "10:00 PM"}

                hora = menu.subMenuTrainerHora()  # Supongo que aquí estás obteniendo la hora de algún menú.

                encontrado = False

                for i, trainer in enumerate(datos_clases):
                    if trainer['Profesor'] == nombre:
                        try:
                            if hora in infoHora:
                                trainer['Hora'] = infoHora[hora]
                                print(f"Has seleccionado la hora {infoHora[hora]}.")
                                listaHorasNoDis.append(infoHora[hora])
                                if listaHorasNoDis:
                                    print("Horas no disponibles: ", listaHorasNoDis)
                                else:
                                    print("Todas las horas están disponibles.")
                                del infoHora[hora]
                                encontrado = True
                                break
                            else:
                                print("Hora no disponible.")
                        except KeyError:
                            print("Error al intentar asignar la hora.")
                            encontrado = True  # Marcamos como encontrado para evitar el mensaje "No se encontró ningún Profesor en el sistema."

                if not encontrado:
                    print("No se encontró ningún Profesor en el sistema.")
                else:
                    guardar_lista_Trainers(datos_clases)
                    print("Los datos del trainer han sido actualizados.")
                    TablaCampers.visualizar(datos_clases)

            elif comandoTra == "B":
                print("Opcion B")
                
        
