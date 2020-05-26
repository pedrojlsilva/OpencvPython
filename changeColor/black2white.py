import cv2
import numpy as np

image = cv2.imread("./battery.png", cv2.IMREAD_UNCHANGED)
b,g,r, a = cv2.split(image)

b=b+255
needed_multi_channel_img = np.zeros((image.shape[0], image.shape[1], 4))

needed_multi_channel_img [:,:,0] = b
needed_multi_channel_img [:,:,1] = b
needed_multi_channel_img [:,:,2] = b
needed_multi_channel_img [:,:,3] = a

cv2.imwrite("batteryWhite.png", needed_multi_channel_img)