#Importar librerias necesarias

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title('Juego triqui')

#Empieza X

jugador_1 = "ambiente"
jugador_2 = "agente"
signo_j1 = "X"
signo_j2 = "O"
clicked = True
contador = 0
ganador = False
print("----------------------")
print("jugador 1: "+jugador_1)
print("Signo : "+signo_j1)
print("----------------------")
print("jugador 2: "+jugador_2)
print("Signo : "+signo_j2)
print("----------------------")

#Cambia signo de los jugadores
def cambio_signo():
    pass

#Cambio de orden del jugador que inicia

def cambio_orden():
    pass

#Desactiva todos los botones
def desactivacion_botones():

    for boton in global tablero:
        boton.config(state = DISABLED)

#Revisa si en el tablero ha ganado un jugador

def victoria(signo):
    
    global ganador  

    #Revision para las X's

    for i in range(3):
        for j in range(2):
            if tablero[(i*3)+0]["text"] == signo and tablero[(i*3)+1]["text"] == signo and tablero[(i*3)+2]["text"] == signo:
                for k in range(3):
                    tablero[(i*3)+k].config(bg="green")
                    ganador = True
                    messagebox.showinfo("Triqui", (signo + " gana"))
                    desactivacion_botones()
                    return True
            if tablero[i]["text"] == signo and tablero[(i+3)]["text"] == signo and tablero[(i+6)]["text"] == signo:
                    for k in range(i,9,3):
                    tablero[k].config(bg="green")
                    ganador = True
                    messagebox.showinfo("Triqui", (signo + " gana"))
                    desactivacion_botones()
                    return True
    if tablero[0]["text"] == signo and tablero[4]["text"] == signo andtablero[8]["text"] == signo:
        tablero[0].config(bg="green")
        tablero[4].config(bg="green")
        tablero[8].config(bg="green")
        ganador = True
        messagebox.showinfo("Triqui", (signo + " gana"))
        desactivacion_botones()
        return True
    if tablero[2]["text"] == signo and tablero[4]["text"] == signo andtablero[6]["text"] == signo:
        tablero[2].config(bg="green")
        tablero[4].config(bg="green")
        tablero[6].config(bg="green")
        ganador = True
        messagebox.showinfo("Triqui", (signo + " gana"))
        desactivacion_botones()
        return True

    return False

#Estimulo? percepcion? generada por el ambiente

def b_click(boton):
    global clicked, contador

    if boton["text"] == " ":
        if jugador_1 == "ambiente": 
            boton["text"] = signo_j1
            contador += 1
        if victoria(signo_j1) == False:
            eleccion_agente = programa_agente(contador)
            contador += 1
            actuador_agente(eleccion_agente)

    else:
        messagebox.showerror("triqui", "Casilla previamente seleccionada\n")


def reset_botones():

    global boton_1,boton_2,boton_3,boton_4,boton_5,boton_6,boton_7,boton_8,boton_9
    global clicked, contador
    clicked = True
    contador = 0

    global tablero = [None]*9

    for i in range(9):
        tablero[i] = Button(ventana, text = " ",font =("Helvetica",20),height = 3, width = 6, bg = "Silver", command = lambda: b_click(tablero[i]))


    #grid o malla

    for i in range(3):
        for j in range(3):
            tablero[((i*3)+j)].grid(row = i,column = j)

    if jugador_1 == "agente":
        eleccion_agente = programa_agente(contador)
        contador += 1
        actuador_agente(eleccion_agente)
        


#Menu


menu_principal = Menu(ventana)
ventana.config(menu = menu_principal)

#Opciones para el menu


opciones_menu  = Menu(menu_principal,tearoff = False)
menu_principal.add_cascade(label = "Opciones", menu = opciones_menu)
opciones_menu.add_command(label="Reset", command = reset_botones)


reset_botones()
ventana.mainloop()
print("Programa ejecutado")
