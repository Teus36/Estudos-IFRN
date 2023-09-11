from tkinter import *

class app():
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('640x635')
        self.janela.title('Teste.3')

        self.frame1 = Frame(self.janela)
        self.frame1.pack()
        
        self.foto1 = PhotoImage(file='lula_cade.png')
        
        self.imagem = Label(
            self.frame1,
            image=self.foto1,
        )
        self.imagem.pack()

        self.janela.mainloop()


aplicar = app()