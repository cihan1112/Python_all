bakiye = 1000
hak = 3
kullanici_adi = "mizo"
sifre = "1234"

while hak != 0: 
    adi = input("Kullanıcı adını yazınız:  ")
    sifre_k = input("Şifrenizi giriniz:  ")

    while True:

        if(adi == kullanici_adi and sifre_k == sifre):
            print("Mizgin Hanım hoşgeldiniz") # \n alt satıra inmeyi sağlar
            x = ("1 - Para Yatırma \n"
                            "2 - Para Çekme \n"
                            "3 - Bakiye Sorgulama \n" 
                            "4 - Çıkış Yap \n")
            print(x)
            secim = input ("Yapmak istediğin işlemin numrasını gir: ")

            if (secim == "1"):
                yatirma = int(input("Yatırmak istediğin miktarı yaz:  "))
                bakiye = bakiye + yatirma
                print("işlem gerçekleştirildi")
        
            elif(secim == "2"):
                cekme = int(input("Çekmek istediğin miktarı yaz:  "))
                if(cekme > bakiye):
                    print("Bakiyeniz yetersiz")
                else:
                    bakiye = bakiye - cekme
                    print("işlem gerçekleştirildi")
        
            elif(secim == "3"):
                print(bakiye)

            elif(secim == "4"):
                print("Yine beklerizzzzzz")
                break

            else:
                print("lütfen seçenek numarasını doğru giriniz")
    
        else:
            hak = hak-1
            if(hak == 0):
                break
