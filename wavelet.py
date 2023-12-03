import pywt
import numpy
from PIL import Image, ImageEnhance

def max_ndarray(mat):
    return numpy.amax(mat) if type(mat).__name__ == 'ndarray' else 0

def get_image_dimensions(imagefile):             # Function to get the dimensions of the image
    with Image.open(imagefile) as img:
        width, height = img.size
    return int(width), int(height)    

def extract_rgb_coeff(img):
    (width, height) = img.size
    img = img.copy()

    mat_r = numpy.empty((width, height))
    mat_g = numpy.empty((width, height))
    mat_b = numpy.empty((width, height))

    for i in range(width):
        for j in range(height):
            (r, g, b) = img.getpixel((i, j))
            mat_r[i, j] = r
            mat_g[i, j] = g
            mat_b[i, j] = b

    coeffs_r = pywt.dwt2(mat_r, 'haar')
   
    coeffs_g = pywt.dwt2(mat_g, 'haar')
    
    coeffs_b = pywt.dwt2(mat_b, 'haar')
    
    return (coeffs_r, coeffs_g, coeffs_b)


def img_from_dwt_coeff(coeff_dwt):
    # Channel Red
    (coeffs_r, coeffs_g, coeffs_b) = coeff_dwt
    (width, height) = (len(coeffs_r[0]), len(coeffs_r[0][0]))
    cARed = numpy.array(coeffs_r[0])
    cHRed = numpy.array(coeffs_r[1][0])
    cVRed = numpy.array(coeffs_r[1][1])
    cDRed = numpy.array(coeffs_r[1][2])
    # Channel Green
    cAGreen = numpy.array(coeffs_g[0])
    cHGreen = numpy.array(coeffs_g[1][0])
    cVGreen = numpy.array(coeffs_g[1][1])
    cDGreen = numpy.array(coeffs_g[1][2])
    # Channel Blue
    cABlue = numpy.array(coeffs_b[0])
    cHBlue = numpy.array(coeffs_b[1][0])
    cVBlue = numpy.array(coeffs_b[1][1])
    cDBlue = numpy.array(coeffs_b[1][2])

    # maxValue per channel par matrix
    cAMaxRed = max_ndarray(cARed)
    cAMaxGreen = max_ndarray(cAGreen)
    cAMaxBlue = max_ndarray(cABlue)

    cHMaxRed = max_ndarray(cHRed)
    cHMaxGreen = max_ndarray(cHGreen)
    cHMaxBlue = max_ndarray(cHBlue)

    cVMaxRed = max_ndarray(cVRed)
    cVMaxGreen = max_ndarray(cVGreen)
    cVMaxBlue = max_ndarray(cVBlue)

    cDMaxRed = max_ndarray(cDRed)
    cDMaxGreen = max_ndarray(cDGreen)
    cDMaxBlue = max_ndarray(cDBlue)

    # Image object init
    dwt_img = Image.new('RGB', (width, height), (0, 0, 20))
    # cA reconstruction

    '''
    The image formed from the low frequnecy of the images which contains the main content of the image
    '''
    for i in range(width):
        for j in range(height):
            R = cARed[i][j]
            R = numpy.clip((R/cAMaxRed)*120.0,0,255)
            G = cAGreen[i][j]
            G = numpy.clip((G/cAMaxGreen)*120.0,0,255)
            B = cABlue[i][j]
            B = numpy.clip((B/cAMaxBlue)*120.0,0,255)
            new_value = (int(R), int(G), int(B))
            dwt_img.putpixel((i, j), new_value)
   
    return dwt_img


def compress(file):
    img = Image.open(file)                       # Loads the image selected
    coef = extract_rgb_coeff(img)              # Extracts the RBG Coefficients from the image 
    image = img_from_dwt_coeff(coef)           # Forms the new image using the dwt coeeficients                        # Saves the image

    '''
    Below lines of the code are to resize and enhance the images
    '''
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(2)
   
    file_enh = "enhanced.bmp"
    # image.save(file_enh)
    im = Image.open(file_enh)
    size = get_image_dimensions(file)
    # im_resized = im.resize(size)
    # im_resized.save("file_comp.bmp")
    
    return image,size

def decompress(im,size,saida):
    im_resized = im.resize(size)
    im_resized.save(saida)
    

# compress("benchmark.bmp")