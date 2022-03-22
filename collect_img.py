from hash_generate import list_dilay
import os

list_img = []
list_img_cp = list_img.copy()
len_dilays = [len(os.listdir(f'dilay/{dilay}')) for dilay in list_dilay]
s = 0
k = 1

for dilay in list_dilay:
    for img in os.listdir(f'dilay/{dilay}'):
        list_img.append(img)

for n in range(len(len_dilays)):
    list_img_cp[s:sum(len_dilays[0:k])] = [list_img[s:sum(len_dilays[0:k])]]
    s = sum(len_dilays[0:k])
    k += 1
