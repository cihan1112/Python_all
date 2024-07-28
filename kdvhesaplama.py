soru = int(input("ürün fiyatı ne kadar??"))
islem1 = 0
toplam = 0
if (soru > 0 and soru < 1000):
    islem1 = (soru * 0.10)
    toplam = soru + islem1
    print(toplam)
else:
    islem2 = (soru * 0.18)
    toplam = soru + islem2
    print(toplam)