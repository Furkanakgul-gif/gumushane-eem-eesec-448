import cv2 as cv
import numpy as np

resim = cv.imread('gondol.jpg') # resim yükle
print('yükseklik = %i   genişlik = %i   kanal sayısı = %i' %(resim.shape[0],resim.shape[1],resim.shape[2]))
# resmin üzerine yazı yazalım
font = cv.FONT_HERSHEY_SIMPLEX # font tipi
org = (400, 450) # yazının içinde bulunduğu dikdörtgenin sol alt köşesi
fontScale = 2 # font büyüklüğü
color = (100, 255, 50) # BGR sırasında yazının renk kodu
thickness = 5 # yazının kalınlığı
yaziliResim = cv.putText(resim, 'gondol', org, font, fontScale, color, thickness, cv.LINE_AA)
# resmi yeniden boyutlandır, dosyaya kaydet ve ekranda görüntüle
s = 1.2 # scale - ölçek
dim = (int(s*resim.shape[1]), int(s*resim.shape[0])) # boyut
yeniYaziliResim = cv.resize(yaziliResim, dim, interpolation = cv.INTER_AREA)
cv.imwrite('cizim.jpg', yeniYaziliResim, [cv.IMWRITE_JPEG_QUALITY, 100])
cv.imshow("Uzerine yazi yazilmis ve yeniden boyutlandirilmis resim", yeniYaziliResim)
cv.waitKey(0)