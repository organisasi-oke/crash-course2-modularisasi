#from geometri.segitiga import hitung_luas_segitiga
#import geometri.segitiga as gs
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga
from geometri.persegi_panjang import hitung_luas_persegi_panjang, info as info_segipanjang

print(info_segitiga())
print(f'hitung luas segitiga(6,10) = {hitung_luas_segitiga(6,10)}')
print(info_segipanjang())
print(f'hitung luas segi panjang(6,10) = {hitung_luas_persegi_panjang(6,10)}')