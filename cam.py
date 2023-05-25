import cv2

# Kamera numarasını belirleyin (genellikle 0 veya 1)
kamera_numarasi = 0

# Kamera yakalayıcısını başlatın
kamera = cv2.VideoCapture(kamera_numarasi)

# Kamera çözünürlüğünü ayarlayın
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    # Kameradan görüntüyü yakalayın
    ret, frame = kamera.read()

    # Görüntüyü ekranda gösterin
    cv2.imshow("Kamera", frame)

    # Çıkış için "q" tuşuna basıldığında döngüyü sonlandırın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırakın ve pencereleri kapatın
kamera.release()
cv2.destroyAllWindows()
