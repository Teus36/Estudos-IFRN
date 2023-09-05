from tkinter import *

class app:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Janela legal")
        self.janela.geometry("1200x800")


        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.texto1 = Label(
            self.frame1,
            text='Nome'
        )
        self.texto1.pack(side='left')

        self.texto2 = Label(
            self.frame1,
            text='Senha'
        )
        self.texto2.pack()

        self.caixa1= Entry(self.frame1)
        self.caixa1.pack()

        self.caixa2= Entry(self.frame1)
        self.caixa2.pack()

        self.janela.mainloop()


aplicar = app()
    