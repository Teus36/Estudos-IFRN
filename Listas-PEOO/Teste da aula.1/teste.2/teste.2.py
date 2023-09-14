from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
<<<<<<< Updated upstream:Listas-PEOO/Teste da aula.1/teste.2/teste.2.py
        self.janela.title("Teste.2")
        self.janela.geometry("1200x800")

=======
        self.janela.geometry('350x200')
        self.janela.title('Concatenando Strings')
>>>>>>> Stashed changes:Listas-PEOO/Teste da aula.1/teste.2.py

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.texto1 = Label(self.frame1, text='Nome: ')
        self.texto1.pack(side = 'left', pady=10)

        self.caixa1 = Entry(self.frame1)
        self.caixa1.pack(side = 'left', pady=10)

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        self.texto2 = Label(self.frame2, text='Telefone: ')
        self.texto2.pack(side = 'left', pady=5)

        self.caixa2 = Entry(self.frame2)
        self.caixa2.pack(side = 'left', pady=5)

        self.frame3 = Frame(self.janela)
        self.frame3.pack()

        self.botaoInserir = Button(self.frame3, text='Inserir', command=self.concatenar)
        self.botaoInserir.pack(pady=5)

        self.frame4 = Frame(self.janela)
        self.frame4.pack()

        self.textoResultado = Label(self.frame4, text='Concatenação')
        self.textoResultado['bg']='black'
        self.textoResultado['fg']='yellow'        
        self.textoResultado.pack(pady=10)

        self.janela.mainloop()

    def concatenar(self):
        self.textoResultado['text'] = self.caixa1.get()+self.caixa2.get()
    
aplicacao=App()