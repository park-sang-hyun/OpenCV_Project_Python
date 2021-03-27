import cv2

img_file = "../img/girl.jpg"
img = cv2.imread(img_file)
title = 'IMG'                           # 창 이름
x, y = 100, 100                         # 최초 좌표

while True:
    cv2.imshow(title, img)
    cv2.moveWindow((title), x, y)
    key = cv2.waitKey(0) & 0xFF         # 키보드 입력을 무한 대기, 8비트 마스크 처리
    print(key, chr(key))                # 키보드 입력 값, 문자 값 출력

    if key == ord('h'):                 # 'h' 키이면 좌로 이동
        x -= 10
    elif key == ord('j'):               # 'j' 키이면 아래로 이동
        y += 10
    elif key == ord('k'):               # 'k' 키이면 위로 이동
        y -= 10
    elif key == ord('l'):               # 'l' 키이면 우로 이동
        x += 10
    elif key == ord('q') or key == 27:  # 'q' 나 'esc' 키이면 종료
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y)
    