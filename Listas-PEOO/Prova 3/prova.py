from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()

        self.frame1 = Frame(self.janela)

        self.botao1 = Button(self.frame1, text='oi!', width='30', height='40')
        self.botao1.pack()

        self.janela.mainloop()

ap=App()