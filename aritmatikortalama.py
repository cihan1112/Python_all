tekrar= int(input("kaç sayının ortalamasını alacaksın????????????"))

baslangic = 0
toplam = 0

while baslangic != tekrar :
    sayi = int(input("Sayıyı girsenemsu."))
    toplam = toplam + sayi 
    baslangic = baslangic + 1

ortalama = toplam / tekrar
print ("verdiğin sayıların aritmetik ortalamamsisu: ", ortalama)
