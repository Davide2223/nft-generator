from hashlib import sha256 
import os 
import pygame

hash_matches = {} #dict used for register hash of any img
list_dilay = os.listdir('dilay') #list used for register any directory of imgs

#function used for generate hash for nft
def generate_hash_nft(hash_img):
    unicode = hash_img #the hash of nft is based on hash of single img
    hash = sha256(unicode.encode('utf-8')).hexdigest()
    
    return hash

#function uded for generate hash for img
def generate_hash_img(name, size, width, height):
    unicode = name + str(size) + str(width) + str(height) #the hash of img is based on name, size, width, height of img
    hash = sha256(unicode.encode('utf-8')).hexdigest()
    
    return hash

#update dict with hash of any img 
for dilay in list_dilay:
    for img in os.listdir(f'dilay/{dilay}'):
        width, height = pygame.image.load(f'dilay/{dilay}/{img}').get_rect()[2:] #using pygame module for get width and height of img
        hash_matches.update({img: generate_hash_img(img, pygame.image.load(f'dilay/{dilay}/{img}').get_size(), width, height)})

