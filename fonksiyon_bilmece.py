#def ?????():
#   s = input("İki kere kaç eder?")
#   if s == "dört":
#       print("doğru!")
#   else:
#       print("tekrar dene!")
def bilmece():
    cevap = 25
    y = 0
    sayac = 0
    while cevap != y:
        y = int(input("Matematik sorusunun cevabını söyle, 5*5 kaçtır? "))
        sayac = sayac + 1
    print("AFERİN !!! ", sayac , "defada buldun" )

bilmece()
