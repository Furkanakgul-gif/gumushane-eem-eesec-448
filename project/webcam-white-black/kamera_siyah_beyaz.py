import cv2 as cv

cap = cv.VideoCapture(0)
T =100
while True:
    ret, frame = cap.read() # web kamerası ile kare yakala
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    t, frameBW = cv.threshold(frameGray, T, 255, cv.THRESH_BINARY)
    cv.imshow('web kamerasi renkli resim', frameBW) # yakalanan kareyi ekranda görüntüle
    if cv.waitKey(1) & 0xFF == ord('s'): # eğer bir an bile s'ya basarsa
        cv.imwrite('cekilen resim.jpg', frameBW, [cv.IMWRITE_JPEG_QUALITY, 100]) # dosyaya yaz 
        break # ve döngüden çık
cap.release() # release serbest bırak demek
cv.destroyAllWindows() # bütün pencereleri kapat ve programı sonlandır