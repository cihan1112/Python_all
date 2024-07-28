k = "cihannergiz6"
s = "555"
n = input("kullanıcı adınızı giriniz: ")
p = input("Şifrenizi giriniz: ")
if ( n == k and s == p ):
    print ("giriş başarılı ")
elif ( k == n and s != p):
    print ("Hatalı şifre")
else :
    (" Hatalı kullanıcı adı ")