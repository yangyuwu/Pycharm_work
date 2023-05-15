import cv2 as cv

cap = cv.VideoCapture(0)  # 打开摄像头
while (True):
    hx, frame = cap.read()  # 开始用摄像头读数据，返回hx为true则表示读成功，frame为读的图像
    if hx is False:
        print('read video error')
        exit()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)    # 把彩色图像转换成灰度图像，也可不转换
    cv.namedWindow('video', cv.WINDOW_AUTOSIZE)     # 窗口设置为自动调节大小
    cv.imshow('video', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):       # 按q退出
        break
cap.release()   # 释放摄像头
