def principal():
    comando1 = input("""
          Bienvenido a la Intranet CampusLands
          
          Selecciona la opcón según corresponda:
          
          A: Camper
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
                     H: Añadir/Eliminar Trainer
                     
                     """)
    
    if comando2 in ["A", "B", "C", "D", "E", "F", "G", "H"]:
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
                                                B) Ver Campers en Inscrito
                                                C) Ver Campers en Aprobado Examen Inicial
                                                D) Ver Campers con bajo Rendimiento
                                                E) Ver Nota Campers por Ruta -> Modulo
                                                F) Ver Campers en Expulsado
                                                G) Ver Campers en Retirado
                                                H) Ver Menú Anterior
                    
                                            """)
    if comando in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuVisualizarEstado()

def subMenuModulo():
    comando = input("""
                                                Seleccione el numero según el modulo del que quiere saber la nota:
                                                
                                                1) Fundamentos de Programación
                                                2) Programación Web
                                                3) Programación Formal
                                                4) Bases de Datos
                                                5) Backend
                    
                                            """)
    if comando in ["1", "2", "3", "4", "5"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuModulo()
#MENÚ CAMPER
#************************************************************************************************

def MenuCamper():
    comando = input("""
                        BIENVENDIO AL MODULO CAMPERS
                                ¿QUÉ DESEAS HACER?
                    A: Inscripcion
                    B: Ver Notas
                    C: Volver Menú anterior
                    
                    """)
    if comando in ["A", "B", "C"]:
        return comando
    else:
        print("Comando Incorrecto")
        MenuCamper()

def subMenuNotasCamper():
    comando = input("""
                     Selecciona
                     
                     A: Ingresar
                     B: Volver al menú inicial
                     
                     """)
    
    if comando in ["A", "B"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuNotasCamper()

#MENÚ Trainer
#************************************************************************************************

def MenuTrainer(lista):
    try:
        nombre = input("""
                    *********************
                    Ingresa tu nombre: 
                    *********************

                    """)
        for i in lista:
            if i['Profesor'] == nombre:
                print("BIENVENIDO --->", nombre)            
    except Exception:
        print("Acceso denegado, vuelve a intentarlo: ")
        MenuTrainer(lista)


def subMenuTrainer():
    comando = input("""
                    BIENVENIDO AL MODULO TRAINERS
                                ¿QUÉ DESEAS HACER?
                    A: Registro Nuevo Trainer
                    B: Ver Notas Campers
                    C: Salir
                    
                    """)
    if comando in ["A", "B", "C"]:
        return comando
    else:
        print("Comando Incorrecto")
        MenuCamper()
        
def subMenuTrainerHora():
    comando = input(""" 
                                Selecciona Tu hora
                            A) 2:00 PM
                            B) 6:00 PM
                            C) 10:00 PM
                            """)
    if comando in ["A", "B", "C"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuTrainerHora()
        
        
def AñadirEliTrainer():
    comando = input(""" 
                                Selecciona:
                            A) Añadir nuevo Trainer
                            B) Eliminar Trainer
                            C) Volver 
                            """)
    if comando in ["A", "B", "C"]:
        return comando
    else:
        print("Comando Incorrecto")
        AñadirEliTrainer()
#************************************************************************************************
        

