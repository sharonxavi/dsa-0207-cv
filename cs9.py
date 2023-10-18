import cv2
path ="C:/Users/Sharon Xavier Jude/Desktop/cv images/Picture3.jpg"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180)
img = cv2.resize(image,(600,600))
cv2.imshow(window_name, img)
cv2.waitKey(0)
