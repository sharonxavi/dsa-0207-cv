import cv2
watch_cascade = cv2.CascadeClassifier("C:/Users/Sharon Xavier Jude/Desktop/cv images/watch_cascade.xml")
img = cv2.imread("C:/Users/Sharon Xavier Jude/Desktop/cv images/WhatsApp Image 2023-10-18 at 09.15.03_a2b8ea1c.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
watches = watch_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
for (x, y, w, h) in watches:
 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Watches Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
