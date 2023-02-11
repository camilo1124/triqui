#Importar librerias necesarias

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title('Juego triqui')

#Empieza X
clicked = True
contador = 0


#Desactiva todos los botones
def desactivacion_botones():

    boton_1.config(state = DISABLED)
    boton_2.config(state = DISABLED)
    boton_3.config(state = DISABLED)
    boton_4.config(state = DISABLED)
    boton_5.config(state = DISABLED)
    boton_6.config(state = DISABLED)
    boton_7.config(state = DISABLED)
    boton_8.config(state = DISABLED)
    boton_9.config(state = DISABLED)


#Revisa si en el tablero ha ganado un jugador

def victoria():
    
    global winner 
    ganador = False 

    #Revision para las X's

    if boton_1["text"] == "X" and  boton_2["text"] == "X" and boton_3["text"] == "X":
        boton_1.config(bg="green")
        boton_2.config(bg="green")
        boton_3.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "X gana")
        desactivacion_botones()
    elif boton_4["text"] == "X" and  boton_5["text"] == "X" and boton_6["text"] == "X":
        boton_4.config(bg="green")
        boton_5.config(bg="green")
        boton_6.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "X gana")
        desactivacion_botones()
    elif boton_7["text"] == "X" and  boton_8["text"] == "X" and boton_9["text"] == "X":
        boton_7.config(bg="green")
        boton_8.config(bg="green")
        boton_9.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "X gana")
        desactivacion_botones()
    elif boton_1["text"] == "X" and  boton_4["text"] == "X" and boton_7["text"] == "X":
        boton_1.config(bg="green")
        boton_4.config(bg="green")
        boton_7.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "X gana")
        desactivacion_botones()

    elif boton_2["text"] == "X" and  boton_5["text"] == "X" and boton_8["text"] == "X":
        boton_2.config(bg="green")
        boton_5.config(bg="green")
        boton_8.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "X gana")
        desactivacion_botones()

    elif boton_3["text"] == "X" and  boton_6["text"] == "X" and boton_9["text"] == "X":
        boton_3.config(bg="green")
        boton_6.config(bg="green")
        boton_9.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "X gana")
        desactivacion_botones()

    elif boton_1["text"] == "X" and  boton_5["text"] == "X" and boton_9["text"] == "X":
        boton_1.config(bg="green")
        boton_5.config(bg="green")
        boton_9.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "X gana")
        desactivacion_botones()

    elif boton_7["text"] == "X" and  boton_5["text"] == "X" and boton_3["text"] == "X":
        boton_7.config(bg="green")
        boton_5.config(bg="green")
        boton_3.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "X gana")
        desactivacion_botones()

    # Revision para las O's

    if boton_1["text"] == "O" and  boton_2["text"] == "O" and boton_3["text"] == "O":
        boton_1.config(bg="green")
        boton_2.config(bg="green")
        boton_3.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "O gana")
    elif boton_4["text"] == "O" and  boton_5["text"] == "O" and boton_6["text"] == "O":
        boton_4.config(bg="green")
        boton_5.config(bg="green")
        boton_6.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "O gana")
        desactivacion_botones()
    elif boton_7["text"] == "O" and  boton_8["text"] == "O" and boton_9["text"] == "O":
        boton_7.config(bg="green")
        boton_8.config(bg="green")
        boton_9.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "O gana")
        desactivacion_botones()
    elif boton_1["text"] == "O" and  boton_4["text"] == "O" and boton_7["text"] == "O":
        boton_1.config(bg="green")
        boton_4.config(bg="green")
        boton_7.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "O gana")
        desactivacion_botones()

    elif boton_2["text"] == "O" and  boton_5["text"] == "O" and boton_8["text"] == "O":
        boton_2.config(bg="green")
        boton_5.config(bg="green")
        boton_8.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "O gana")
        desactivacion_botones()

    elif boton_3["text"] == "O" and  boton_6["text"] == "O" and boton_9["text"] == "O":
        boton_3.config(bg="green")
        boton_6.config(bg="green")
        boton_9.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "O gana")
        desactivacion_botones()

    elif boton_1["text"] == "O" and  boton_5["text"] == "O" and boton_9["text"] == "O":
        boton_1.config(bg="green")
        boton_5.config(bg="green")
        boton_9.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "O gana")
        desactivacion_botones()

    elif boton_7["text"] == "O" and  boton_5["text"] == "O" and boton_3["text"] == "O":
        boton_7.config(bg="green")
        boton_5.config(bg="green")
        boton_3.config(bg="green")

        ganador = True 

        messagebox.showinfo("Tic Tac Toe", "O gana")
        desactivacion_botones()

#Estimulo? percepcion? generada por el ambiente

def b_click(boton):
    global clicked, contador

    if boton["text"] == " " and clicked == True:
        boton["text"] = "X"
        clicked = False
        contador += 1
        victoria()
    elif boton["text"] == " " and clicked == False:
        boton["text"] = "O"
        clicked = True
        contador += 1
        victoria()
    else:
        messagebox.showerror("triqui", "Casilla previamente seleccionada\n")


def reset():

    global boton_1,boton_2,boton_3,boton_4,boton_5,boton_6,boton_7,boton_8,boton_9
    global clicked, contador
    clicked = True
    count = 0

    boton_1 = Button(ventana, text = " ",font = ("Helvetica", 20), height = 3, width = 6,
                     bg = "Silver", command =lambda: b_click(boton_1))
    boton_2 = Button(ventana, text = " ",font = ("Helvetica", 20), height = 3, width = 6,
                     bg = "Silver", command =lambda: b_click(boton_2))
    boton_3 = Button(ventana, text = " ",font = ("Helvetica", 20), height = 3, width = 6,
                     bg = "Silver", command =lambda: b_click(boton_3))
    boton_4 = Button(ventana, text = " ",font = ("Helvetica", 20), height = 3, width = 6,
                     bg = "Silver", command =lambda: b_click(boton_4))
    boton_5 = Button(ventana, text = " ",font = ("Helvetica", 20), height = 3, width = 6,
                     bg = "Silver", command =lambda: b_click(boton_5))
    boton_6 = Button(ventana, text = " ",font = ("Helvetica", 20), height = 3, width = 6,
                     bg = "Silver", command =lambda: b_click(boton_6))
    boton_7 = Button(ventana, text = " ",font = ("Helvetica", 20), height = 3, width = 6,
                     bg = "Silver", command =lambda: b_click(boton_7))
    boton_8 = Button(ventana, text = " ",font = ("Helvetica", 20), height = 3, width = 6,
                     bg = "Silver", command =lambda: b_click(boton_8))
    boton_9 = Button(ventana, text = " ",font = ("Helvetica", 20), height = 3, width = 6,
                     bg = "Silver", command =lambda: b_click(boton_9))

    #grid o malla

    boton_1.grid(row = 0, column = 0)
    boton_2.grid(row = 0, column = 1)
    boton_3.grid(row = 0, column = 2)

    boton_4.grid(row = 1, column = 0)
    boton_5.grid(row = 1, column = 1)
    boton_6.grid(row = 1, column = 2)

    boton_7.grid(row = 2, column = 0)
    boton_8.grid(row = 2, column = 1)
    boton_9.grid(row = 2, column = 2)

#Menu


menu_principal = Menu(ventana)
ventana.config(menu = menu_principal)

#Opciones para el menu


opciones_menu  = Menu(menu_principal,tearoff = False)
menu_principal.add_cascade(label = "Opciones", menu = opciones_menu)
opciones_menu.add_command(label="Reset", command = reset)


reset()
ventana.mainloop()
print("Programa ejecutado")
