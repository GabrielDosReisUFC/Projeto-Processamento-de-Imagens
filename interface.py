from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel, StringVar, Radiobutton, Button, messagebox
from PIL import Image, ImageTk
import numpy as np
import os
import matplotlib.pyplot as plt
import re
import negativo
import correcao_gamma
import transformacao_logaritmica
import histograma
import esteganografia
import limearizacao
import linear
import filtro
import conversao
import ajustes
import chroma
import rotacao_escala
import fourier
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

caminho_modificado = os.getcwd()  + "\modificado.tif"
exibindo = os.getcwd()  + "\exibindo.tif"

class Application:

    def __init__(self, master=None):
        self.root = root
        self.tela()

        self.frame_superior = Frame(self.root, background="#BC6FF1")
        self.frame_superior.pack(fill="x",side='top')
        self.bt_abrir_imagem = Button(self.frame_superior, width=10, height=1, compound="c", text="Abrir imagem", command=lambda:self.abrir_imagem())
        self.bt_abrir_imagem.pack(side='left', padx=5,pady=5)
        self.bt_salvar_imagem = Button(self.frame_superior, width=10, height=1, compound="c", text="Salvar imagem", command=lambda:self.salvar_imagem())
        self.bt_salvar_imagem.pack(side='left', padx=5,pady=5)

        self.frame_esquerdo = Frame(self.root, background="#58317F")
        self.frame_esquerdo.pack(fill='y',side="left")

        self.frame3 = Frame(self.frame_esquerdo)
        self.frame3.pack(pady=15)

        self.bt = Button(self.frame3, width=30, height=1, compound="c", text="Negativo", command=lambda:aplicar_negativo(self,self.Path_img,self.colorido))
        self.bt.grid(row=0,column=0,ipadx = 5, ipady= 5 )
        
        self.bt1 = Button(self.frame3, width=30, height=1, compound="c", text="Correção Gamma", command=lambda:aplicar_gamma(self,self.Path_img))
        self.bt1.grid(row=1,column=0,ipadx = 5, ipady= 5 )
        
        self.bt2 = Button(self.frame3, width=30, height=1, compound="c", text="Transformação Logarítmica", command=lambda:aplicar_transformacao_logaritmica(self,self.Path_img))
        self.bt2.grid(row=2,column=0,ipadx = 5, ipady= 5 )
        
        self.bt3 = Button(self.frame3, width=30, height=1, compound="c", text="Normal", command=lambda:self.normal(self.Path_img_normal))
        self.bt3.grid(row=3,column=0,ipadx = 5, ipady= 5 )
        
        self.bt4 = Button(self.frame3, width=30, height=1, compound="c", text="Histograma", command=lambda:aplicar_histograma(self,self.Path_img_normal,self.colorido))
        self.bt4.grid(row=4,column=0,ipadx = 5, ipady= 5 )
        
        self.bt6 = Button(self.frame3, width=30, height=1, compound="c", text="Limearização", command=lambda:aplicar_Limiar(self,self.Path_img))
        self.bt6.grid(row=5,column=0,ipadx = 5, ipady= 5 )
        
        self.bt7 = Button(self.frame3, width=30, height=1, compound="c", text="Aplicar Esteganografia", command=lambda:aplicar_Esteganografia(self.Path_img,self.colorido,self.text_area))
        self.bt7.grid(row=6,column=0,ipadx = 5, ipady= 5 )
        
        self.bt8 = Button(self.frame3, width=30, height=1, compound="c", text="Linear definido por partes", command=lambda:aplicar_linear(self,self.Path_img))
        self.bt8.grid(row=8,column=0,ipadx = 5, ipady= 5 )
        
        self.bt9 = Button(self.frame3, width=30, height=1, compound="c", text="Filtros", command=lambda:aplicar_filtros(self,self.Path_img,self.colorido))
        self.bt9.grid(row=9,column=0,ipadx = 5, ipady= 5 )

        self.bt10 = Button(self.frame3, width=30, height=1, compound="c", text="Escala de cinza", command=lambda:aplicar_converter_escala_cinza(self,self.Path_img,self.colorido))
        self.bt10.grid(row=10,column=0,ipadx = 5, ipady= 5 )

        self.bt11 = Button(self.frame3, width=30, height=1, compound="c", text="Ajustes", command=lambda:aplicar_ajustes(self,self.Path_img,self.colorido))
        self.bt11.grid(row=12,column=0,ipadx = 5, ipady= 5 )

        self.bt12 = Button(self.frame3, width=30, height=1, compound="c", text="Sepia", command=lambda:aplicar_sepia(self,self.Path_img,self.colorido))
        self.bt12.grid(row=13,column=0,ipadx = 5, ipady= 5 )

        self.bt13 = Button(self.frame3, width=30, height=1, compound="c", text="Chroma key", command=lambda:aplicar_chroma(self,self.Path_img,self.colorido))
        self.bt13.grid(row=14,column=0,ipadx = 5, ipady= 5 )

        self.bt14 = Button(self.frame3, width=30, height=1, compound="c", text="Rotação", command=lambda:aplicar_rotacao(self,self.Path_img))
        self.bt14.grid(row=15,column=0,ipadx = 5, ipady= 5 )

        self.bt15 = Button(self.frame3, width=30, height=1, compound="c", text="Escala", command=lambda:aplicar_escala(self,self.Path_img))
        self.bt15.grid(row=16,column=0,ipadx = 5, ipady= 5 )

        self.bt16 = Button(self.frame3, width=30, height=1, compound="c", text="Fourier", command=lambda:aplicar_fourier(self,self.Path_img))
        self.bt16.grid(row=17,column=0,ipadx = 5, ipady= 5 )

        self.frame_aux = Frame(root)
        self.frame_aux.pack(fill=BOTH,expand=True,padx=5,pady=5)
        self.text_area = Text(self.frame_aux)

        self.text_area.pack(fill=BOTH,expand=True)


        self.Path_img = None
        self.Path_img_2 = None
        self.Path_img_normal = None
        self.img = None
        self.label_img = None
        self.Top_level = None
        self.colorido = None
    
    def tela(self):
        self.root.title("Editor de Imagens")
        self.root.configure(background = "#1A1A1A")
        self.root.resizable(True,True)
        Width = 900
        height = 650
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
        imagem = Image.open(path)
        imagem.save(exibindo)
        if self.Top_level:
            self.label_img.config(image="")  # Fechar a imagem anterior
            self.img = None
        else:
            self.Top_level = Toplevel(self.root)  # Cria uma nova janela sobre a janela principal
            self.Top_level.title("Imagem")
            self.Top_level.attributes('-topmost', 1)
            imagem.save(caminho_modificado)
        imagem.close()
        imagem_exibida = Image.open(exibindo)
        if imagem_exibida.mode != 'RGB' and imagem_exibida.mode != 'HSV':
            self.colorido = False
        else:
            self.colorido = True
        self.img = ImageTk.PhotoImage(imagem_exibida)
        # self.nova_janela(self.img)
        largura,altura = imagem_exibida.size
        if largura > self.root.winfo_screenwidth() or altura > self.root.winfo_screenheight():
            imagem_exibida.show()   
            self.Top_level.destroy()
            self.Top_level = None 
        else:
            self.label_img = Label(self.Top_level, image=self.img)
            self.label_img.place(relx = 0, rely= 0)
            self.Top_level.geometry("%dx%d" % (largura,altura))
            self.Top_level.protocol("WM_DELETE_WINDOW", self.fechar_janela_toplevel)
            
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
        caminho_imagem = filedialog.askopenfilename(title="Selecione uma Imagem", filetypes=[("Imagens", "*.jpg *.png *.jpeg *.tif *.tiff *.bmp")])
        self.Path_img_normal = caminho_imagem
        if caminho_imagem:
            self.display_image(caminho_imagem)

    def salvar_imagem(self):
        if self.Path_img_normal:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("Imagens", "*.jpg *.png *.jpeg *.tif *.tiff *.bmp")])
            imagem = Image.open("modificado.tif")
            imagem.save(file_path)
        else:
            messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_negativo(tela,Path_img,colorido):
    if Path_img:
        if colorido:
            negativo.negativo_RGB(Path_img,caminho_modificado)
        else:
            negativo.inverter(Path_img,caminho_modificado)
        Application.display_image(tela,caminho_modificado)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def pergunta_gamma():
    try:
        resposta = simpledialog.askfloat("Valor","Insira o valor do gamma")
        return resposta
    except:
        return None

