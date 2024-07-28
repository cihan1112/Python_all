ans1 = "Biraz dinlenmelisin!"
ans2 = "Her şey yolunda, bir sorun yok!"
ans3 = "Ailene haber vermelisin!"
ans4 = "Ambulans çağır!"

q1 = "Ateşin 37 dereceden düşük mü?"
q2 = "Ateşin 36 dereceden yüksek mi?"
q3 = "Ateşin 40 dereceden yüksek mi?"

m = ( input (q1))
if (m == "evet"):
    k = ( input (q2))
    if (k == "evet"):
        print (ans2)
    else:
        print (ans1)
else :
    s = (input (q3))
    if (s == "evet"):
        print (ans4)
    else :
        print (ans3)
    