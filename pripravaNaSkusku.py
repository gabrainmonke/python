# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:11:06 2024

@author: Richard
"""

from random import randrange

N = 4
vstupnePole = [0,1,2,3,4,5,6,7,8,9]

def funkcia(N,vstupnePole):
    
    vystupnePole = []
    
    for i in range(N):
        pole = []
        
        for j in range(N):
            pole.append(randrange(10))
        
        vystupnePole.append(pole)
        
    return vystupnePole
        
        
print(funkcia(N, vstupnePole))

import os
import cv2

path = os.getcwd() + "\obrazok.jpeg" #vráti cestu ku danému adresáru kde pracujem

def embed_image(image_path, num_nested):
    # Načítanie obrázka
    image = cv2.imread(image_path)

    # Získanie rozmerov obrázka
    img_height, img_width = image.shape[:2]

    # Inicializácia výsledného obrázka ako kópie pôvodného
    result_image = image.copy()

    # Pre každé vnorovanie obrázka
    for i in range(1, num_nested + 1):
        # Vypočítanie rozmerov nového obrázka (polovičné veľkosti)
        new_width = img_width // (2 ** i)
        new_height = img_height // (2 ** i)
        
        # Zmenšenie obrázka
        resized_image = cv2.resize(image, (new_width, new_height))
        
        # Vypočítanie pozície pre vloženie zmenšeného obrázka do stredu
        x = (img_width - new_width) // 2
        y = (img_height - new_height) // 2
        
        # Vloženie zmenšeného obrázka do stredu
        result_image[y:y+new_height, x:x+new_width] = resized_image

    # Uloženie výsledného obrázka
    cv2.imwrite('result.jpg', result_image)

    # Zobrazenie výsledného obrázka
    cv2.imshow('Result', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Použitie funkcie
embed_image(path, 7)  # Zadaj cestu k tvojmu obrázku a počet vnorovaní

