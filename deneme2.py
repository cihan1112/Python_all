import turtle

# Kaplumbağa oluştur
kaplumbaga = turtle.Turtle()

# Kaplumbağanın boyutunu ayarla
kaplumbaga.shapesize(stretch_wid=10, stretch_len=10, outline=5)  # Stretch_wid: yükseklik, Stretch_len: genişlik

# Kaplumbağa hareket et
kaplumbaga.forward(100)

# Pencereyi kapatmak için bekle
turtle.done()
