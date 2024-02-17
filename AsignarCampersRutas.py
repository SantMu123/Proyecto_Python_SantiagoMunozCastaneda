import random
import json

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


def asignar(ruta, listaCampers, nombreEstudiante):
        info = {
        "ID": "None",
        "name": "None",
        "Second name": "None",
        "Riesgo":"None",
        "Modulo1": "No Aprobado",
        "NotaPractica1": "None",
        "NotaTeorica1": "None",
        "Actividades1": "None",
        "Final1": "None",
        "Modulo2": "No Aprobado",
        "NotaPractica2": "None",
        "NotaTeorica2": "None",
        "Actividades2": "None",
        "Final2": "None",
        "Modulo3": "No Aprobado",
        "NotaPractica3": "None",
        "NotaTeorica3": "None",
        "Actividades3": "None",
        "Final3": "None",
        "Modulo4": "No Aprobado",
        "NotaPractica4": "None",
        "NotaTeorica4": "None",
        "Actividades4": "None",
        "Final4": "None",
        "Modulo5": "No Aprobado",
        "NotaPractica5": "None",
        "NotaTeorica5": "None",
        "Actividades5": "None",
        "Final5": "None"
    }
        RutaNode = []
        RutaJava = []
        RutaNet = []
        for camper in listaCampers:
            if camper['name'] == nombreEstudiante:
                info['name'] = nombreEstudiante
                info['Second name'] = camper['Second name']
                info['ID'] = camper['ID']
                if ruta == "Node":
                    ListaRutaNode.append(info)
                    guardar_lista_RutaNode(ListaRutaNode)
                    RutaNode.append(info)
                elif ruta == "Java":
                    ListaRutaJava.append(info)
                    guardar_lista_RutaJava(ListaRutaJava)
                    RutaJava.append(info)
                elif ruta == "NetCore":
                    ListaRutaNet.append(info)
                    guardar_lista_RutaNet(ListaRutaNet)
                    RutaNet.append(info)
        return RutaNode, RutaJava, RutaNet

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