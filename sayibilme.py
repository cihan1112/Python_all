import random 
print ("sayı tahmin oyununa hoşgeldiniz aşkolar 1-100 arasında bir sayı tuttum sen bul onu ayol onu da mı ben yapıcam")
def tahmin ():
    sayi = random.randint(1 , 100)
    sayac = 0
    while (True) :
        cevap = int (input ("Aklımda tuttuğum sayı kaç aşko?"))
        sayac = sayac + 1
        if (cevap > sayi):
            print ("aşağı")
        elif (cevap < sayi):
            print ("yukarı")
        else :
            print ("buldun aşko oha nasıl yaptın")
            print ( sayac , "defada buldun aşko tamam mı")
            break

tahmin ()