def aplicar_gamma(tela,Path_img):
    if Path_img:
        gamma = pergunta_gamma()
        if gamma is not None:
            resposta = correcao_gamma.gamma(Path_img,gamma,caminho_modificado)
            if resposta == True:
                Application.display_image(tela,caminho_modificado)
            else:
                messagebox.showinfo("Alerta","Erro ao aplicar o gamma")
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_transformacao_logaritmica(tela,Path_img):
    if Path_img:
        transformacao_logaritmica.transformacao_logaritmica(Path_img,caminho_modificado)
        Application.display_image(tela,caminho_modificado)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def escolha_histograma(tela,Path_img,colorido,janela,opcao):
    if colorido:
        if opcao == 1:
            histograma.histograma_rgb(Path_img)
        elif opcao == 2:
            contagem_pixel = histograma.equalizar_intensidade(Path_img,caminho_modificado)
            Application.display_image(tela,caminho_modificado)
            plt.plot(range(0,101),contagem_pixel)
            plt.show()
        else:
            messagebox.showinfo("Alerta","Escolha inválida")
    else:
        if opcao == 1:
            histograma.histograma(caminho_modificado)
        elif opcao == 2:
            contagem_pixel = histograma.histograma_equalizado(Path_img,caminho_modificado)
            Application.display_image(tela,caminho_modificado)
            plt.plot(range(0,256),contagem_pixel)
            plt.show()
        else:
            messagebox.showinfo("Alerta","Escolha inválida")
    janela.destroy()    

