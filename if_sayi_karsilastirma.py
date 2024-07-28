#sayılar eşit ise girilen sayılar eşit desin
#ilk girilen sayı büyükse ilk sayı büyük desin
#ikinci girilen sayı büyükse iikinci büyük desin
m = int ( input("1. sayını yaz "))
z = int ( input("2. sayını yaz "))
if ( m == z ):
    print ("Sayı eşit tekrar dene")
elif (m < z ):
    print ("2. girdiğin sayı daha büyük ")
else :
    print (" 1. girdiğin sayı daha büyük ")
