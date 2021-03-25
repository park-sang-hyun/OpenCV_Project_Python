import cv2
cap = cv2.VideoCapture(0)

if cap.isOpened:
    file_path = './record.avi'
    fps = 25.40
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')               # 인코딩 포맷 문자
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))
    out = cv2.VideoWriter(file_path, fourcc, fps, size)     # VideoWriter 객체 생성

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera-recording', frame)
            out.write(frame)                                # 파일 저장
            if cv2.waitKey(int(1000/fps)) != -1:
                break
        else:
            print("no frame")
            break

    out.release()                                           # 파일 닫기
else:
    print("can't open camera.")

cap.release()                           
cv2.destroyAllWindows()


cap.release()                           
cv2.destroyAllWindows()
