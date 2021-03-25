import cv2

video_file = "../img/big_buck.avi"

cap = cv2.VideoCapture(video_file)      # 동영상 캡처 객체 생성
if cap.isOpened():                      # 캡처 객체 초기화 확인
    while True:
        ret, img = cap.read()           # 다음 프레임 읽기
        if ret:                         # ret이 True이면 프레임 읽기 성공 (img를 꺼내서 사용가능)
            cv2.imshow(video_file, img) # 화면에 표시
            cv2.waitKey(25)             # 25ms 지연 (40fps로 가정)
        else:
            break
else:
    print("can't open video.")

cap.release()                           # 캡처 자원 반납
cv2.destroyAllWindows()