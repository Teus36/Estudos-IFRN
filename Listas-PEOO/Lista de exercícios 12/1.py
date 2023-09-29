from tkinter import *

class App():
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Calculadora aprimorada")
        self.janela.geometry("320x280")

        self.canvas1 = Canvas(
            self.janela,
            bg='gray',
            height='280',
            width='320',
            )
        self.canvas1.pack()
        
        self.label1 = Label(
            self.janela,
            text='0.00',
            bg='white',
            height='2',
            width='12',
            anchor='e',
            font=('Arial', 24)
        )
        self.label1.pack()
        self.label1.place(x=75, y=10)
        
        self.imagem1 = PhotoImage(file='logo_ifrn_01.png').subsample(14)
        self.canvas1.create_image(40, 50, image=self.imagem1, tags='logo_IF')
        self.canvas1.create_text(280, 260, text='Lista 12', font=('Arial', 13), fill='white')
        self.canvas1.tag_bind('logo_IF','<Button-1>', self.mudar_cor)

        self.botao1 = Button(
            self.janela, 
            text='7',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_7
        )
        self.botao1.pack()
        self.botao1.place(x=10, y=110)

        self.botao2 = Button(
            self.janela, 
            text='8',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_8
        )
        self.botao2.pack()
        self.botao2.place(x=70, y=110)

        self.botao3 = Button(
            self.janela, 
            text='9',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_9
        )
        self.botao3.pack()
        self.botao3.place(x=130, y=110)

        self.botao4 = Button(
            self.janela,
            text='+',
            width='6',
            border='2',
            command=self.operacao_soma
        )
        self.botao4.pack()
        self.botao4.place(x=190, y=110)

        self.botao5 = Button(
            self.janela,
            text='←',
            bg='red',
            width='7',
            border='2',
            command=self.backspace
        )
        self.botao5.pack()
        self.botao5.place(x=250, y=110)

        self.botao6 = Button(
            self.janela, 
            text='4',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_4

        )
        self.botao6.pack()
        self.botao6.place(x=10, y=145)

        self.botao7 = Button(
            self.janela, 
            text='5',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_5
        )
        self.botao7.pack()
        self.botao7.place(x=70, y=145)

        self.botao8 = Button(
            self.janela, 
            text='6',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_6
        )
        self.botao8.pack()
        self.botao8.place(x=130, y=145)

        self.botao9 = Button(
            self.janela,
            text='-',
            width='6',
            border='2',
            command=self.operacao_subtracao
        )
        self.botao9.pack()
        self.botao9.place(x=190, y=145)

        self.botao10 = Button(
            self.janela, 
            text='1',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_1
        )
        self.botao10.pack()
        self.botao10.place(x=10, y=180)

        self.botao11 = Button(
            self.janela, 
            text='2',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_2
        )
        self.botao11.pack()
        self.botao11.place(x=70, y=180)

        self.botao12 = Button(
            self.janela, 
            text='3',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_3
        )
        self.botao12.pack()
        self.botao12.place(x=130, y=180)

        self.botao13 = Button(
            self.janela,
            text='/',
            width='6',
            border='2',
            command=self.operacao_divisao
        )
        self.botao13.pack()
        self.botao13.place(x=190, y=180)

        self.botao14 = Button(
            self.janela,
            text='0',
            width='6',
            border='2',
            bg='lightgray',
            command=self.digitar_0
        )
        self.botao14.pack()
        self.botao14.place(x=10, y=215)

        self.botao15 = Button(
            self.janela,
            text='.',
            width='6',
            border='2',
            bg='lightgray',
            command=self.ponto
            )
        self.botao15.pack()
        self.botao15.place(x=70, y=215)

        self.botao16 = Button(
            self.janela,
            text='C',
            width='6',
            border='2',
            bg='yellow',
            command=self.clear
            )
        self.botao16.pack()
        self.botao16.place(x=130, y=215)

        self.botao17 = Button(
            self.janela,
            text='*',
            width='6',
            border='2',
            command=self.operacao_multiplicacao
        )
        self.botao17.pack()
        self.botao17.place(x=190, y=215)

        self.botao18 = Button(
            self.janela,
            text='=',
            width='7',
            height='6',
            border='2',
            bg='black',
            fg='white',
            command=self.calcular
        )
        self.botao18.pack()
        self.botao18.place(x=250, y=140)

        self.numero_atual = '0.00'
        self.primeiro_numero = None
        self.operacao = ''

        self.janela.mainloop()

    def digitar_0(self):
        self.digitar('0')

    def digitar_1(self):
        self.digitar('1')

    def digitar_2(self):
        self.digitar('2')

    def digitar_3(self):
        self.digitar('3')

    def digitar_4(self):
        self.digitar('4')

    def digitar_5(self):
        self.digitar('5')

    def digitar_6(self):
        self.digitar('6')

    def digitar_7(self):
        self.digitar('7')

    def digitar_8(self):
        self.digitar('8')

    def digitar_9(self):
        self.digitar('9')

    def digitar(self, numero):
        if self.numero_atual == '0.00':
            self.numero_atual = numero
        else:
            self.numero_atual = self.numero_atual + numero
        self.label1.config(text=self.numero_atual)

    def operacao_soma(self):
        self.primeiro_numero = self.numero_atual
        self.operacao = '+'
        self.clear()

    def operacao_subtracao(self):
        self.primeiro_numero = self.numero_atual
        self.operacao = '-'
        self.clear()

    def operacao_divisao(self):
        self.primeiro_numero = self.numero_atual
        self.operacao = '/'
        self.clear()

    def operacao_multiplicacao(self):
        self.primeiro_numero = self.numero_atual 
        self.operacao = '*'
        self.clear()
    
    def calcular(self):
            if self.operacao == '+':
                resultado = float(self.primeiro_numero) + float(self.numero_atual)
                self.numero_atual = resultado
                self.label1.config(text=self.numero_atual)
            elif self.operacao == '-':
                resultado = float(self.primeiro_numero) - float(self.numero_atual)
                self.numero_atual = resultado
                self.label1.config(text=self.numero_atual)
            elif self.operacao == '/':
                resultado = float(self.primeiro_numero) / float(self.numero_atual)
                self.numero_atual = resultado
                self.label1.config(text=self.numero_atual)
            elif self.operacao == '*':
                resultado = float(self.primeiro_numero) * float(self.numero_atual)
                self.numero_atual = resultado
                self.label1.config(text=self.numero_atual)

    def backspace(self):
        if self.numero_atual != '0.00':
            self.numero_atual = self.numero_atual[: -1]
            self.label1.config(text=self.numero_atual)
            if len(self.numero_atual) == 0:
                self.numero_atual = '0.00'
                self.label1.config(text=self.numero_atual)

    def ponto(self):
        if '.' not in self.numero_atual:
            self.numero_atual = self.numero_atual + '.'
            self.label1.config(text=self.numero_atual)

    def clear(self):
        self.numero_atual = '0.00'
        self.label1.config(text=self.numero_atual)

    def mudar_cor(self, evento):
        cor_do_botao = self.botao18.cget('bg')
        if cor_do_botao == 'black':
            self.botao18.config(bg='#021F59')
        else:
            self.botao18.config(bg='black')


aplicar = App()