from hashlib import sha256
import os
import pygame

hash_matches = {}
list_dilay = os.listdir('dilay')

def generate_hash_nft(hash_img):
    unicode = hash_img
    hash = sha256(unicode.encode('utf-8')).hexdigest()
    return hash
    
def generate_hash_img(name, size, width, height):
    unicode = name + str(size) + str(width) + str(height)
    hash = sha256(unicode.encode('utf-8')).hexdigest()
    return hash
 
for dilay in list_dilay:
    for img in os.listdir(f'dilay/{dilay}'):
        width, height = pygame.image.load(f'dilay/{dilay}/{img}').get_rect()[2:]
        hash_matches.update({img: generate_hash_img(img, pygame.image.load(f'dilay/{dilay}/{img}').get_size(), width, height)})

