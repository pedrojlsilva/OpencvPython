import cv2
import numpy as np

img = cv2.imread("HSV.png")

hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hue_img, sat_img, val_img = cv2.split(hsv_img)

thresh = 10
sat_thresh = 100 #raio da coroa circular

low_hue = np.array(40)  #Diminuir aumenta o branco no sentido horario
high_hue = np.array(80) #aumentar aumenta o branco no sentido anti horario


binary_img_hue = cv2.inRange(hue_img,low_hue,high_hue)
binary_img_sat = cv2.inRange(sat_img,sat_thresh,255)
binarizedImg = cv2.bitwise_and(binary_img_hue,binary_img_sat)

cv2.imshow("hue", binary_img_hue)
cv2.imshow("sat", binary_img_sat)
cv2.imshow("Binarized", binarizedImg)

cv2.waitKey(0)

cv2.destroyAllWindows() 
