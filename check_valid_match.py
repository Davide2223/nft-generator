from hash_generate import generate_hash_nft
from collect_img import list_img_cp
from itertools import product

list_img_nft_check = list(product(list_img_cp[0], list_img_cp[1], list_img_cp[2], list_img_cp[3], list_img_cp[4], list_img_cp[5], list_img_cp[6]))
list_hash_nft_check = []
list_img_nft = []

for i in range(len(list_img_nft_check)):
    list_img_nft_check[i] = list(list_img_nft_check[i])
    list_img_nft_check[i].append(generate_hash_nft(''.join(list_img_nft_check[i])))

for hash_nft in list_img_nft_check:
    if hash_nft[-1] not in list_hash_nft_check:
        list_img_nft.append(hash_nft[0:len(hash_nft)-1])
        list_hash_nft_check.append(hash_nft[-1])

