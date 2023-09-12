from tkinter import *
from PIL import ImageTk, Image

class app:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("500x300")
        self.janela.title("Teste.5")
        
        self.frame1 = Frame(self.janela)
        self.frame1.pack()
