import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():                      
    while True:
        ret, frame = cap.read()
        if ret:                         
            cv2.imshow('camera', frame)
            if cv2.waitKey(1) != -1:            # 아무키나 누르면
                cv2.imwrite('photo.jpg', frame) # 프레임을 'photo.jpg'로 저장
                break
        else:
            print('no frame')
            break
else:
    print("can't open camera.")

cap.release()                           
cv2.destroyAllWindows()
