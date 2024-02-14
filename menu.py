def principal():
    comando1 = input("""
          Bienvenido a la Intranet CampusLands
          
          Selecciona la opcón según corresponda:
          
          A: Estudiante
          B: Trainer
          C: Coordinador
          D: Finalizar Programa
          
          """)
    
    if comando1 in ["A", "B", "C", "D"]:
        return comando1
    else:
        print("Comando Incorrecto")
        principal()
        

def menuCoordinador():
    comando2 = input("""
                     Sistema Coordinador
                     
                     A: Asignar Notas Nuevos Campers
                     B: Cambiar de estado a Campers Inscritos
                     C: Construir Rutas
                     D: Asignar Campers a Rutas
                     E: Asignar Notas
                     F: Reporte Estado Campers
                     G: Volver al menú anterior
                     
                     """)
    
    if comando2 in ["A", "B", "C", "D", "E", "F", "G"]:
        return comando2
    else:
        print("Comando Incorrecto")
        menuCoordinador()

def subMenuEstado():
    comando = input("""
                Existen los siguientes Estados posibles:
                
                A) Proceso de Ingreso
                B) Inscrito
                C) Aprobado
                D) Cursando
                E) Graduado
                F) Expulsado
                G) Retirado
                    
                        """)
    if comando in ["A", "B", "C", "D", "E", "F", "G"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuEstado()

def subMenuInternodeEstado():
    comando = input("""Seleccione según su necesdad: 
                                    
                                A): Asignar un nuevo Estado
                                B): Salir al Menú anterior
                                    
                                    """)
    if comando in ["A", "B"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuInternodeEstado()

def subMenuAsignarNotas():
    comando = input("""
                     Asignar Notas
                     
                     A: Asignar Nota a Camper
                     B: Asignar Nota a Todos de Forma Aleatoria
                     C: Salir al Menú anterior
                     
                     """)
    
    if comando in ["A", "B", "C"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuAsignarNotas()
    
def subMenuCreacionRuta():
    comando = input("""
                    Presione:
                    
                            A: Para crear Rutas
                            B: Para Regresar al menú inicial
                    
                    """)
    
    if comando in ["A", "B"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuCreacionRuta()

def subMenuAsignarRutas():
    comando = input("""
                                    Seleccione según su necesidad:
                                    
                                    A) Asignar manualmente camper a una ruta
                                    B) Asignar aleatoriamente
                                    C) Volver al menu anterior
                                    D) Volver a ver la tabla de Campers y las rutas ***
                                            """)
    if comando in ["A", "B", "C", "D"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuCreacionRuta()
        
def subMenuVisualizarModulo():
    comando = input("""
                                    Seleccione según el modulo que deseas ver:
                                    
                                    A) Fundamentos de programacion
                                    B) Programacion Web
                                    C) Programacion Formal
                                    D) Base de datos
                                    E) Backend
                                    F) Volver al Menu Anterior
                                            """)
    if comando in ["A", "B", "C", "D", "E", "F"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuVisualizarModulo()
        
def subMenuNotaModulo():
    comando = input("""
                                                Seleccione según su necesidad:
                                                
                                                A) Asignar nota manualmente a camper
                                                B) Asignar aleatoriamente
                                                C) Volver al menu anterior
                                                D) Volver a ver la tabla de Campers y las rutas
                                            """)
    if comando in ["A", "B", "C", "D"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuNotaModulo()

def subMenuVisualizarEstado():
    comando = input("""
                                                Seleccione según su necesidad:
                                                
                                                A) Ver Campers en Proceso de Ingreso
                                                B) Ver Campers en Insicrito
                                                C) Ver Campers en Aprobado
                                                D) Ver Campers en Cursando
                                                E) Ver Campers en Graduado
                                                F) Ver Campers en Expulsado
                                                G) Ver Campers en Retirado
                                                H) Ver Menú Anterior
                    
                                            """)
    if comando in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuVisualizarEstado()

#MENÚ CAMPER
#************************************************************************************************

def MenuCamper():
    comando = input("""
                        BIENVENDIO AL MODULO CAMPERS
                                ¿QUÉ DESEAS HACER?
                    A: Inscripcion
                    B: Ver Notas
                    C: Ver Trainers
                    D: Ver Rutas Modulos
                    E: Volver Menú anterior
                    
                    """)
    if comando in ["A", "B", "C", "D", "E"]:
        return comando
    else:
        print("Comando Incorrecto")
        MenuCamper()

#MENÚ Trainer
#************************************************************************************************

def MenuTrainer(lista):
    nombre = input("""
                   *********************
                   Ingresa tu nombre: 
                   *********************

                   """)
    if nombre in lista:
        print("BIENVENIDO --->", nombre)
    else:
        print("Acceso denegado, vuelve a intentarlo: ")
        MenuTrainer(lista)


def subMenuTrainer():
    comando = input("""
                    BIENVENDIO AL MODULO TRAINERS
                                ¿QUÉ DESEAS HACER?
                    A: Inscripcion
                    B: Ver Notas
                    C: Ver Trainers
                    D: Ver Rutas Modulos
                    E: Salir
                    
                    """)
    if comando in ["A", "B", "C", "D", "E"]:
        return comando
    else:
        print("Comando Incorrecto")
        MenuCamper()

#************************************************************************************************
        

