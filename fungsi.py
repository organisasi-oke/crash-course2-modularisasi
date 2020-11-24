"""
menghitung luas segitiga
L=(a*t)/2
"""
a=10
t=6
L=(a*t)/2
print(f"segitiga dg alas={a} dan tinggi={t} yaitu L=(a*t)/2={L}")

def hitung_luas_segitiga(alas,tinggi):
    luas_segitiga=(alas*tinggi)/2
    return luas_segitiga

print(f'menghitung luas segitiga {hitung_luas_segitiga(20, 6)}')
