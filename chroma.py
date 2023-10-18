from PIL import Image
import numpy as np

def chromakey(path,path2,valor1,valor2,salvar):
    img = Image.open(path)
    img2 = Image.open(path2)
    imagem_redimensionada = img2.resize((img.width, img.height))
    img_array = np.array(img)
    img_array2 = np.array(imagem_redimensionada)

    for i in range(img.height):
        for j in range(img.width):
            r,g,b = img_array[i,j]
            r_g = int(r) - int(g) 
            b_g = int(b) - int(g)
            if r_g < 0 and b_g < 0 and valor1 <= g <= valor2 :
              if i < imagem_redimensionada.height and j < imagem_redimensionada.width:
                  img_array[i,j] = img_array2[i,j]

    img_final = Image.fromarray(img_array)
    img_final.save(salvar)
    img.close()
    img2.close()
    img_final.close()
    

