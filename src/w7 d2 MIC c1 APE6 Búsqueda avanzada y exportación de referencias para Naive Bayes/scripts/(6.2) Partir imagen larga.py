from PIL import Image
import os

# Ruta de la imagen
imagen_path = "(6.2) Capturas de pantalla (NotebookLM).png"

# Abrir imagen
img = Image.open(imagen_path)

# Obtener dimensiones
ancho, alto = img.size

# El tamaño del cuadrado será el ancho
lado = ancho

# Carpeta de salida
output_dir = "trozos"
os.makedirs(output_dir, exist_ok=True)

# Cortar en cuadrados
contador = 0

for y in range(0, alto, lado):
    # Área de recorte
    caja = (0, y, ancho, min(y + lado, alto))

    trozo = img.crop(caja)

    # Si el último trozo no es cuadrado,
    # puedes rellenarlo o dejarlo así.
    # Aquí lo rellenamos con transparencia.
    if trozo.size[1] < lado:
        nuevo = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
        nuevo.paste(trozo, (0, 0))
        trozo = nuevo

    salida = os.path.join(output_dir, f"trozo_{contador}.png")
    trozo.save(salida)

    contador += 1

print(f"Se generaron {contador} trozos.")