import cv2
car_cascade = cv2.CascadeClassifier("C:/Users/Sharon Xavier Jude/Desktop/cv images/cars.xml" )
cap = cv2.VideoCapture("C:/Users/Sharon Xavier Jude/Desktop/cv images/WhatsApp Video 2023-10-18 at 08.28.54_f776b43e.mp4")
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
