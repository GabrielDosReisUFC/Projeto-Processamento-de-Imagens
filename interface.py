from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Canvas, Scrollbar
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import negativo
import correcao_gamma
import transformcao_logaritmica
import histograma
import nome_complicado

class Application:

    def __init__(self, master=None):
        self.root = root
        self.tela()

        self.frame_superior = Frame(self.root, background="#BC6FF1")
        self.frame_superior.pack(fill="x",side='top')
        self.bt_abrir_imagem = Button(self.frame_superior, width=10, height=1, compound="c", text="Abrir imagem", command=lambda:self.abrir_imagem())
        self.bt_abrir_imagem.pack(side='left', padx=5,pady=5)

        # self.frame1 = Frame(self.root)
        # self.frame1.place(relx= 0.181, rely= 0.037, relwidth= 1, relheight= 0.97)
        # self.frame1.pack()

        self.frame_esquerdo = Frame(self.root, background="#58317F")
        # self.frame2.place(relx = 0, rely= 0.035, relwidth= 0.3, relheight= 0.5 )
        self.frame_esquerdo.pack(fill='y',side="left")

        self.frame3 = Frame(self.frame_esquerdo)
        self.frame3.pack(pady=15)

        self.bt = Button(self.frame3, width=30, height=1, compound="c", text="Negativo", command=lambda:aplicar_negativo(self,self.Path_img))
        self.bt.grid(row=0,column=0,ipadx = 5, ipady= 5 )
        
        self.bt1 = Button(self.frame3, width=30, height=1, compound="c", text="Correção Gamma", command=lambda:aplicar_gamma(self,self.Path_img))
        self.bt1.grid(row=1,column=0,ipadx = 5, ipady= 5 )
        
        self.bt2 = Button(self.frame3, width=30, height=1, compound="c", text="Transformação Logarítmica", command=lambda:aplicar_transformacao_logaritmica(self,self.Path_img))
        self.bt2.grid(row=2,column=0,ipadx = 5, ipady= 5 )
        
        self.bt3 = Button(self.frame3, width=30, height=1, compound="c", text="Nomal", command=lambda:self.normal(self.Path_img_normal))
        self.bt3.grid(row=3,column=0,ipadx = 5, ipady= 5 )
        
        self.bt4 = Button(self.frame3, width=30, height=1, compound="c", text="Histograma", command=lambda:aplicar_histograma(self.Path_img_normal))
        self.bt4.grid(row=4,column=0,ipadx = 5, ipady= 5 )
        
        self.bt5 = Button(self.frame3, width=30, height=1, compound="c", text="Equalizar por Histograma", command=lambda:aplicar_equalizar_histograma(self,self.Path_img))
        self.bt5.grid(row=5,column=0,ipadx = 5, ipady= 5 )
        
        self.bt6 = Button(self.frame3, width=30, height=1, compound="c", text="Filtro",)
        self.bt6.grid(row=6,column=0,ipadx = 5, ipady= 5 )
        
        self.bt7 = Button(self.frame3, width=30, height=1, compound="c", text="Aplicar Esteganografia", command=lambda:aplicar_Esteganografia(self.Path_img, self.text_area))
        self.bt7.grid(row=7,column=0,ipadx = 5, ipady= 5 )
        
        self.bt7 = Button(self.frame3, width=30, height=1, compound="c", text="Ler Esteganografia", command=lambda:ler_Esteganografia(self.Path_img, self.text_area))
        self.bt7.grid(row=8,column=0,ipadx = 5, ipady= 5 )
        
        self.text_area = Text(self.root)
        # self.frame_text.pack()
        # text_area = Text(self.frame_text, wrap = WORD, height=8, width=30)
        self.text_area.pack(fill=BOTH,expand=True,padx=5,pady=5)

        # self.frame3.grid_rowconfigure(0, weight=1)
        # self.frame3.grid_columnconfigure(0, weight=1)
        # self.frame3.grid_columnconfigure(1, weight=1)

        self.Path_img = None
        self.Path_img_normal = None
        self.img = None
        self.label_img = None
        self.Top_level = None

    def tela(self):
        self.root.title("Editor de Imagens")
        self.root.configure(background = "#1A1A1A")
        self.root.resizable(True,True)
        # Width = self.root.winfo_screenwidth()
        # height = self.root.winfo_screenheight()
        Width = 800
        height = 600
        self.root.geometry("%dx%d" % (Width,height))
        self.root.resizable(False,False)
        
    def fechar_janela_toplevel(self):
        self.Top_level.destroy()
        self.Path_img = None
        self.Path_img_normal = None
        self.img = None
        self.label_img = None
        self.Top_level = None

    def display_image(self,path):
        if self.Top_level:
            self.label_img.config(image="")  # Fechar a imagem anterior
            self.img = None
        else:
            self.Top_level = Toplevel(self.root)  # Cria uma nova janela sobre a janela principal
            self.Top_level.title("Imagem")
        imagem = Image.open(path)
        self.img = ImageTk.PhotoImage(imagem)
        # self.nova_janela(self.img)
        largura,altura = imagem.size
        if largura > self.root.winfo_screenwidth() or altura > self.root.winfo_screenheight():
            imagem.show()   
            self.Top_level.destroy()
            self.Top_level = None 
        else:
            self.label_img = Label(self.Top_level, image=self.img)
            self.label_img.place(relx = 0, rely= 0)
            self.Top_level.geometry("%dx%d" % (largura,altura))
            self.Top_level.protocol("WM_DELETE_WINDOW", self.fechar_janela_toplevel)
            
            # self.label_img = Label(self.frame1,image=self.img)
            # self.label_img.place(relx = 0, rely= 0)
        
        self.Path_img = path

    def normal(self,path):
        if self.Path_img:
            self.display_image(path)
        else:
            messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

    def nova_janela(self,img):
        nova_janela = Toplevel(self.root)  # Cria uma nova janela sobre a janela principal
        nova_janela.title("Nova Janela")
        label = Label(nova_janela, image=img)
        label.pack()
    
    def abrir_imagem(self):
        caminho_imagem = filedialog.askopenfilename(title="Selecione uma Imagem", filetypes=[("Imagens", "*.jpg *.png *.jpeg *.tif *.tiff")])
        self.Path_img_normal = caminho_imagem
        if caminho_imagem:
            self.display_image(caminho_imagem)

