import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print('Web kamerasına erişimde sorun!')
else:
    print('Kameranın FPS değeri %i.' %cap.get(cv.CAP_PROP_FPS))
while cap.isOpened() == True:
    ret, frame = cap.read()
    k = 15 # kernel size - pencere boyutu
    filtered = cv.blur(frame, (k,k))
    # filtered = cv2.GaussianBlur(frame, (k,k), 0)
    # filtered = cv2.medianFilter(frame, k)
    # filtered = cv2.bilateralFilter(frame, k, 69, 39)
    windowText = '(%i x %i) pencere boyutu filtrelenmis video' %(k,k)
    if ret == True: # eğer kareyi yakaladıysak
        cv.imshow('web kamerasi', frame)
        cv.imshow(windowText, filtered)
        if cv.waitKey(1) & 0xFF == ord('s'): # eğer bir an bile s'ya basarsa
            cv.imwrite('web kamerasi.jpg', frame, [cv.IMWRITE_JPEG_QUALITY, 100])
            cv.imwrite('filtrelenen resim.jpg', filtered, [cv.IMWRITE_JPEG_QUALITY, 100])
            break
    else: # eğer kareyi yakalayamadıysak
        print('Kare yakalanamadı!')
        break
cap.release()
cv.destroyAllWindows()