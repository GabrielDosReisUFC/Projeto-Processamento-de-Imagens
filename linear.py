import matplotlib.pyplot as plt
from PIL import Image,ImageDraw
import math

def linearizar(image_path,salvar):
    # Variáveis globais para armazenar os pontos
    points = []
    points.append((0,0))

    # Função para lidar com eventos de clique do mouse
    def on_click(event):
        if event.button == 1:  # Botão esquerdo do mouse
            points.append((round(event.xdata), round(event.ydata)))
            update_plot()
        elif event.button == 3:  # Botão direito do mouse
            clear_data()

    # Função para limpar os dados
    def clear_data():
        global points
        points = []
        points.append((0,0))
        update_plot()

    # Função para atualizar o gráfico
    def update_plot():
        plt.clf()  # Limpa o gráfico anterior
        plt.xlim(0, 255)
        plt.ylim(0, 255)
        
        if len(points) > 0:
            x, y = zip(*points)
            plt.plot([0] + list(x), [0] + list(y), marker='o', linestyle='-')
        else:
            plt.plot([0, 0], [0, 0])

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Pontos e Reta')
        
        plt.draw()

    # Configuração do gráfico
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', on_click)

    update_plot()

    plt.show()

    if len(points) < 1:
        print("Gráfico vazio, desenhe para aplicar")
    else:
        ultimo_valor = points[len(points)-1]
        ultimo_valor[0] != 255
        points.append((255,255))
    dicionario = {}
    for i in range(len(points)):
        if i != 0:
            delta_y = (points[i][1] - points[i-1][1])
            delta_x = (points[i][0] - points[i-1][0])
            if delta_x != 0:
                m = delta_y/delta_x
                n = points[i][1] - m*points[i][0]
                dicionario[points[i][0]] = (m,n)

    img_aux = Image.open(image_path)
    if img_aux.mode == "RGB" or "HSV":
        imagem = Image.new('RGB',(img_aux.width,img_aux.height))
        nova_imagem = ImageDraw.Draw(imagem)
        for linha in range(img_aux.height):
            for coluna in range(img_aux.width):
                r,g,b = img_aux.getpixel((coluna,linha))

                for i in dicionario.keys():
                    if r <= i:
                        r = math.floor(r*dicionario[i][0] + dicionario[i][1])
                    if g <= i:
                        g = math.floor(g*dicionario[i][0] + dicionario[i][1])
                    if b <= i:
                        b = math.floor(b*dicionario[i][0] + dicionario[i][1])
                
                nova_imagem.point((coluna,linha),fill=(r,g,b))
            imagem.save(salvar)
    else:
        for x in range(img_aux.width):
            for y in range(img_aux.height):
                pixel = int(img_aux.getpixel((x, y)))                
                for i in dicionario.keys():
                    if pixel <= i:
                        pixel = math.floor(pixel*dicionario[i][0] + dicionario[i][1])
                # Atualize o pixel na imagem
                img_aux.putpixel((x, y), pixel)
                # Salve a imagem resultante
        img_aux.save(salvar)
        img_aux.close()
        img = Image.open(salvar)
        img.save(image_path)
        img.close()