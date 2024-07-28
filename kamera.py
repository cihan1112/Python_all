import cv2
import numpy as np

def apply_magic_frame(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path)

    # Mavi renkli bir çerçeve oluştur
    magic_frame = np.zeros_like(image)
    magic_frame[:] = [255, 0, 0]  # Mavi renk (BGR formatında)

    # Görüntüyü ve sihirli çerçeveyi birleştir
    magic_image = cv2.addWeighted(image, 0.7, magic_frame, 0.3, 0)

    # Görüntüyü ekranda göster
    cv2.imshow('Original Image', image)
    cv2.imshow('Magic Frame Effect', magic_image)

    # Pencere kapatmak için bekleyin
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Fonksiyonu kullanarak örnek görüntü üzerine uygula
apply_magic_frame('man.jpg')
