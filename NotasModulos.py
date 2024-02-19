import menu
import random
import TablaCampers
import json
import tabulate
"""
def VisualizarGrupos(ruta1, ruta2, ruta3):
    nuevaTabla = []
    comando = menu.subMenuVisualizarModulo()
    if comando == "A":
        nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
        notaIntro = int()
        notaPS = 
        notaPython = 
        infoModulo1 = {"name": nombre, "Modulo 1": {"Introduccion Algoritmia": notaIntro, "PSeint":notaPS, "Python":notaPython}}
    elif comando == "B":
        infoModulo2 = {"name": nombre, "Modulo 2": {"HTML": notaHTML, "CSS":notaCSS, "Bootstrap":notaBT}}
    elif comando == "C":    
        infoModulo3 = {"name": nombre, "Modulo 3": {"Java": notaJava, "JavaScript":notaJS, "C#":notaC}}
    elif comando == "D":
        infoModulo4 = {"name": nombre, "Modulo 4": {"Mysql": notaSQL, "MongoDb":notaMD, "Postgresql":notaPGql}}
    elif comando == "E":
        infoModulo5 = {"name": nombre, "Modulo 5": {"NetCore": notaNet, "Spring Boot":notaSB, "Express":notaExp}}
"""
with open('RutaNode.json') as f:
    ListaRutaNode = json.load(f)
    
with open('RutaJava.json') as f:
    ListaRutaJava = json.load(f)
    
with open('RutaNet.json') as f:
    ListaRutaNet = json.load(f)

def guardar_lista_RutaNode(lista_RutaNode):
    with open('RutaNode.json', 'w') as file:
        file.write(json.dumps(lista_RutaNode, indent=4))
def guardar_lista_RutaJava(lista_RutaJava):
    with open('RutaJava.json', 'w') as file:
        file.write(json.dumps(lista_RutaJava, indent=4))
def guardar_lista_RutaNet(lista_RutaNet):
    with open('RutaNet.json', 'w') as file:
        file.write(json.dumps(lista_RutaNet, indent=4))
        
