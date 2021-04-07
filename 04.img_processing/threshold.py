import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)      # 이미지를 그레이 스케일로 읽기

# NumPy 연산으로 바이너리 이미지 만들기
tresh_np = np.zeros_like(img)                                           # 원본과 동일한 크기의 0으로 채워진 이미지
tresh_np[img > 127] = 255                                               # 127보다 큰 값만 255로 변경

# OpenCV 함수로 바이너리 이미지 만들기
ret, tresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(ret)                                                              # 127.0, 바이너리 이미지에 사용된 경계 값 반환

# 원본과 결과물 출력
imgs = {'Original': img, 'NumPy API': tresh_np, 'cv2.treshold': tresh_cv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()
