import matplotlib.pyplot as plt

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
for i in range(len(points)):
    if i != 0:
        m = (points[i][1] - points[i-1][1]) / (points[i][0] - points[i-1][0])
        n = points[i][1] - m*points[i][0]
        
        if n > 0 :
            print(f'y = {m}x + {n}')
        elif n < 0 :
            print(f'y = {m}x {n}')
        else : print(f'y = {m}')
