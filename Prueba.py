import random
import json
from tabulate import tabulate

class AsignarCampersRutas:
    @staticmethod
    def asignar(ruta, listaCampers, nombreEstudiante):
        RutaNode = []
        RutaJava = []
        RutaNet = []
        for camper in listaCampers:
            if camper['name'] == nombreEstudiante:
                if ruta == "Node":
                    RutaNode.append(camper)
                elif ruta == "Java":
                    RutaJava.append(camper)
                elif ruta == "NetCore":
                    RutaNet.append(camper)
        return RutaNode, RutaJava, RutaNet

    @staticmethod
    def asignarAleatorio(listaCampers):
        RutaNode = []
        RutaJava = []
        RutaNet = []

        for camper in listaCampers:
            ruta_aleatoria = random.choice(["Node", "Java", "NetCore"])
            if ruta_aleatoria == "Node":
                RutaNode.append(camper)
            elif ruta_aleatoria == "Java":
                RutaJava.append(camper)
            elif ruta_aleatoria == "NetCore":
                RutaNet.append(camper)
    
        return RutaNode, RutaJava, RutaNet

# Supongamos que tienes una lista de diccionarios de campers llamada 'listaCampers' importada desde un archivo JSON

with open('Campers.json') as f:
    datos = json.load(f)

while True:
    comandoAsignarCamper = input("Presione A para asignar manualmente, B para asignar aleatoriamente o C para salir: ")
    if comandoAsignarCamper == "C":
        break

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
        print("Grupo 1:")
        print(tabulate(ruta1, headers="keys"))
        print()
        print("Grupo 2:")
        print(tabulate(ruta2, headers="keys"))
        print()
        print("Grupo 3:")
        print(tabulate(ruta3, headers="keys"))
        print()

