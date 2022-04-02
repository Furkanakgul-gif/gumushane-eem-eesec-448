import cv2 as cv

cap = cv.VideoCapture(0)
k = 1
i = 1
while True:
    ret, frame = cap.read() # web kamerası ile kare yakala
    textFrameNumber = 'Frame = %i' %k
    k = k+1
    frame = cv.putText(frame, textFrameNumber, (30,50), 3, 1, (0,0,255), 2, 0)
    cv.imshow('web kamerasi renkli resim', frame) # yakalanan kareyi ekranda görüntüle
    if cv.waitKey(1) & 0xFF == ord('s'): # eğer bir an bile q'ya basarsa
        textFrameNumber = 'webkamerasiresim = %i.jpg' %i
        cv.imwrite('textFrameNumber', frame, [cv.IMWRITE_JPEG_QUALITY, 100]) # dosyaya yaz 
        i = i+1
    elif cv.waitKey(1) & 0xFF == ord('q'):
        break # ve döngüden çık
cap.release() # release serbest bırak demek
cv.destroyAllWindows() # bütün pencereleri kapat ve programı sonlandır