def aplicar_histograma(tela,Path_img,colorido):
    if Path_img:
        janela = Toplevel()
        janela.title("Selecione uma opção")
        opcao = StringVar()
        opcao1 = Radiobutton(janela, text="Histograma", variable=opcao, value="1")
        opcao2 = Radiobutton(janela, text="Equalizar por histograma", variable=opcao, value="2")

        opcao1.pack()
        opcao2.pack()

        # Botão de submissão
        botao = Button(janela, text="Selecionar", command=lambda:escolha_histograma(tela,Path_img,colorido,janela,int(opcao.get())))
        botao.pack()

    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def pergunta_limiar():
    try:
        resposta = simpledialog.askinteger("Valor","Insira o valor do Limiar")
        if resposta > 255 or resposta < 0:
            messagebox.showinfo("Alerta","Valor informado deve estar entre 0 e 255")
            return None
        return resposta
    except:
        messagebox.showinfo("Alerta","Valor informado é inválido")
        return None

def aplicar_Limiar(tela,Path_img):
    if Path_img:       
        valor = pergunta_limiar()
        if valor is not None:
            limearizacao.limearizar(Path_img,valor,caminho_modificado)
            Application.display_image(tela,caminho_modificado)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def escolha_esteganografia(Path_img,colorido,janela,opcao,text):
    if colorido:
        messagebox.showinfo("Alerta","Não é aceito nesse formato de imagem")
    else:
        if opcao == 1:
            mensagem = esteganografia.extract_and_display_message(Path_img)
            text.delete("1.0", END)
            text.insert("1.0", mensagem)
        elif opcao == 2:
            mensagem = text.get("1.0","end-1c")
            esteganografia.hide_message(Path_img,mensagem)
        else:
            messagebox.showinfo("Alerta","Escolha inválida")
    janela.destroy()    

