import json
import menu
import random
import AsignarCampersRutas
import TablaCampers
import NotasModulos
from tabulate import tabulate

with open('Campers.json') as f:
    datos = json.load(f)
comando1 = "A"
#datos_tabla = []
while comando1 != "D":
    comando1 = menu.principal()
    if comando1 == "C":
        comando2 = "A"
        while comando2 != "I":
            comando2 = menu.menuCoordinador()
            if comando2 == "A":
                comando3 = menu.subMenuAsignarNotas()
                while comando3 != "C":
                    if comando3 == "A":
                        print("Los siguientes son los estudiantes inscritos: ")
                        TablaCampers.visualizar(datos)

                        print("**********************************************")

                        nombre = input("Digite el nombre del estudiante al que desea digitar notas: ")
                        notaTeorica = int(input("Digite la nota teorica: "))
                        notaPractica = int(input("Digite la nota practica: "))

                        promedio = (notaTeorica + notaPractica) / 2

                        print("El promedio del estudiante es: ", promedio)

                        # Usar un indicador para verificar si se ha encontrado al estudiante
                        encontrado = False
                        for camper in datos:
                            if nombre == camper['name']:
                                camper['Teoric Note'] = notaTeorica
                                camper['Practical Note'] = notaPractica
                                camper['Average Note'] = promedio
                                if promedio >= 60:
                                    camper['Status'] = "Aprobado"
                                else:
                                    camper['Status'] = "No Aprobado"
                                encontrado = True
                                break  # Salir del bucle una vez que se haya encontrado al estudiante

                        if not encontrado:
                            print("No se encontró ningún estudiante con ese nombre.")
                        else:
                            TablaCampers.visualizar(datos)

                    elif comando3 == "B":
                        for camper in datos:
                            notaTeorica = random.randint(60,100)
                            notaPractica = random.randint(60,100)
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
                            estados = {"A": "Proceso de Ingreso", "B": "Inscrito", "C": "Aprobado", "D": "Cursando", "E": "Graduado", "F": "Expulsado", "G": "Retirado"}
                            camper['Status'] = estados[estado]
                    
                    TablaCampers.visualizar(datos)
                    comando2B = menu.subMenuInternodeEstado()

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

                datos_clases = [
                    {"Profesor": "Oscar", "Hora": "08:00 - 12:00", "Ruta": "Node JS", "Salon": "A Kepler"},
                    {"Profesor": "Sofía", "Hora": "12:00 - 16:00", "Ruta": "Java", "Salon": "B Apolo"},
                    {"Profesor": "Santiago", "Hora": "16:00 - 20:00", "Ruta": "NetCore", "Salon": "C Artemis"}
                ]

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
                
                TablaCampers.visualizarRutas(nuevas_rutas)
                
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
                RutaSelec = input("Digita la Ruta aa la cual quieres acceder para colocar Nota a un estudiante")
                Examen = input("Digita el numero del examen que vas a digitar: ")
                
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
            
