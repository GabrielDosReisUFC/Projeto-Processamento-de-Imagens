from PIL import Image
import numpy as np

def chromakey(path,path2,valor,salvar):
    img = Image.open(path)
    img2 = Image.open(path2)

    img_array = np.array(img)
    img_array2 = np.array(img2)

    for i in range(img.height):
        for j in range(img.width):
            r,g,b = img_array[i,j]
            if g < 255-valor:
              # print(g)
              if i < img2.height and j < img2.width:
                  img_array[i,j] = img_array2[i,j]

    img_final = Image.fromarray(img_array)
    img_final.save(salvar)
    


