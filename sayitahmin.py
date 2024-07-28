import random
sayi = random.randint(1 , 100)
cevap = 0
sayac = 0
while (sayi != cevap):
    cevap = int ( input ("sayiyi bul(100- 1)"))
    sayac = (sayac +1)
    if (cevap < sayi):
        print ("yukarı")
    elif (cevap > sayi):
        print (" aşağı")
print ("OMG...Buldun" , sayac , "defada buldun")
