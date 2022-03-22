from hash_generate import list_dilay
import os

list_img = [] #list used for register any "img" (name of img)
list_img_cp = list_img.copy() #used for insert in array a sub array with the set of img
len_dilays = [len(os.listdir(f'dilay/{dilay}')) for dilay in list_dilay] #list with len of any single set img directory(folder)
s = 0
k = 1

#add any name img in list
for dilay in list_dilay:
    for img in os.listdir(f'dilay/{dilay}'):
        list_img.append(img)

#add in list_im_cp the sub array (set of any delay)
for n in range(len(len_dilays)):
    list_img_cp[s:sum(len_dilays[0:k])] = [list_img[s:sum(len_dilays[0:k])]]
    s = sum(len_dilays[0:k])
    k += 1
