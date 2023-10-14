from PIL import Image
import os

path = 'C:\\Users\\danie\\Downloads\\Daniel_Ribeiro_.jpg'

if os.path.exists(path):
    imagem_original = Image.open(path)
else:
    print("O arquivo não foi encontrado no caminho especificado.")


# Abra a imagem original
imagem_original = Image.open(path)

# Obtenha as dimensões da imagem
largura, altura = imagem_original.size

# Crie uma nova imagem em tons de cinza
imagem_tons_de_cinza = Image.new('L', (largura, altura))

# Percorra todos os pixels da imagem original e converta para tons de cinza
for x in range(largura):
    for y in range(altura):
        pixel = imagem_original.getpixel((x, y))
        # Converte o pixel para tons de cinza
        cinza = int(0.2989 * pixel[0] + 0.5870 * pixel[1] + 0.1140 * pixel[2])
        imagem_tons_de_cinza.putpixel((x, y), cinza)

# Defina o valor de limiar (ajuste conforme necessário)
limiar = 128

# Crie uma nova imagem em branco para a imagem binarizada
imagem_binarizada = Image.new('1', (largura, altura))

# Percorra todos os pixels da imagem em tons de cinza e binarize
for x in range(largura):
    for y in range(altura):
        pixel = imagem_tons_de_cinza.getpixel((x, y))
        if pixel < limiar:
            imagem_binarizada.putpixel((x, y), 0)  # Se for menor, atribua 0 (preto)
        else:
            imagem_binarizada.putpixel((x, y), 255)  # Caso contrário, atribua 255 (branco)

# Salve a imagem em tons de cinza
imagem_tons_de_cinza.save('imagem_tons_de_cinza.png')

# Salve a imagem binarizada
imagem_binarizada.save('imagem_binarizada.png')

# Mostrar as imagens tanto em tons de cinza como binarizada
imagem_binarizada.show()

imagem_tons_de_cinza.show()