def VisualizarGrupos(ruta, ListaRuta):
    nuevaTablaM1 = []
    nuevaTablaM2 = []
    nuevaTablaM3 = []
    nuevaTablaM4 = []
    nuevaTablaM5 = []
    comando = "A"
    while comando != "F":
        comando = menu.subMenuVisualizarModulo()
        if comando == "A":
            comando2 = "A"
            while comando2 != "C": 
                comando2 = menu.subMenuNotaModulo()
                if comando2 == "A":
                    print("++++++ Has ingresado al modulo de fundamentos de programacón ++++++ \n")
                    id = int(input("Digita el ID del estudiante al que deseas asignar nota: "))
                    NT = int(input("Ingresa la nota teorica del modulo: "))
                    NP = int(input("Ingresa la nota practica del modulo: "))
                    AC = int(input("Ingresa la nota de actividades: "))            
                    Ave = (NT*0.3 + NP*0.6 + AC*0.10)
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 1: ")
                    
                    for i in range(len(ListaRuta)):
                        camper = ListaRuta[i]
                        if camper['ID'] == id:
                            print("Has ingresado")
                            camper['NotaPractica1'] = NP
                            camper['NotaTeorica1'] = NT
                            camper['Actividades1'] = AC
                            camper['Final1'] = Ave
                            if Ave >= 60:
                                camper['Modulo1'] = "Aprobado"
                                camper['Riesgo'] = "Bajo"
                            else:
                                camper['Modulo1'] = "No aprobado"
                                camper['Riesgo'] = "Alto"
                            #nuevaTablaM1.append(infoModulo1)
                            break
                    #print(nuevaTablaM1)
                
                    if ruta == "Node":
                        guardar_lista_RutaNode(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "Java":
                        guardar_lista_RutaJava(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "NetCore":
                        guardar_lista_RutaNet(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    
                elif comando2 == "B":
                    
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 1: ")
                    for i,camper in enumerate(ListaRuta, start=0):
                        NT = random.randint(50,100)
                        NP = random.randint(50,100)
                        AC = random.randint(50,100)            
                        Ave = int(NT*0.3 + NP*0.6 + AC*0.10)
                        infoModulo1 = {"name": camper['name'], "Modulo 1": {"Nota Teorica": NT, "Nota Practica":NP, "Actividades":AC, "Final":Ave}}
                        nuevaTablaM1.append(infoModulo1)

                    TablaCampers.visualizarNotasModulos(nuevaTablaM1)
        elif comando == "B":
            comando2 = "A"
            while comando2 != "C": 
                comando2 = menu.subMenuNotaModulo()
                if comando2 == "A":
                    print("++++++ Has ingresado al modulo de Programacion Web ++++++ \n")
                    nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
                    NT = int(input("Ingresa la nota teorica del modulo: "))
                    NP = int(input("Ingresa la nota practica del modulo: "))
                    AC = int(input("Ingresa la nota de actividades: "))            
                    Ave = int(NT*0.3 + NP*0.6 + AC*0.10)
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 2: ")
                    for i in range(len(ListaRuta)):
                        camper = ListaRuta[i]
                        if camper['name'] == nombre:
                            camper['NotaPractica2'] = NP
                            camper['NotaTeorica2'] = NT
                            camper['Actividades2'] = AC
                            camper['Final2'] = Ave
                            if Ave >= 60:
                                camper['Modulo2'] = "Aprobado"
                                camper['Riesgo'] = "Bajo"
                            else:
                                camper['Modulo2'] = "No aprobado"
                                camper['Riesgo'] = "Alto"
                            #nuevaTablaM1.append(infoModulo1)
                            break
                    #print(nuevaTablaM1)
                
                    if ruta == "Node":
                        guardar_lista_RutaNode(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "Java":
                        guardar_lista_RutaJava(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "NetCore":
                        guardar_lista_RutaNet(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                        
                elif comando2 == "B":
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 2: ")
                    for i,camper in enumerate(ListaRuta, start=0):
                        NT = random.randint(50,100)
                        NP = random.randint(50,100)
                        AC = random.randint(50,100)            
                        Ave = int(NT*0.3 + NP*0.6 + AC*0.10)
                        infoModulo2 = {"name": camper['name'], "Modulo 2": {"Nota Teorica": NT, "Nota Practica":NP, "Actividades":AC, "Final":Ave}}
                        nuevaTablaM2.append(infoModulo2)
                    
                    TablaCampers.visualizarNotasModulos(nuevaTablaM1)
        elif comando == "C":
            while comando2 != "C": 
                comando2 = menu.subMenuNotaModulo()
                if comando2 == "A":
                    print("++++++ Has ingresado al modulo de Programacion Formal ++++++ \n")
                    nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
                    NT = int(input("Ingresa la nota teorica del modulo: "))
                    NP = int(input("Ingresa la nota practica del modulo: "))
                    AC = int(input("Ingresa la nota de actividades: "))            
                    Ave = int(NT*0.3 + NP*0.6 + AC*0.10)
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 3: ")
                    for i in range(len(ListaRuta)):
                        camper = ListaRuta[i]
                        if camper['name'] == nombre:
                            camper['NotaPractica3'] = NP
                            camper['NotaTeorica3'] = NT
                            camper['Actividades3'] = AC
                            camper['Final3'] = Ave
                            if Ave >= 60:
                                camper['Modulo3'] = "Aprobado"
                                camper['Riesgo'] = "Bajo"
                            else:
                                camper['Modulo3'] = "No aprobado"
                                camper['Riesgo'] = "Alto"
                            #nuevaTablaM1.append(infoModulo1)
                            break
                    #print(nuevaTablaM1)
                
                    if ruta == "Node":
                        guardar_lista_RutaNode(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "Java":
                        guardar_lista_RutaJava(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "NetCore":
                        guardar_lista_RutaNet(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                elif comando2 == "B":
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 3: ")
                    for i,camper in enumerate(ListaRuta, start=0):
                        NT = random.randint(50,100)
                        NP = random.randint(50,100)
                        AC = random.randint(50,100)            
                        Ave = int(NT*0.3 + NP*0.6 + AC*0.10)
                        infoModulo3 = {"name": camper['name'], "Modulo 3": {"Nota Teorica": NT, "Nota Practica":NP, "Promedio":AC, "Final":Ave}}
                        nuevaTablaM3.append(infoModulo3)
                    TablaCampers.visualizarNotasModulos(nuevaTablaM1)
        elif comando == "D":
            while comando2 != "C": 
                comando2 = menu.subMenuNotaModulo()
                if comando2 == "A":
                    print("++++++ Has ingresado al modulo de Base de datos ++++++ \n")
                    nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
                    NT = int(input("Ingresa la nota teorica del modulo: "))
                    NP = int(input("Ingresa la nota practica del modulo: "))
                    AC = int(input("Ingresa la nota de actividades: "))            
                    Ave = int(NT*0.3 + NP*0.6 + AC*0.10)
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 4: ")
                    for i in range(len(ListaRuta)):
                        camper = ListaRuta[i]
                        if camper['name'] == nombre:
                            camper['NotaPractica4'] = NP
                            camper['NotaTeorica4'] = NT
                            camper['Actividades4'] = AC
                            camper['Final4'] = Ave
                            if Ave >= 60:
                                camper['Modulo4'] = "Aprobado"
                                camper['Riesgo'] = "Bajo"
                            else:
                                camper['Modulo4'] = "No aprobado"
                                camper['Riesgo'] = "Alto"
                            #nuevaTablaM1.append(infoModulo1)
                            break
                    #print(nuevaTablaM1)
                
                    if ruta == "Node":
                        guardar_lista_RutaNode(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "Java":
                        guardar_lista_RutaJava(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "NetCore":
                        guardar_lista_RutaNet(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                elif comando2 == "B":
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 4: ")
                    for i,camper in enumerate(ListaRuta, start=0):
                        NT = random.randint(50,100)
                        NP = random.randint(50,100)
                        AC = random.randint(50,100)            
                        Ave = int(NT*0.3 + NP*0.6 + AC*0.10)
                        infoModulo4 = {"name": camper['name'], "Modulo 4": {"Nota Teorica": NT, "Nota Practica":NP, "Actividades":AC, "Final":Ave}}
                        nuevaTablaM4.append(infoModulo4)
                    TablaCampers.visualizarNotasModulos(nuevaTablaM1)
        elif comando == "E":
            while comando2 != "C": 
                comando2 = menu.subMenuNotaModulo()
                if comando2 == "A":
                    print("++++++ Has ingresado al modulo de Backend ++++++ \n")
                    nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
                    NT = int(input("Ingresa la nota teorica del modulo: "))
                    NP = int(input("Ingresa la nota practica del modulo: "))
                    AC = int(input("Ingresa la nota de actividades: "))            
                    Ave = int(NT*0.3 + NP*0.6 + AC*0.10)
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 5: ")
                    for i in range(len(ListaRuta)):
                        camper = ListaRuta[i]
                        if camper['name'] == nombre:
                            camper['NotaPractica5'] = NP
                            camper['NotaTeorica5'] = NT
                            camper['Actividades5'] = AC
                            camper['Final5'] = Ave
                            if Ave >= 60:
                                camper['Modulo5'] = "Aprobado"
                                camper['Riesgo'] = "Bajo"
                            else:
                                camper['Modulo5'] = "No aprobado"
                                camper['Riesgo'] = "Alto"
                            #nuevaTablaM1.append(infoModulo1)
                            break
                    #print(nuevaTablaM1)
                
                    if ruta == "Node":
                        guardar_lista_RutaNode(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "Java":
                        guardar_lista_RutaJava(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                    elif ruta == "NetCore":
                        guardar_lista_RutaNet(ListaRuta)
                        TablaCampers.visualizar(ListaRuta)
                elif comando2 == "B":
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 5: ")
                    for i,camper in enumerate(ListaRuta, start=0):
                        NT = random.randint(50,100)
                        NP = random.randint(50,100)
                        AC = random.randint(50,100)            
                        Ave = int(NT*0.3 + NP*0.6 + AC*0.10)
                        infoModulo5 = {"name": camper['name'], "Modulo 5": {"Nota Teorica": NT, "Nota Practica":NP, "Actividades":AC, "Final":Ave}}
                        nuevaTablaM5.append(infoModulo5)
                    TablaCampers.visualizarNotasModulos(nuevaTablaM1)
    