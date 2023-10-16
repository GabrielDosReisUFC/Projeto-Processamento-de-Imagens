import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog

# Variáveis globais
current_brush_color = 0
drawing = False
spectrum = None
spectrum_view = None
spectrum_rect = None
prev_x, prev_y = 0, 0
image = None
height, width = 0, 0

def calculate_dft(image):
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)
    return f_shift

def calculate_inverse_dft(f_shift):
    f_ishift = np.fft.ifftshift(f_shift)
    image_back = np.fft.ifft2(f_ishift)
    return np.abs(image_back)

def toggle_brush_color():
    current_brush_color = 255 - current_brush_color

def draw_spectrum(event):
    x, y = event.x, event.y
    i, j = y, x

    if event.type == 'ButtonPress':
        drawing = True
        prev_x, prev_y = x, y

    if drawing and 0 <= i < height and 0 <= j < width:
        if event.type == 'Motion':
            color = current_brush_color
            spectrum[i, j] = color
            spectrum_view.itemconfig(spectrum_rect, fill='#%02x%02x%02x' % (color, color, color))

    if event.type == 'ButtonRelease':
        drawing = False

def update_image():
    global spectrum
    f_shift = np.zeros((height, width), dtype=complex)
    for i in range(height):
        for j in range(width):
            f_shift[i, j] = spectrum[i, j]

    image_back = calculate_inverse_dft(f_shift)
    image_back = cv2.normalize(image_back, None, 0, 255, cv2.NORM_MINMAX)
    image_back = np.uint8(image_back)

    cv2.imshow("Filtered Image", image_back)

root = tk.Tk()
root.title("DFT Image Editor")

file_path = filedialog.askopenfilename()
if not file_path:
    root.destroy()
    exit()

image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

height, width = image.shape
spectrum = np.zeros((height, width), dtype=np.uint8)

cv2.imshow("Original Image", image)

f_shift = calculate_dft(image)

spectrum_view = tk.Canvas(root, width=width, height=height)
spectrum_view.pack()
spectrum_rect = spectrum_view.create_rectangle(0, 0, width, height, fill="white")
spectrum_view.bind('<ButtonPress-1>', draw_spectrum)
spectrum_view.bind('<ButtonRelease-1>', draw_spectrum)
spectrum_view.bind('<B1-Motion>', draw_spectrum)
spectrum_view.bind('<ButtonPress-3>', draw_spectrum)
spectrum_view.bind('<ButtonRelease-3>', draw_spectrum)
spectrum_view.bind('<B3-Motion>', draw_spectrum)

# Botão para alternar entre pincel preto e branco
brush_color_button = tk.Button(root, text="Alternar Pincel", command=toggle_brush_color)
brush_color_button.pack()

# Botão para calcular a transformada inversa
inverse_button = tk.Button(root, text="Calcular Inversa", command=update_image)
inverse_button.pack()

root.mainloop()

cv2.waitKey(0)
cv2.destroyAllWindows()
