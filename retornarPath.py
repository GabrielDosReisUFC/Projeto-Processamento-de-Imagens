import os 
def path(string,img):
    path = os.getcwd() + "\modificado.tif"
    img.save(path)
    img.close()
    return path

