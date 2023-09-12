from tkinter import *
from PIL import ImageTk, Image

class app:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("500x300")
        self.janela.title("Teste.5")
        
        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.imagemOriginal = Image.open('indo_ali.jfif')
        self.imagemAlteracao = self.imagemOriginal.resize((1280,720))
        self.imagemCarregada = ImageTk.PhotoImage(self.imagemAlteracao)

        self.imagem = Label(self.frame1, image=self.imagemCarregada)
        self.imagem.pack()

        self.janela.mainloop()

janela = app()