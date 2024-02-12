def principal():
    comando1 = input("""
          Bienvenido a la Intranet CampusLands
          
          Selecciona la opcón según corresponda:
          
          A: Estudiante
          B: Trainer
          C: Coordinador
          
          """)
    
    if comando1 in ["A", "B", "C"]:
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
                     H: Informacion asociada con las rutas de entrenamiento *
                     
                     """)
    
    if comando2 in ["A", "B", "C", "D", "E", "F", "G"]:
        return comando2
    else:
        print("Comando Incorrecto")
        menuCoordinador()

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
    


