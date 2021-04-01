import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)                    # 0 ~ 9
y = x**2                            # 0 ~ 81
plt.plot(x, y)                      # plot 생성
plt.show()                          # plot 그리기
