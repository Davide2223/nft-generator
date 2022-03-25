from check_valid_match import list_img_nft
from hash_generate import list_dilay
from PIL import Image
import os
import random

list_nft = [] #empty list 

#parametres
j = 1
i = 1
k = 1
r = 1

#part of set rare img in a random way
nm = random.randint(1, len(list_img_nft))
c = 1
list_rare_img = [i for i in os.listdir('rare_img')] #list of rare img

#algorithm of match img based on a "tree" matches
#scroll through all match nft 
for n in range(len(list_img_nft)):
    while i <= len(list_img_nft[0])-1:
       #this part is dedicated to the creation of the rare nft
        if c == nm:
            for img_rare in list_rare_img[1:]:
                img_base = Image.open(f'rare_img/{list_rare_img[0]}').convert('RGBA') if i-1 == 0 else Image.open(f'progress_nft/{os.listdir("progress_nft")[-1]}').convert('RGBA')
                img_superimposed = Image.open(f'rare_img/{img_rare}').convert('RGBA')
                img_base.paste(img_superimposed, (0, 0), img_superimposed)
                img_base.save(f'progress_nft/nft{k}.png')

                i += 1

            k += 1
            j += 1
            c += 1
        else:
            #take a base and lnft created earlier and overlap them until it is complete
            img_base = Image.open(f'dilay/{list_dilay[j-1]}/{list_img_nft[n][i-1]}').convert('RGBA') if i-1 == 0 else Image.open(f'progress_nft/{os.listdir("progress_nft")[-1]}').convert('RGBA')
            img_superimposed = Image.open(f'dilay/{list_dilay[j]}/{list_img_nft[n][i]}').convert('RGBA')
            img_base.paste(img_superimposed, (0, 0), img_superimposed)
            img_base.save(f'progress_nft/nft{k}.png')

            k += 1
            i += 1
            j += 1
            c += 1
    
    #save the composed nft in the folder to use it for the next overlay 
    last_nft = Image.open(f'progress nft/{os.listdir("progress_nft")[-1]}')
    last_nft.save(f'nft_generated/nft{r}.png')
    
    #remove from the folder of previus match the img matches
    for img_nft in os.listdir('progress_nft'):
        os.remove(f'progress nft/{img_nft}')

    i = 1
    j = 1
    r += 1
