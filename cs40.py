import cv2
img = cv2.imread("C:/Users/Sharon Xavier Jude/Desktop/cv images/WhatsApp Image 2023-10-18 at 09.27.12_e0dc8c15.jpg")
x, y = 100, 100
width, height = 200, 150
roi = img[y:y+height, x:x+width]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
