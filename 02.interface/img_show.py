import cv2

img_file = "../img/girl.jpg" # 이미지 경로
img = cv2.imread(img_file)  # 이미지 읽어서 img 변수에 할당

if img is not None:
    cv2.imshow('IMG', img)  # 읽은 이미지를 화면에 표시
    cv2.waitKey()           # 키가 입력될 때까지 대기
    cv2.destroyAllWindows() # 창 모두 닫기
else:
    print('No image file.')
    