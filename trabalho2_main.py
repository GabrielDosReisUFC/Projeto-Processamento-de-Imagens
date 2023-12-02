import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import wavelet
import huffman
import codificacao_preditiva

class JanelaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manipulação de Imagens")
        
        # Variáveis
        self.nome_arquivo = tk.StringVar()
        self.tamanho_arquivo = tk.StringVar()
        
        # Rótulos
        self.label_nome = tk.Label(root, text="Nome do Arquivo Original:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.label_tamanho = tk.Label(root, text="Tamanho do Arquivo Original:")
        self.label_tamanho.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)

        # Entradas de texto (somente leitura)
        self.entry_nome = tk.Entry(root, textvariable=self.nome_arquivo)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky=tk.W+tk.E)

        self.entry_tamanho = tk.Entry(root, textvariable=self.tamanho_arquivo, state='readonly')
        self.entry_tamanho.grid(row=0, column=4, padx=10, pady=5, columnspan=2, sticky=tk.W+tk.E)
       
        self.nome_arquivo_novo = tk.StringVar()
        self.tamanho_arquivo_novo = tk.StringVar()

        # Rótulos
        self.label_nome_novo = tk.Label(root, text="Nome do Novo Arquivo:")
        self.label_nome_novo.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.label_tamanho_novo = tk.Label(root, text="Tamanho do Novo Arquivo:")
        self.label_tamanho_novo.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)

        # Entradas de texto
        self.entry_nome_novo = tk.Entry(root, textvariable=self.nome_arquivo_novo   )
        self.entry_nome_novo.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky=tk.W+tk.E)

        self.entry_tamanho_novo = tk.Entry(root, textvariable=self.tamanho_arquivo_novo, state='readonly')
        self.entry_tamanho_novo.grid(row=1, column=4, padx=10, pady=5, columnspan=2, sticky=tk.W+tk.E)

        # Botão para abrir imagem
        self.btn_abrir = tk.Button(root, text="Abrir Imagem", command=self.abrir_imagem)
        self.btn_abrir.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        # Botões para compactar e descompactar (funcionalidades futuras)
        self.btn_compactar = tk.Button(root, text="Compactar", command=self.compactar)
        self.btn_compactar.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        self.btn_descompactar = tk.Button(root, text="Descompactar", command=self.descompactar)
        self.btn_descompactar.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)

    def abrir_imagem(self):
        # Abrir diálogo para selecionar arquivo
        filepath = filedialog.askopenfilename(filetypes=[
            ("Imagens", "*.png;*.jpg;*.jpeg;*.tif;*.bmp"),
            ("Todos os Arquivos", "*.*")
        ])

        # Atualizar variáveis e campos de texto
        if filepath:
            self.nome_arquivo.set(os.path.basename(filepath))
            self.tamanho_arquivo.set(f"{os.path.getsize(filepath)//1024} kbytes")

    def validar(self):
        self.tamanho_arquivo.set(f"{os.path.getsize(self.nome_arquivo.get())//1024} kbytes")
        if not self.nome_arquivo.get().strip():
            messagebox.showwarning("Aviso", "O campo nome arquivo original está vazio. Abre uma imagem primeiro")
            return False
        elif not self.nome_arquivo_novo.get().strip():
            messagebox.showwarning("Aviso", "O campo nome arquivo novo está vazio.")
            return False
        return True
        
    def compactar(self):
        valido = self.validar()
        if valido:
            compressed_img = wavelet.compress(self.nome_arquivo.get())
            encoded_data = codificacao_preditiva.predictive_coding_encode(compressed_img)
            huffman.compress_array(encoded_data,self.nome_arquivo_novo.get()+".grl")
            self.nome_arquivo_novo.set(os.path.basename(self.nome_arquivo_novo.get()))
            self.tamanho_arquivo_novo.set(f"{os.path.getsize(self.nome_arquivo_novo.get()+'.grl')//1024} kbytes")

    def descompactar(self):
        valido = self.validar()
        if valido:
            imagem_codificada =huffman.decompress_image(self.nome_arquivo.get())
            codificacao_preditiva.decodificacao_preditiva(imagem_codificada,self.nome_arquivo_novo.get()+".bmp")
            #waveletbenchmark.decompress_image(self.nome_arquivo_novo.get()+".bmp")
            self.nome_arquivo_novo.set(os.path.basename(self.nome_arquivo_novo.get()))
            self.tamanho_arquivo_novo.set(f"{os.path.getsize(self.nome_arquivo_novo.get()+'.bmp')//1024} kbytes")

# Criar a janela principal
root = tk.Tk()
app = JanelaApp(root)

# Iniciar o loop de eventos
root.mainloop()
