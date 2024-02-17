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
                    nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
                    NT = int(input("Ingresa la nota teorica del modulo: "))
                    NP = int(input("Ingresa la nota practica del modulo: "))
                    AC = int(input("Ingresa la nota de actividades: "))            
                    Ave = (NT*0.3 + NP*0.6 + AC*0.10)
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 1: ")
                    for camper in ListaRuta:
                        if nombre == camper['name']:
                            infoModulo1 = {"name": nombre, "Modulo 1": {"Nota Teorica": NT, "Nota Practica":NP, "Actividades":AC, "Final":Ave}}
                            nuevaTablaM1.append(infoModulo1)
                            break
                    print(nuevaTablaM1)
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
                    for camper in ListaRuta:
                        if nombre == camper['name']:
                            infoModulo2 = {"name": nombre, "Modulo 2": {"Nota Teorica": NT, "Nota Practica":NP, "Actividades":AC, "Final":Ave}}
                            nuevaTablaM2.append(infoModulo2)
                            break
                    print(nuevaTablaM2)
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
                    for camper in ListaRuta:
                        if nombre == camper['name']:
                            infoModulo3 = {"name": nombre, "Modulo 3": {"Nota Teorica": NT, "Nota Practica":NP, "Actividades":AC, "Final":Ave}}
                            nuevaTablaM3.append(infoModulo3)
                            break
                    print(nuevaTablaM1)
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
                    for camper in ListaRuta:
                        if nombre == camper['name']:
                            infoModulo4 = {"name": nombre, "Modulo 4": {"Nota Teorica": NT, "Nota Practica":NP, "Actividades":AC, "Final":Ave}}
                            nuevaTablaM4.append(infoModulo4)
                            break
                    print(nuevaTablaM4)
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
                    for camper in ListaRuta:
                        if nombre == camper['name']:
                            infoModulo5 = {"name": nombre, "Modulo 5": {"Nota Teorica": NT, "Nota Practica":NP, "Actividades":AC, "Final":Ave}}
                            nuevaTablaM5.append(infoModulo5)
                            break
                    print(nuevaTablaM5)
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