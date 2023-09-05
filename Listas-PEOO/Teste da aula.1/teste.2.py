from tkinter import *

class app:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Janela legal")
        self.janela.geometry("1200x800")


        self.frame1 = Frame(self.janela)
        self.frame1.pack(side='right')

        self.texto1 = Frame(
            self.frame1,
            text='Nome'
        )
        self.texto1.pack(side='left')
        
        self.janela.mainloop()


aplicar = app()
    