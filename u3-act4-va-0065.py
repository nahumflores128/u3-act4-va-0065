# ==============================================================================
# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2  # Importa OpenCV para procesamiento de imágenes.
import numpy as np  # Importa NumPy para manejar matrices.
import sys  # Permite detener el programa si ocurre un error.
import win32gui
import win32con
import win32api

print("-+-+-+-+-Nahum Flores 0065 -+-+-+-+")

# ==============================================================================
# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES")

nombre_ventana = "Gpo 3H patricio nahum flores 0065"
img = cv2.imread('patricio.png')

if img is None:
    print("Error: No se pudo leer 'patricio.png'. Revisa el nombre y ubicación.")
    sys.exit()
else:
    print("Imagen cargada exitosamente.")

# ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN")

height, width, channels = img.shape

print(f"Dimensiones de la imagen: {width}x{height} píxeles")
print(f"Número de canales de color: {channels}")
print(f"Tipo de dato de la imagen: {img.dtype}")
print(f"Total de datos/píxeles: {img.size}")

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL")
print("Presiona cualquier tecla sobre la ventana para continuar...")

cv2.imshow('Imagen Original - Patricio', img)
cv2.waitKey(0)

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")

pixel_img = img.copy()

y, x = 100, 150

if y >= height or x >= width:
    print("Error: Las coordenadas están fuera de la imagen.")
    sys.exit()

pixel = pixel_img[y, x]

print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")

pixel_img[y, x] = [0, 0, 255]  # Cambia el píxel a rojo puro
cv2.circle(pixel_img, (x, y), 20, (255, 0, 0), 3)  # Dibuja un círculo azul visible alrededor del píxel

cv2.imshow('Pixel Modificado - Rojo', pixel_img)
cv2.waitKey(0)

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI - REGION OF INTEREST)
# ==============================================================================
print("\n5. REGIÓN DE INTERÉS (ROI)")

roi_img = img.copy()

roi = roi_img[50:200, 100:300]

cv2.rectangle(roi_img, (100, 50), (300, 200), (0, 255, 0), 2)

cv2.imshow('Imagen con ROI marcada', roi_img)
cv2.waitKey(0)

cv2.imshow('ROI Extraida (Recorte)', roi)
cv2.waitKey(0)

# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES DE COLOR (BGR)
# ==============================================================================
print("\n6. SEPARANDO Y FUSIONANDO CANALES")

b, g, r = cv2.split(img)

cv2.imshow('Canal Azul (Escala de grises)', b)
cv2.waitKey(0)

cv2.imshow('Canal Verde (Escala de grises)', g)
cv2.waitKey(0)

cv2.imshow('Canal Rojo (Escala de grises)', r)
cv2.waitKey(0)

zeros = np.zeros_like(b)

blue_img = cv2.merge([b, zeros, zeros])
green_img = cv2.merge([zeros, g, zeros])
red_img = cv2.merge([zeros, zeros, r])

cv2.imshow('Canal Azul (Coloreado)', blue_img)
cv2.waitKey(0)

cv2.imshow('Canal Verde (Coloreado)', green_img)
cv2.waitKey(0)

cv2.imshow('Canal Rojo (Coloreado)', red_img)
cv2.waitKey(0)

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES (RESIZING)
# ==============================================================================
print("\n7. REDIMENSIONANDO IMÁGENES")

resized_img = cv2.resize(img, (400, 300))

cv2.imshow('Redimensionada a 400x300', resized_img)
cv2.waitKey(0)

half_size = cv2.resize(img, None, fx=0.5, fy=0.5)
double_size = cv2.resize(img, None, fx=1.5, fy=1.5)

cv2.imshow('Mitad de tamano (0.5x)', half_size)
cv2.waitKey(0)

cv2.imshow('Ampliada (1.5x)', double_size)
cv2.waitKey(0)

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n8. ROTANDO IMÁGENES")

height, width = img.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D(
    (width / 2, height / 2), 45, 1
)

rotated_img = cv2.warpAffine(
    img, rotation_matrix, (width, height)
)

cv2.imshow('Imagen Rotada (45 grados)', rotated_img)
cv2.waitKey(0)

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES (FLIPPING)
# ==============================================================================
print("\n9. VOLTEANDO IMÁGENES")

horizontal_flip = cv2.flip(img, 1)

cv2.imshow('Volteo Horizontal (Espejo)', horizontal_flip)
cv2.waitKey(0)

vertical_flip = cv2.flip(img, 0)

cv2.imshow('Volteo Vertical (De cabeza)', vertical_flip)
cv2.waitKey(0)

both_flip = cv2.flip(img, -1)

cv2.imshow('Volteo en Ambos Ejes', both_flip)
cv2.waitKey(0)

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n10. GUARDANDO IMAGEN RESULTANTE")

result = cv2.imwrite('patricio_rotado.png', rotated_img)

if result:
    print("Imagen rotada guardada exitosamente como 'patricio_rotado.png'")
else:
    print("Error: No se pudo guardar la imagen rotada.")

cv2.destroyAllWindows()

print("\n¡Todas las operaciones se completaron con éxito! - Nahum Flores 0065")