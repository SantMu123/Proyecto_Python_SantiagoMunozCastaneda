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
                     F: Otras Funcionalidades
                     G: Asignar Notas
                     H: Informacion asociada con las rutas de entrenamiento 
                     I: Volver al menú anterior
                     
                     """)
    
    if comando2 in ["A", "B", "C", "D", "E", "F", "G", "H", "I"]:
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
                                    D) Volver a ver la tabla de Campers y las rutas
                                            """)
    if comando in ["A", "B", "C", "D"]:
        return comando
    else:
        print("Comando Incorrecto")
        subMenuCreacionRuta()