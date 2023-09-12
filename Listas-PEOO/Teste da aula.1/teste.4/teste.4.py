from tkinter import *

class app:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('500x300')
        self.janela.title('Teste.4')


        self.frame1 = Frame(self.janela)
        self.frame1.pack()
        
        self.foto1 = PhotoImage(file='btn_ok.png')
        self.foto2 = PhotoImage(file='btn_cancel.png')
        
        self.botao1 = Button(
            self.frame1,
            image=self.foto1,
            text='Ok',
            compound='left',
            width='80'
            )
        self.botao1.pack(side='left')
        
        self.botao2 = Button(
            self.frame1,
            image=self.foto2,
            text='Cancelar',
            compound='left',
            width='80'
            )
        self.botao2.pack(side='right')

        self.janela.mainloop()


aplicar = app()