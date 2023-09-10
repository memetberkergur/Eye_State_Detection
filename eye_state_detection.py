import cv2

# Cascade sınıflandırıcısını yükle (gözler için)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Kamera bağlantısını başlatın
kamera = cv2.VideoCapture(0)  # 0, yerleşik kamera için kullanılır

while True:
    # Kamera görüntüsünü okuyun
    ret, frame = kamera.read()

    # Gri tonlamalı görüntü oluşturun (daha hızlı işlem yapmak için)
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gözleri tespit et
    gozler = eye_cascade.detectMultiScale(gri, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Gözlerin durumunu belirle
    if len(gozler) > 0:
        durum = "AÇIK"
    else:
        durum = "KAPALI"

    # Ekranın üst kısmına durumu yazdır
    cv2.putText(frame, f"Göz Durumu: {durum}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Görüntüyü göster
    cv2.imshow('Göz Durumu Tespiti', frame)

    # Çıkış için "q" tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapatın
kamera.release()

# Pencereyi kapatın
cv2.destroyAllWindows()
