import cv2

#读取图片
img = cv2.imread("2.jpg", cv2.IMREAD_UNCHANGED)

#灰度图像
h = 0
w = 0
while h < 620 * 349:
    w = 0
    none = 0
    if w < 349:
        w += 1
    if w == 349:
        w -= 349
    print(w)
    p = img[h, w]
    black = (float(p[0]) + float(p[1]) + float(p[2])) / 3
    print(black)

cv2.imshow("2.img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
