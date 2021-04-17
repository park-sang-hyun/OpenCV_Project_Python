import cv2
import numpy as np
import matplotlib.pylab as plt

win_name = 'back_projection'
img = cv2.imread('../img/pump_horse.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
draw = img.copy()

# 역투영된 결과를 마스킹해서 결과를 출력하는 공통함수
def masking(bp, win_name):
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    cv2.filter2D(bp, -1, disc, bp)
    _, mask = cv2.threshold(bp, 1, 255, cv2.THRESH_BINARY)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow(win_name, result)

# 직접 구현한 역투영 함수
def backProject_manual(hist_roi):
    # 전체 영상에 대한 H, S 히스토그램 계산
    hist_img = cv2.calcHist([hsv_img], [0,1], None, [180,256], [0,180,0,256])

    # 선택 영역과 전체 영상에 대한 히스토그램 비율 계산
    hist_rate = hist_roi / (hist_img + 1)

    # 비율에 맟는 픽셀 값 매핑
    h,s,v = cv2.split(hsv_img)
    bp = hist_rate[h.ravel(), s.ravel()]
    bp = np.minimum(bp, 1)
    bp = bp.reshape(hsv_img.shape[:2])
    cv2.normalize(bp, bp, 0, 255, cv2.NORM_MINMAX)
    bp = bp.astype(np.uint8)

    # 역투영 결과로 마스킹해서 결과 출력
    masking(bp, 'result_manual')

# OpenCV API로 구현한 함수
def backProject_cv(hist_roi):
    # 역투영 함수 호출
    bp = cv2.calcBackProject([hsv_img], [0, 1], hist_roi, [0, 180, 0, 256], 1)

    # 역투영 결과로 마스킹해서 결과 출력
    masking(bp, 'result_cv')

# ROI 선택
(x,y,w,h) = cv2.selectROI(win_name, img, False)

if w > 0 and h > 0:
    roi = draw[y:y+h, x:x+w]
    cv2.rectangle(draw, (x, y), (x+w, y+h), (0,0,255), 2)

    # 선택한 ROI를 HSV 컬러 스페이스로 변경
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # H, S 채널에 대한 히스토그램 계산
    hist_roi = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # ROI의 히스토그램을 매뉴얼 구현함수와 OpenCV를 이용하는 함수에 각각 전달
    backProject_manual(hist_roi)
    backProject_cv(hist_roi)

cv2.imshow(win_name, draw)
cv2.waitKey()
cv2.destroyAllWindows()
