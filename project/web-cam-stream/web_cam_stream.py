import cv2 as cv

cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print('Web kamerasına erişimde sorun!')
else:
    print('Kameranın FPS değeri %i.' %cap.get(cv.CAP_PROP_FPS))
while cap.isOpened() == True:
    ret, frame = cap.read() # web kamerası ile kare yakala
    if ret == True: # eğer kareyi yakaladıysak
        cv.imshow('web kamerasi renkli resim', frame) # yakalanan kareyi ekranda görüntüle
        if cv.waitKey(1) & 0xFF == ord('s'): # eğer bir an bile q'ya basarsa
            cv.imwrite('cekilen resim.jpg', frame, [cv.IMWRITE_JPEG_QUALITY, 100]) # dosyaya yaz 
            break # ve döngüden çık
    else: # eğer kareyi yakalayamadıysak
        print('Kare yakalanamadı!') # ekrana uyarı mesajı yaz
        break # ve döngüden çık
cap.release() # release serbest bırak demek
cv.destroyAllWindows() # bütün pencereleri kapat ve programı sonlandır