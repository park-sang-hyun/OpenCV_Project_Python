import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../img/girl.jpg')

plt.imshow(img[:,:,::-1])       # 이미지 컬러 채널 변경해서 표시
plt.xticks([])                  # x좌표 눈금 제거
plt.yticks([])                  # y좌표 눈금 제거
plt.show()
