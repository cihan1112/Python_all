soru = int (input ("Bugün hava kaç derece?"))
if (soru > 0 and soru < 10):
    print("Evde film izleyebilirsin, Eve arkadaşlarını çağırıp sohbet edebilirsin...")
    soru2 = input("Daha fazla fikir ister misin?")
    if (soru2 == "evet" or "tamam"):
        print ("Evde lego yapabilirsin(bunu diyorum ama lego bedava değil), Evde şarkı açıp dans edebilirsin, Evde çay partisi verebilirsin.")

elif (soru > 10 and soru < 20):
    print("Sinemaya gidebilirsin, Bir kafede arkadaşların ile veya yalnız oturabilirsin...")
    soru3 = input("Daha fazla fikir ister misin?")
    if (soru3 == "evet" or "tamam"):
        print ("Avmde takılabilirsin, Evde parti verebilirsin.")

elif (soru > 20 and soru < 30):
    print("Dışarıda koşu veya yürüyüş yapabilirsin, Bir kafede oturabilirsin...")
    soru4 = input("Daha fazla fikir ister misin?")
    if (soru4 == "evet" or "tamam"):
        print ("Pikniğe gidebilirsin, Arkadaşların ile su savaşı yapabilirsin.")

elif (soru > 30 and soru < 40):
    print("Sahile gidebilirsin, Güneşlenebilirsin...")
    soru5 = input("Daha fazla fikir ister misin?")
    if (soru5 == "evet" or "tamam"):
        print ("Dondurma yiyebilirsin, Klima açabilirsin.")

elif (soru > 40 and soru < 60):
    print("Otur evinde klimanı son derece aç(dikkat et buharlaşma)!")
    soru6 = input("Daha fazla fikir ister misin?")
    if (soru6 == "evet" or "tamam"):
        print ("OTUR EVİNDE AÇ KLİMANI BAŞKA YAPACAĞIN BİRŞEY YOK ZATEN!!!!!!")

elif (soru > -10 and soru < 0):
    print("Evde pijama partisi verebilirsin, Sıcak çikolata veya kahve yapıp içebilirsin...")
    soru7 = input("Daha fazla fikir ister misin?")
    if (soru7 == "evet" or "tamam"):
        print ("Evde oturup film izleyebilirsin ve çok fazla yapabileceğin birşey yok zaten.")

elif (soru > -30 and soru < -10):
    print("KOMBİNİ SONLA OTUR EVİNDE İÇ KAHVENİ!!!")
    soru5 = input("Daha fazla fikir ister misin?")
    if (soru5 == "evet" or "tamam"):
        print ("İSTİYORSAN ÇIK DIŞARI KANIN DONSUN!!!")







