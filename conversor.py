# -*- coding: utf-8 -*-
import sys
from PIL import Image
from PIL import ImageFilter

#Checando e imprimindo os argumentos de linha de comando
if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")        



# Codigo da conversao (CONTOUR)
imagemOriginal = Image.open(sys.argv[1])

kernel = ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0)
imagemComFiltro = imagemOriginal.filter(kernel)

imagemComFiltro.save(sys.argv[2])