from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk
import negativo
import correcao_gamma
import transformcao_logaritmica
import histograma

class Application:

    def __init__(self, master=None):
        self.root = root
        self.tela()
        self.frame1 = Frame(self.root)
        self.frame1.place(relx= 0.3, rely= 0.05, relwidth= 1, relheight= 0.9)

        self.frame2 = Frame(self.root, background="#58317F")
        self.frame2.place(relx = 0, rely= 0.05, relwidth= 0.3, relheight= 0.5 )

        self.frame3 = Frame(self.frame2)
        self.frame3.pack(pady=15)

        self.bt = Button(self.frame3, width=15, height=1, compound="c", text="Negativo", command=lambda:aplicar_negativo(self,self.Path_img))
        self.bt.grid(row=0,column=0,ipadx = 5, ipady= 5 )
        
        self.bt1 = Button(self.frame3, width=15, height=1, compound="c", text="Correção Gamma", command=lambda:aplicar_gamma(self,self.Path_img))
        self.bt1.grid(row=0,column=1,ipadx = 5, ipady= 5 )
        
        self.bt2 = Button(self.frame3, width=15, height=1, compound="c", text="Transformação Logarítmica", command=lambda:aplicar_transformacao_logaritmica(self,self.Path_img))
        self.bt2.grid(row=1,column=0,ipadx = 5, ipady= 5 )
        
        self.bt3 = Button(self.frame3, width=15, height=1, compound="c", text="Nomal", command=lambda:self.normal(self.Path_img_normal))
        self.bt3.grid(row=1,column=1,ipadx = 5, ipady= 5 )
        
        self.bt4 = Button(self.frame3, width=15, height=1, compound="c", text="Histograma", command=lambda:aplicar_histograma(self.Path_img_normal))
        self.bt4.grid(row=2,column=0,ipadx = 5, ipady= 5 )
        
        self.bt5 = Button(self.frame3, width=15, height=1, compound="c", text="Equalizar por Histograma", command=lambda:aplicar_equalizar_histograma(self,self.Path_img))
        self.bt5.grid(row=2,column=1,ipadx = 5, ipady= 5 )
        
        self.bt6 = Button(self.frame3, width=15, height=1, compound="c", text="Abrir imagem", command=lambda:self.abrir_imagem())
        self.bt6.grid(row=3,column=0,ipadx = 5, ipady= 5 )

        self.Path_img = NONE
        self.Path_img_normal = NONE
        self.img = NONE
        self.label_img = Label(self.frame1,image="")

    def tela(self):
        self.root.title("Projeto andromedra")
        self.root.configure(background = "#1A1A1A")
        self.root.resizable(True,True)
        Width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (Width,height))
        
    def display_image(self,path):
        if self.img:
            self.label_img.config(image="")  # Fechar a imagem anterior
            self.img = None
        imagem = Image.open(path)
        self.img = ImageTk.PhotoImage(imagem)
        self.label_img = Label(self.frame1,image=self.img )
        self.label_img.place(relx = 0, rely= 0)
        self.Path_img = path

    def normal(self,path):
        if self.Path_img != NONE:
            self.display_image(path)
    
    def nova_janela(self):
        nova_janela = Toplevel(self.root)  # Cria uma nova janela sobre a janela principal
        nova_janela.title("Nova Janela")
        label = Label(nova_janela, text="Esta é a nova janela.")
        label.pack()
    
    def abrir_imagem(self):
        caminho_imagem = filedialog.askopenfilename(title="Selecione uma Imagem", filetypes=[("Imagens", "*.jpg *.png *.jpeg *.tif *.tiff")])
        self.Path_img_normal = caminho_imagem
        if caminho_imagem:
            self.display_image(caminho_imagem)

def aplicar_negativo(tela,Path_img):
    if Path_img != NONE:
        path = negativo.inverter(Path_img)
        Application.display_image(tela,path)
        

def pergunta():
    resposta = simpledialog.askfloat("Valor de gamma","Insira o valor de gamma")
    return resposta

def aplicar_gamma(tela,Path_img):
    if Path_img != NONE:
        gamma = pergunta()
        path = correcao_gamma.gamma(Path_img,gamma)
        Application.display_image(tela,path)

def aplicar_transformacao_logaritmica(tela,Path_img):
    if Path_img != NONE:
        path = transformcao_logaritmica.transformacao_logaritmica(Path_img)
        Application.display_image(tela,path)

def aplicar_histograma(Path_img):
    histograma.histograma(Path_img)
    

def aplicar_equalizar_histograma(tela,Path_img):
    if Path_img != NONE:
        path = histograma.histograma_equalizado(Path_img)
        Application.display_image(tela,path)

root = Tk()
Application(root)
root.mainloop()