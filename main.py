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
    with open('Campers.json', 'w') as file:
        file.write(json.dumps(lista_trainers, indent=4))

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
                    
                    nombre = input("Digite el nombre del estudiante al que desea cambiar de estado: ")
                    
                    for camper in datos:
                        if camper['name'] == nombre:
                            # Mapear la entrada del usuario a un estado correspondiente
                            estados = {"A": Ingreso, "B": Inscrito, "C": Aprobado, "D": Cursando, "E": Graduado, "F": Expulsado, "G": Retirado}
                            estados[estado].append(camper)
                            break
                            #camper['Status'] = estados[estado]
                        if estado == "F":
                            datos.remove(camper)
                            print("Se ha eliminado correctamente!!!!")
                    
                    #CambioEstado.NuevoEstado(nombre, estado, datos) #Añade camper a la lista de estado especificada
                    TablaCampers.visualizar(datos)
                    comando2B = menu.subMenuInternodeEstado()

            if comando2 == "H":
                print("Añdir nuevo trainer")

            if comando2 == "C":
                def mostrar_clases(datos):
                    print("Se tienen los siguientes profesores, rutas y salones")
                    print("***************************************************")

                    tabla = []
                    for fila in datos:
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
        comandoCam = ModuloCamper()
        if comandoCam == "E":
            continue
    elif comando1 == "B":
        comandoTra = "A"
        while comandoTra != "C":
            print("Modulo trainer")
            comandoTra = "A" 
            #menu.MenuTrainer(datos_clases)
            if comandoTra == "A":
                print("Registrate Nuevo Trainer!!!")
                idTrain = input("Ingresa tu ID: ")
                nombre = input("Ingresa tu nombre: ")
                apellido = input("Ingresa tu apellido: ")
                infoHora = {"A":"2:00 PM", "B":"6:00 PM", "C":"10:00 PM"}
                # Mostrar las horas disponibles
                print(""" 
                                Selecciona Tu hora
                            A) 2:00 PM
                            B) 6:00 PM
                            C) 10:00 PM
                            """)
                hora = input("Elige tu hora (A, B o C): ")

                for i in range(len(datos_clases)):
                    if datos_clases[i]['Profesor'] == nombre:
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
                # Verificar si la hora seleccionada está en el diccionario
                if hora in infoHora:
                    # Guardar la hora seleccionada antes de eliminarla
                    hora_seleccionada = infoHora[hora]
                    # Eliminar la hora seleccionada del diccionario
                    infoHora.pop(hora)
                    for trainer in datos_clases:
                        if trainer['Profesor'] == nombre:
                            trainer['Hora'] = hora_seleccionada 
                            break
                    guardar_lista_Trainers(datos_clases)
                    print(f"Has seleccionado la hora {hora_seleccionada}.")
                    print("Hora eliminada del diccionario.")
                else:
                    print("Hora no válida.")

                    
                
        
