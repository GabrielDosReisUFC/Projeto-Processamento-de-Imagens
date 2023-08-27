from tkinter import *
from tkinter import simpledialog
from PIL import Image, ImageTk

class Apli:   

    def __init__(self, master=None):
        self.root = root
        inicio_label = Label(root,text="Inicio")
        inicio_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")

        fim_label = Label(root,text="Fim")
        fim_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")

        inicio_entrada = Entry(root)
        inicio_entrada.grid(row=0, column=1, padx=10, pady=5)

        fim_entrada = Entry(root)
        fim_entrada.grid(row=1, column=1, padx=10, pady=5)

        botao = Button(root, text="Aplicar", command=lambda:self.aplicar())
        botao.grid(row=2, columnspan=2, pady=10)

        self.vetor_normal = [0]*256
        self.vetor_modificado = [0]*256
        self.a = 1
        self.b = 1

        for i in range(0,256):
            self.vetor_normal = i
            self.vetor_modificado = i
            
    def funcao(self,a,b):
        self.a = a
        self.b = b

    def aplicar(self):
        path = "te.tif"
        imagem = Image.open(path)
        dados_imagem = imagem.load()
        for linha in range(imagem.height):
            for coluna in range(imagem.width):
                if round(dados_imagem[coluna, linha]) < 20:
                    dados_imagem[coluna, linha] =  round(0.5*dados_imagem[coluna, linha])
                
        imagem.show()
        #img = ImageTk.PhotoImage(imagem)
        

root = Tk()
Apli(root)
root.mainloop()      
