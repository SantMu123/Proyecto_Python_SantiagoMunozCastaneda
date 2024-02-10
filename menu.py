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
                     
                     A: Campers Inscritos *
                     B: Cambiar de estado a Campers Inscritos
                     C: Asignar Ruta a Camper
                     D: Campers Aprobados *
                     E: Trainers Activos *
                     F: Notas Campers *
                     G: Asignar Notas
                     H: Informacion asociada con las rutas de entrenamiento *
                     
                     """)
    
    if comando2 in ["A", "B", "C", "D", "E", "F", "G"]:
        return comando2
    else:
        print("Comando Incorrecto")
        menuCoordinador()
        
def Sub_menuTrainers():
    
    rutas = ["NodeJs", "Java", "NetCore"]
    trainers = [{"Oscar": 8}, {"Santiago": 12}, {"Olga": 16}, {"Lulu": 20}]
    
    