def aplicar_Esteganografia(Path_img,colorido,text):
    if Path_img:
        janela = Toplevel()
        janela .title("Selecione uma opção")
        opcao = StringVar()
        opcao1 = Radiobutton(janela, text="Ler", variable=opcao, value="1")
        opcao2 = Radiobutton(janela, text="Escrever", variable=opcao, value="2")

        opcao1.pack()
        opcao2.pack()

        # Botão de submissão
        botao = Button(janela, text="Selecionar", command=lambda:escolha_esteganografia(Path_img,colorido,janela,int(opcao.get()),text))
        botao.pack()

    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_linear(tela,Path_img):
    if Path_img:
        linear.linearizar(Path_img,caminho_modificado)
        Application.display_image(tela,caminho_modificado)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_filtros(tela,Path_img,colorido):
    global matrix_kernel
    matrix_kernel = None
    
    def escolher_tamanho():
        resposta = simpledialog.askinteger("Valor","Insira o tamanho da matriz (máximo 9 e número quadrado impar)")
        if resposta != 3 and resposta!=5 and resposta!=7 and resposta!=9:
            messagebox.showinfo("Alerta","Valor inserido é inválido")
            return None
        else:
            return resposta

    def definir_kernel(tamanho,janela,colorido):
        matrix = []
        janela.title("Digite a Matriz")
        for i in range(tamanho):
            linha = []
            for j in range(tamanho):
                entry= ttk.Entry(janela)
                entry.grid(row=i,column=j)
                linha.append(entry)
            matrix.append(linha)
        botao = ttk.Button(janela, text="Salvar Matriz", command=lambda:enviar_conteudo_matriz(matrix,janela,colorido))
        botao.grid(row=tamanho, columnspan=tamanho)
    
    def enviar_conteudo_matriz(matrix,janela,colorido):
        global matrix_kernel
        matrix_kernel=[]
        for linha in matrix:
            valores_linhas = []
            for entry in linha:
                valor = float(entry.get())
                valores_linhas.append(valor)
            matrix_kernel.append(np.array(valores_linhas))
        janela.destroy()
        matrix_kernel = np.array(matrix_kernel)
        if colorido == False:
            filtro.convolucao(Path_img,matrix_kernel,caminho_modificado)
        else:
            filtro.convolucao_rgb(Path_img,matrix_kernel,caminho_modificado)
        Application.display_image(tela,caminho_modificado)

    def escolha(colorido):
        opcao_selecionada = opcao.get()
        if opcao_selecionada == "Generico" or opcao_selecionada == "ponderada":
            resposta = escolher_tamanho()
            if resposta != None:
                for widget in top_level.winfo_children():
                    widget.destroy()
                definir_kernel(resposta,top_level,colorido)
            else:
                top_level.destroy()
        else:
            try:
                if opcao_selecionada == "simples":
                    resposta = escolher_tamanho()                    
                    if resposta is not None:
                        filtro.convolucao_media(Path_img,resposta,caminho_modificado)
                if opcao_selecionada == "mediana":
                    resposta = escolher_tamanho()
                    if resposta is not None:
                        filtro.convoluca_mediana(Path_img,resposta,caminho_modificado)
                if opcao_selecionada == "laplaciano":
                    filtro.laplaciano(Path_img,caminho_modificado)
                if opcao_selecionada == "high":
                    filtro.high_boost(Path_img,caminho_modificado)
                if opcao_selecionada == "x":
                    img = filtro.sobel_x(Path_img)
                    img.save(caminho_modificado)
                if opcao_selecionada == "y":
                    img = filtro.sobel_y(Path_img)
                    img.save(caminho_modificado)
                if opcao_selecionada == "magnitude":
                    filtro.sobel(Path_img,caminho_modificado)
                if opcao_selecionada == "suavizacao":
                    filtro.suavizacao_rgb(Path_img,caminho_modificado)
                if opcao_selecionada == "agucamento":
                    filtro.agucamento_rgb(Path_img,caminho_modificado)
                Application.display_image(tela,caminho_modificado)
                top_level.destroy()
            except Exception as e:
                print(e)
                messagebox.showinfo("Alerta","formato inválido.")
                
    top_level = Toplevel()
    top_level .title("Selecione uma opção")
    opcao = StringVar()

    op_1 = ttk.Radiobutton(top_level, text="Filtro Genérico", variable=opcao, value="Generico")
    op_2 = ttk.Radiobutton(top_level, text="Filtro de suavização média simples", variable=opcao, value="simples")
    op_3 = ttk.Radiobutton(top_level, text="Filtro de suavização média ponderada", variable=opcao, value="ponderada")
    op_4 = ttk.Radiobutton(top_level, text="Filtro de mediana", variable=opcao, value="mediana")
    op_5 = ttk.Radiobutton(top_level, text="Filtro Laplaciano", variable=opcao, value="laplaciano")
    op_6 = ttk.Radiobutton(top_level, text="Filtro de High-Boost", variable=opcao, value="high")
    op_7 = ttk.Radiobutton(top_level, text="Filtro de Sobel x", variable=opcao, value="x")
    op_8 = ttk.Radiobutton(top_level, text="Filtro de Sobel y", variable=opcao, value="y")
    op_9 = ttk.Radiobutton(top_level, text="Filtro de bordas pelo gradiente", variable=opcao, value="magnitude")
    op_10 = ttk.Radiobutton(top_level, text="Filtro de suavização em RGB", variable=opcao, value="suavizacao")
    op_11 = ttk.Radiobutton(top_level, text="Filtro de aguçamento em RGB", variable=opcao, value="agucamento")
    op_1.pack()
    op_2.pack()
    op_3.pack()
    op_4.pack()
    op_5.pack()
    op_6.pack()
    op_7.pack()
    op_8.pack()
    op_9.pack()
    op_10.pack()
    op_11.pack()

    show_button = ttk.Button(top_level, text="Escolher", command=lambda:escolha(colorido))
    show_button.pack()

