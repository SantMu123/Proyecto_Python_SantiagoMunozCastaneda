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
                    print("++++++ Has ingresado al modulo de fundamentos de prgramacón ++++++ \n")
                    nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
                    NT = int(input("Ingresa la nota teorica del modulo: "))
                    NP = int(input("Ingresa la nota practica del modulo: "))
                    Ave = (NT + NP) / 2
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 1: ")
                    for camper in ListaRuta:
                        if nombre == camper['name']:
                            infoModulo1 = {"name": nombre, "Modulo 1": {"Nota Teorica": NT, "Nota Practica":NP, "Promedio":Ave}}
                            nuevaTablaM1.append(infoModulo1)
                            break
                    print(nuevaTablaM1)
                elif comando2 == "B":
                    print("RUTA ", ruta, " : ")
                    print("         MODULO 1: ")
                    for i,camper in enumerate(ListaRuta, start=0):
                        NT = random.randint(50,100)
                        NP = random.randint(50,100)
                        Ave = (NT + NP) / 2
                        infoModulo1 = {"name": camper['name'], "Modulo 1": {"Nota Teorica": NT, "Nota Practica":NP, "Promedio":Ave}}
                        nuevaTablaM1.append(infoModulo1)
                        print("***********************************************")
                        print("Nombre: ", nuevaTablaM1[i]['name'])
                        print("Nota Teorica: ", nuevaTablaM1[i]['Modulo 1']['Nota Teorica'])
                        print("Nota Practica: ", nuevaTablaM1[i]['Modulo 1']['Nota Practica'])
                        print("Nota Promedio: ", nuevaTablaM1[i]['Modulo 1']['Promedio'])
                        print("***********************************************")

                    
        elif comando == "B":
            print("++++++ Has ingresado al modulo de programación WEB ++++++ \n")
            nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
            NT = int(input("Ingresa la nota teorica del modulo: "))
            NP = int(input("Ingresa la nota practica del modulo: "))
            Ave = (NT + NP) / 2
            print("RUTA ", ruta, " : ")
            print("         MODULO 2: ")
            infoModulo2 = {"name": nombre, "Modulo 1": {"Nota Teorica": NT, "Nota Practica":NP, "Promedio":Ave}}
        elif comando == "C":
            print("++++++ Has ingresado al modulo de programación formal ++++++ \n")
            nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
            NT = int(input("Ingresa la nota teorica del modulo: "))
            NP = int(input("Ingresa la nota practica del modulo: "))
            Ave = (NT + NP) / 2
            print("RUTA ", ruta, " : ")
            print("         MODULO 3: ")    
            infoModulo3 = {"name": nombre, "Modulo 1": {"Nota Teorica": NT, "Nota Practica":NP, "Promedio":Ave}}
        elif comando == "D":
            print("++++++ Has ingresado al modulo de Base de Datos ++++++ \n")
            nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
            NT = int(input("Ingresa la nota teorica del modulo: "))
            NP = int(input("Ingresa la nota practica del modulo: "))
            Ave = (NT + NP) / 2
            print("RUTA ", ruta, " : ")
            print("         MODULO 4: ")
            infoModulo4 = {"name": nombre, "Modulo 1": {"Nota Teorica": NT, "Nota Practica":NP, "Promedio":Ave}}
        elif comando == "E":
            print("++++++ Has ingresado al modulo de Backend ++++++ \n")
            nombre = input("Digita el nombre del estudiante al que deseas asignar nota: ")
            NT = int(input("Ingresa la nota teorica del modulo: "))
            NP = int(input("Ingresa la nota practica del modulo: "))
            Ave = (NT + NP) / 2
            print("RUTA ", ruta, " : ")
            print("         MODULO 5: ")
            infoModulo5 = {"name": nombre, "Modulo 1": {"Nota Teorica": NT, "Nota Practica":NP, "Promedio":Ave}}