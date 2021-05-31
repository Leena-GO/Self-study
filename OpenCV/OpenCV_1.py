import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #_: read()는 2개의 arg를 받는데, 첫 arg는 무시해도 된다는 것
    
    cv2.imshow('Webcam', frame) #앞의 string값은 Window name이다.

    if cv2.waitKey(1) == ord('q'):
        break