def validar_numero(numero):
    pattern = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'
    return re.match(pattern, numero)

def escolha_escala_cinza(tela,Path_img,janela,opcao):
    janela.destroy()    
    if opcao == 1:        
        conversao.converter_escala_cinza(Path_img,caminho_modificado)
        Application.display_image(tela,caminho_modificado)
    elif opcao == 2:
        conversao.converter_escala_cinza_ponderada(Path_img,caminho_modificado)
        Application.display_image(tela,caminho_modificado)

def aplicar_converter_escala_cinza(tela,Path_img,colorido):
    if Path_img:
        if not colorido:
            messagebox.showinfo("Alerta","Não é aceito nesse formato de imagem")
        else:
            janela = Toplevel()
            janela .title("Selecione uma opção")
            opcao = StringVar()
            opcao1 = Radiobutton(janela, text="simples", variable=opcao, value="1")
            opcao2 = Radiobutton(janela, text="ponderado", variable=opcao, value="2")

            opcao1.pack()
            opcao2.pack()

            botao = Button(janela, text="Selecionar", command=lambda:escolha_escala_cinza(tela,Path_img,janela,int(opcao.get())))
            botao.pack()

    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def escolha_ajutes(tela,Path_img,janela,opcao):
    janela.destroy()
    if opcao == 1:
        try:
            resposta = simpledialog.askinteger("Valor","Insira um valor de -360 a 360")
            ajustes.ajuste_matiz(Path_img,resposta,caminho_modificado)
        except:
            messagebox.showinfo("Alerta","Você deve inserir um valor válido")
    elif opcao == 2:
        try:
            resposta = simpledialog.askinteger("Valor","Insira um valor de -100 a 100")
            ajustes.ajuste_saturacao(Path_img,resposta,caminho_modificado)
        except:
            messagebox.showinfo("Alerta","Você deve inserir um valor válido")
    elif opcao == 3:
        try:
            resposta = simpledialog.askinteger("Valor","Insira um valor de -100 a 100")
            ajustes.ajuste_brilho(Path_img,resposta,caminho_modificado)
        except:
            messagebox.showinfo("Alerta","Você deve inserir um valor válido")
    elif opcao == 4:
        try:
            resposta = simpledialog.askinteger("Valor","Insira um valor de -255 a 255")
            ajustes.ajuste_R(Path_img,resposta,caminho_modificado)
        except:
            messagebox.showinfo("Alerta","Você deve inserir um valor válido")
    elif opcao == 5:
        try:
            resposta = simpledialog.askinteger("Valor","Insira um valor de -255 a 255")
            ajustes.ajuste_G(Path_img,resposta,caminho_modificado)
        except:
            messagebox.showinfo("Alerta","Você deve inserir um valor válido")
    elif opcao == 6:
        try:
            resposta = simpledialog.askinteger("Valor","Insira um valor de -255 a 255")
            ajustes.ajuste_B(Path_img,resposta,caminho_modificado)
        except:
            messagebox.showinfo("Alerta","Você deve inserir um valor válido")
    Application.display_image(tela,caminho_modificado)


def aplicar_ajustes(tela,Path_img,colorido):
    if Path_img:
        if colorido:
            janela = Toplevel()
            janela .title("Selecione uma opção")
            opcao = StringVar()
            opcao1 = Radiobutton(janela, text="ajuste matiz", variable=opcao, value="1")
            opcao2 = Radiobutton(janela, text="ajuste saturação", variable=opcao, value="2")
            opcao3 = Radiobutton(janela, text="ajuste brilho", variable=opcao, value="3")
            opcao4 = Radiobutton(janela, text="ajuste canal R", variable=opcao, value="4")
            opcao5 = Radiobutton(janela, text="ajuste canal G", variable=opcao, value="5")
            opcao6 = Radiobutton(janela, text="ajuste canal B", variable=opcao, value="6")

            opcao1.pack()
            opcao2.pack()
            opcao3.pack()
            opcao4.pack()
            opcao5.pack()
            opcao6.pack()

            # Botão de submissão
            botao = Button(janela, text="Selecionar", command=lambda:escolha_ajutes(tela,Path_img,janela,int(opcao.get())))
            botao.pack()
        else:
            messagebox.showinfo("Alerta","Formato de imagem inválido")
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_chroma(tela,Path_img,colorido):
    if Path_img:
        if colorido:
            valor = pergunta_limiar()   
            imgfundo = filedialog.askopenfilename(title="Selecione uma Imagem para background", filetypes=[("Imagens", "*.jpg *.png *.jpeg *.tif *.tiff *.bmp")])
            chroma.chromakey(Path_img, imgfundo, valor,caminho_modificado)
            Application.display_image(tela,caminho_modificado)
        else:
            messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")   
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_sepia(tela,Path_img,colorido):
    if Path_img:
        if not colorido:
            messagebox.showinfo("Alerta","Formato inválido")
        else:
            conversao.converter_sepia(Path_img,caminho_modificado)
            Application.display_image(tela,caminho_modificado)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def aplicar_rotacao(tela,Path_img):
    if Path_img:
        resposta = simpledialog.askinteger("Valor","Insira o valor do ângulo")
        rotacao_escala.rotacao(Path_img,resposta,caminho_modificado)
        Application.display_image(tela,caminho_modificado)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

