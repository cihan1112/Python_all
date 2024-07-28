# Kullanıcıdan sayı al
sayi = input("Lütfen bir sayı girin: ")

# Basamak toplamını hesaplamak için bir değişken başlat
basamak_toplami = 0

# Sayının her bir basamağını gez ve topla
for basamak in sayi:
    basamak_toplami += int(basamak)

# Sonucu yazdır
print(f"{sayi} sayısının basamakları toplamı: {basamak_toplami}")
