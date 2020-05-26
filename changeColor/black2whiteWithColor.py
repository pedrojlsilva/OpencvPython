import cv2
import numpy as np

image = cv2.imread("./eq.png", cv2.IMREAD_UNCHANGED)
b,g,r, a = cv2.split(image)

rows,cols, chan = image.shape


for i in range(rows):
      for j in range(cols):
        k = b[i,j]
        if k<=20:
            b[i,j]+=255

        k = g[i,j]
        if k<=20:
            g[i,j]+=255
        
        k = r[i,j]
        if k<=20:
            r[i,j]+=255

needed_multi_channel_img = np.zeros((image.shape[0], image.shape[1], 4))

needed_multi_channel_img [:,:,0] = r
needed_multi_channel_img [:,:,1] = g
needed_multi_channel_img [:,:,2] = b
needed_multi_channel_img [:,:,3] = a

cv2.imwrite("eq.png", needed_multi_channel_img)