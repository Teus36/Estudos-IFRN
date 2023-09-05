from tkinter import *

class app: 
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Janela legal")
        self.janela.geometry("1200x800")
        

        self.frame1 = Frame(
            self.janela,
            bg ='red',
            width = '1200',
            height = '800',
        )
        self.frame1.pack()

        self.texto1 = Label(
            self.frame1, 
            text = "Roberto Carlos",
            font = ('Arial', '20', 'bold'),
            bg = 'red',
            fg = 'white'
            
        )
        self.texto1.pack(side='right')

        self.botao1 = Button(
            self.frame1,
            command=self.muda,
            text = "Clique aqui",
            bg = 'lime green',
            width = 18,
            height = 2,
            font= ('Times new roman','20','bold'),
            borderwidth= 0,
        )
        self.botao1.pack(side='left')

        self.janela.mainloop()
    
    
    def muda(self):
        if self.texto1['text'] == 'Roberto Carlos':
            self.texto1['text'] = 'Ricardo Kléber'
            self.texto1['bg'] = 'blue'
            self.frame1['bg'] = 'blue'
        else:
            self.texto1['text'] = 'Roberto Carlos'
            self.texto1['bg'] = 'red'
            self.frame1['bg'] = 'red'
            


aplicar = app()