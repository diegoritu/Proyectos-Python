import cv2
import numpy as np

imagen = cv2.imread("b.jpg")
escGrises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
escGrisesInv = 255 - escGrises
escGrisesInv = cv2.GaussianBlur(escGrisesInv,(21,21),0)
salida = cv2.divide(escGrises,255-escGrisesInv,scale=256.0)
cv2.namedWindow("im", cv2.WINDOW_AUTOSIZE)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("salida.jpg",salida)

