import menu
import random
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
                        print("***********************************************")
                        print("Nombre: ", nuevaTablaM1[i]['name'])
                        print("Nota Teorica: ", nuevaTablaM1[i]['Modulo 1']['Nota Teorica'])
                        print("Nota Practica: ", nuevaTablaM1[i]['Modulo 1']['Nota Practica'])
                        print("Nota Promedio: ", nuevaTablaM1[i]['Modulo 1']['Actividades'])
                        print("Nota Final: ", nuevaTablaM1[i]['Modulo 1']['Final'])
                        print("***********************************************")

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
                        print("***********************************************")
                        print("Nombre: ", nuevaTablaM2[i]['name'])
                        print("Nota Teorica: ", nuevaTablaM2[i]['Modulo 2']['Nota Teorica'])
                        print("Nota Practica: ", nuevaTablaM2[i]['Modulo 2']['Nota Practica'])
                        print("Nota Promedio: ", nuevaTablaM2[i]['Modulo 2']['Actividades'])
                        print("Nota Final: ", nuevaTablaM2['Modulo 2']['Final'])
                        print("***********************************************")
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
                        print("***********************************************")
                        print("Nombre: ", nuevaTablaM3[i]['name'])
                        print("Nota Teorica: ", nuevaTablaM3[i]['Modulo 3']['Nota Teorica'])
                        print("Nota Practica: ", nuevaTablaM3[i]['Modulo 3']['Nota Practica'])
                        print("Nota Promedio: ", nuevaTablaM3[i]['Modulo 3']['Actividades'])
                        print("Nota Final: ", nuevaTablaM3['Modulo 3']['Final'])
                        print("***********************************************")
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
                        print("***********************************************")
                        print("Nombre: ", nuevaTablaM4[i]['name'])
                        print("Nota Teorica: ", nuevaTablaM4[i]['Modulo 4']['Nota Teorica'])
                        print("Nota Practica: ", nuevaTablaM4[i]['Modulo 4']['Nota Practica'])
                        print("Nota Promedio: ", nuevaTablaM4[i]['Modulo 4']['Actividades'])
                        print("Nota Final: ", nuevaTablaM4['Modulo 4']['Final'])
                        print("***********************************************")
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
                        print("***********************************************")
                        print("Nombre: ", nuevaTablaM5[i]['name'])
                        print("Nota Teorica: ", nuevaTablaM5[i]['Modulo 5']['Nota Teorica'])
                        print("Nota Practica: ", nuevaTablaM5[i]['Modulo 5']['Nota Practica'])
                        print("Nota Promedio: ", nuevaTablaM5[i]['Modulo 5']['Actividades'])
                        print("Nota Final: ", nuevaTablaM5['Modulo 5']['Final'])
                        print("***********************************************")