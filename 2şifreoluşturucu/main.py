import random
karakterler  ="+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def sifre_olustur(uzunluk):
    sifre = ""
    for i in range(sifre_uzunlugu):
        sifre += random.choice(karakterler)
    print(sifre)
    return sifre

while True:    
    hesap = input("Hangi hesabın için şifre istiyorsun?\n")
    sifre_uzunlugu = int(input("şifre uzunluğu ne kadar olsun?\n"))
    if sifre_uzunlugu <= 0:
        break

    with open("sifreler.txt", "a") as doc:
        doc.write(f"{hesap}: {sifre_olustur(sifre_uzunlugu)}\n")