#Aplicar escala: menu para escolher linear ou nearest neighbour

def escolha_escala(tela,Path_img,janela,opcao):
    janela.destroy()
    if opcao == 1:
        # try:
        resposta = simpledialog.askinteger("Valor","Insira um valor de escala")
        rotacao_escala.interpolacao_nn(Path_img,resposta,caminho_modificado)
        # except:
            # messagebox.showinfo("Alerta","Você deve inserir um valor válido")
    elif opcao == 2:
        try:
            resposta = simpledialog.askinteger("Valor","Insira um valor de escala")
            rotacao_escala.interpolacao_lin(Path_img,resposta,caminho_modificado)
        except:
            messagebox.showinfo("Alerta","Você deve inserir um valor válido")

def aplicar_escala(tela,Path_img):
    if Path_img:
        janela = Toplevel()
        janela .title("Selecione uma opção")
        opcao = StringVar()
        opcao1 = Radiobutton(janela, text="Vizinho mais próximo", variable=opcao, value="1")
        opcao2 = Radiobutton(janela, text="Linear", variable=opcao, value="2")
        opcao1.pack()
        opcao2.pack()
        botao = Button(janela, text="Selecionar", command=lambda:escolha_escala(tela,Path_img,janela,int(opcao.get())))
        botao.pack()
        Application.display_image(tela,caminho_modificado)
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")

def escolher_fourier(Path_img,janela,opcao):
    janela.destroy()
    if opcao == 1:
        fourier.DFT2D(Path_img,caminho_modificado)
    elif opcao == 2:
        fourier.FFT(Path_img,caminho_modificado)

#Aplicar Fourier: rápida ou ingênua
def aplicar_fourier(tela,Path_img):
    if Path_img:
        janela = Toplevel()
        janela .title("Selecione uma opção")
        opcao = StringVar()
        opcao1 = Radiobutton(janela, text="Transformada discreta", variable=opcao, value="1")
        opcao2 = Radiobutton(janela, text="Transformada rápida", variable=opcao, value="2")
        opcao1.pack()
        opcao2.pack()
        botao = Button(janela, text="Selecionar", command=lambda:escolher_fourier(Path_img,janela,int(opcao.get())))
        botao.pack()
        Application.display_image(tela,caminho_modificado)
        canvas = FigureCanvasTkAgg(Figure(figsize=(6, 4)), master=tela)
        canvas.get_tk_widget().pack()
        fourier.edit_spectrum_with_brush(caminho_modificado, canvas)
        magnitude_spectrum = np.abs(F)
        plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
        def edit_spectrum_with_brush(img, canvas):
            imagem = plt.imread(img)
            F = np.array(imagem)
            def edit(event):
                x, y = int(event.xdata), int(event.ydata)
                radius = 5  # Tamanho do pincel
                mask = np.zeros(F.shape)
                for i in range(x - radius, x + radius + 1):
                    for j in range(y - radius, y + radius + 1):
                        if 0 <= i < F.shape[1] and 0 <= j < F.shape[0]:
                            mask[j, i] = 1  # Define os pontos dentro do raio do pincel como 1
                            F *= (1 - mask)  # Inverte os pontos clicados de preto para branco

            canvas.figure.clf()
            magnitude_spectrum = np.abs(F)
            plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
            plt.title('Espectro')
            plt.colorbar()
            plt.show()
            canvas.draw()
            modified_F = F  
            filtered_image = fourier.IDFT2D(modified_F)  
    else:
        messagebox.showinfo("Alerta","Você deve abrir uma imagem primeiro")
    
#main
root = Tk()
Application(root)
root.mainloop()