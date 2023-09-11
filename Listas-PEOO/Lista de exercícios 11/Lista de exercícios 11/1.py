from tkinter import *

class app:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Janela legal")
        self.janela.geometry("200x200")


        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        self.frame3 = Frame(self.janela)
        self.frame3.pack(pady='10')

        self.frame4 = Frame(self.janela)
        self.frame4.pack()
        
        self.frame5 = Frame(self.janela)
        self.frame5.pack()

        self.texto1 = Label(
            self.frame1,
            text='Valor 1'
        )
        self.texto1.pack(side='left')

        self.texto2 = Label(
            self.frame2,
            text='Valor 2'
        )
        self.texto2.pack(side='left')

        self.caixa1= Entry(self.frame1)
        self.caixa1.pack()

        self.caixa2= Entry(self.frame2)
        self.caixa2.pack()

        self.botao1 = Button(
            self.frame3,
            command=self.somar,
            text = '+',
            width = '3',
        )
        self.botao1.pack(side='left')

        self.botao2 = Button(
            self.frame3,
            command=self.subtrair,
            text = '-',
            width = '3',
        )
        self.botao2.pack(side='left')

        self.botao3 = Button(
            self.frame3,
            command=self.multiplicar,
            text = '*',
            width = '3',
        )
        self.botao3.pack(side='left')

        self.botao4 = Button(
            self.frame3,
            command=self.dividir,
            text = '/',
            width = '3',
        )
        self.botao4.pack(side='left')

        self.botao5 = Button(
            self.frame5,
            command=self.limpar,
            text='Limpar'
        )
        self.botao5.pack(side='left')

        self.botao6 = Button(
            self.frame5,
            command=self.sair,
            text= 'Sair'
        )
        self.botao6.pack(side='left', padx='3')
    
        self.resultado = Label(self.frame4,text='Resultado')
        self.resultado['fg']= 'black'        
        self.resultado.pack(pady=15)

        self.janela.mainloop()

    def somar(self):
        if self.botao1['text'] == '+':
            self.resultado['text'] = int(self.caixa1.get()) + int(self.caixa2.get())

    def subtrair(self):
        if self.botao2['text'] == '-':
            self.resultado['text'] = int(self.caixa1.get()) - int(self.caixa2.get())

    def multiplicar(self):
        if self.botao3['text'] == '*':
            self.resultado['text'] = int(self.caixa1.get()) * int(self.caixa2.get())

    def dividir(self):
        if self.botao4['text'] == '/':
            self.resultado['text'] = int(self.caixa1.get()) / int(self.caixa2.get())

    def limpar(self):
        self.caixa1.delete(0, END)
        self.caixa2.delete(0, END)
        self.resultado['text'] = '    '

    def sair(self):
        exit()


aplicar = app()