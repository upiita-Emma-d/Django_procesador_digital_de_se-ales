from tkinter import ttk
from tkinter import *
import sqlite3

class Munitor:
    def __init__(self,window):
        self.wind = window
        self.wind.title('Monitoreo')
        # Creating a Frame Conteiner
        frame = LabelFrame(self.wind, text = 'Puerto USB')
        frame.grid(row = 0 , column = 0 , columnspan = 3, pady = 20)
        
        #SELECCION DE PUERTO
        Label(frame , text = 'PUERTO: ').grid(row = 1, column = 0)
        self.puerto = Entry(frame)
        self.puerto.focus()
        self.puerto.grid(row = 1,column = 1)
        ttk.Button(frame , text = 'Seleccionar puerto').grid(row = 4 , columnspan = 2 , sticky = W + E)
        
        ##Botones
        ttk.Button(frame , text = 'Calcular parametros').grid(row = 5 , columnspan = 2 , sticky = W + E)


if __name__ == '__main__':
    window = Tk()
    application = Munitor(window)
    window.mainloop()