def aplicar_negativo(tela,Path_img):
    if Path_img:
        path = negativo.inverter(Path_img)
        Application.display_image(tela,path)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")
        
def pergunta():
    resposta = simpledialog.askfloat("Valor de gamma","Insira o valor de gamma")
    return resposta

def aplicar_gamma(tela,Path_img):
    if Path_img:
        gamma = pergunta()
        path = correcao_gamma.gamma(Path_img,gamma)
        Application.display_image(tela,path)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_transformacao_logaritmica(tela,Path_img):
    if Path_img:
        path = transformcao_logaritmica.transformacao_logaritmica(Path_img)
        Application.display_image(tela,path)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_histograma(Path_img):
    if Path_img:
        histograma.histograma(Path_img)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")
    
def aplicar_equalizar_histograma(tela,Path_img):
    if Path_img:
        path,contagem_pixel = histograma.histograma_equalizado(Path_img)
        Application.display_image(tela,path)
        plt.plot(range(0,256),contagem_pixel)
        plt.show()

    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_Esteganografia(Path_img, informacoes):
    if Path_img:
        mensagem = informacoes.get("1.0","end-1c")
        nome_complicado.hide_message(Path_img,mensagem,"modificado_escondido.tif")
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def ler_Esteganografia(Path_img, text):
    if Path_img:
        mensagem = nome_complicado.extract_and_display_message(Path_img)
        text.delete("1.0", END)
        text.insert("1.0", mensagem)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

root = Tk()
Application(root)
root.mainloop()