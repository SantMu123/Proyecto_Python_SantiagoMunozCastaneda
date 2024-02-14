import menu

comando = "A"

lista = ['oscar', 'santiago', 'sofia']

menu.MenuTrainer(lista)
comando = "A"
while comando != "E":
    comando = menu.subMenuTrainer()
    if comando == "A":
        
        nombre = input("Digita tu nombre: ")
        segundoNombre = input("Digita tu apellido")
        direccion = input("Digita tu direccion: ")
        asistente = input("Digita tu attendant: ")
        numeroCel = input("Digita tu numero CEL: ")
        numeroTel = input("Digita tu numero TEl: ")
        
        info = {
      "name": nombre,
      "Second name": segundoNombre,
      "Adress": direccion,
      "attendant": asistente,
      "Number Contact #1": numeroCel,
      "Number Contact #2": numeroCel,
      "Status": "Inscrito",
      "Risk": "None",
      "Teoric Note": "None",
      "Practical Note": "None",
      "Average Note": "None"
    }

    elif comando == "B":
        print("hola")