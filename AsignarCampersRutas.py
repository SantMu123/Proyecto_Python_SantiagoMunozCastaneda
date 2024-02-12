import random

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