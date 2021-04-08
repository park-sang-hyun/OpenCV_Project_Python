import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)               # 이미지를 그레이 스케일로 읽기

_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)                      # 경계 값을 130으로 지정
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)    # 경계 값을 지정하지 않고 오츠의 알고리즘 선택

print('otsu threshold:', t)                                                     # 오츠의 알고리즘으로 선택된 경계 값 출력

imgs = {'Original': img, 't:130': t_130, 'otsu:%d'%t: t_otsu}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])
    
plt.show()
