import cv2

cap = cv2.VideoCapture(0)               # 0번 카메라 장치 연결 (번호는 0부터 1씩 증가)
if cap.isOpened():                      
    while True:
        ret, img = cap.read()           # 카메라 프레임 읽기
        if ret:                         
            cv2.imshow('camera', img)   # 프레임 이미지 표시
            if cv2.waitKey(1) != -1:    # 1ms 동안 키 입력 대기 (대기 시간동안 계속 -1을 반환함)
                break                   # 아무키나 누르면 중지
        else:
            print('no frame')
            break
else:
    print("can't open camera.")

cap.release()                           
cv2.destroyAllWindows()
