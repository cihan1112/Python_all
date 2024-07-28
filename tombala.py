# Cihan Nergiz Tombala Çalışması
# Bu çalışma Algorithmics Türkiye kurs içeriğinde öğrendiğim python dili ile hazırlandı.
# Çalışma "Kış Teması" yarışması için özel olarak hazırlandı.
# Kış ayları yılbaşını ve yılbaşı tombala oyununu hatırlattığı için :) bu temayı seçtim.
# -----------------------------------------------------------
# Tombala oyununda her oyuncuya bir kart verilir.
# Bu kartların üzerinde 1'den 90'a kadar (1-90 dahil) 15 adet sayı bulunmaktadır.
# Kartlarda yer alan sayıların bazıları ortaktır. Yani 19 iki farklı kartta bulunabilir.
# Aynı zamanda kartlarda yer alan sayılar rastgele hazırlanır (randommmm :D)
# Kartlar haricinde sayıların yazılı olduğu taşlar bulunur.
# Bu Taşlar bir torbanın içine konularak rastgele seçilir.
# Çekilen sayının yer aldığı kartta o sayının üstü çizilir veya kapatılır.
# Kartında yer alan bütün sayıların çekldiği ilk kişi oyunu kazanır.
# -----------------------------------------------------------
# Yaptığımız bu çalışma ile oyuncu sayıları daha kolay takip edebilecek.
# Oyuncu önce kartında yer alan sayıları yazarak bir liste oluşturacak.
# Liste tamamlandıktan sonra kullanıcıdan sayı istenecek.
# İstenilen sayı aslında torbadan çıkan sayı.
# Yazılan sayı listede yer alıyorsa program listede bu sayıyı silecek.
# Her sayı istenildiğinde listenin güncel hali gösterilecek.


kartim = [8, 11, 19, 26, 66, 85, 65, 18, 69, 52, 89, 58, 68, 62, 54 ] #kartda yer alan sayılar
kartim.sort()# listemde yer alan sayıları sıraladım.
kalan = len(kartim) # listede yer alan eleman sayısı. 

while len(kartim)>0: #listede eleman olduğu sürece döngü çalışacak.
    print("_________________________________________________")
    print("Kartın: ", kartim) #listemi ekrana bastım.
    print("Kalan: ", kalan ) #listemde kalan eleman sayısı ekrana bastım.
    okunan = int(input("Torbadan çıkan sayıyı gir:")) #oyuncu torbadan çıkan sayıyı girecek.
    if okunan in kartim: #okunan sayı oyuncunun kartında yer alıyorsa.
        kartim.remove(okunan) #karttdan okunan sayıyı sil.
        kalan=kalan-1 #kalan 1 azaltılarak döngünün sonlanması sağlanacak.
print("***************")
print("God jul du vin!")
print("***************")
#Bu projede bana yardım eden sevgi ve saygıyla Mizgin Durgun öğretmenime çok teşekkür ve tusen takk dilerim