import cv2

resized_img = cv2.imread("C:/Users/Sharon Xavier Jude/Desktop/cv images/picture6.png")
resized_wm = cv2.imread("C:/Users/Sharon Xavier Jude/Desktop/cv images/WhatsApp Image 2023-10-17 at 10.09.47_2349afaa.jpg")

h_img, w_img, _ = resized_img.shape
center_y = int(h_img / 2)
center_x = int(w_img / 2)

h_wm, w_wm, _ = resized_wm.shape

# Resize the watermark to match the dimensions of roi
resized_wm = cv2.resize(resized_wm, (w_wm, h_img))

top_y = center_y - int(h_img / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_img
right_x = left_x + w_wm

roi = resized_img[top_y:bottom_y, left_x:right_x]

# Ensure that roi and resized_wm have the same dimensions
resized_wm = resized_wm[:roi.shape[0], :roi.shape[1]]

result = cv2.addWeighted(resized_wm, 0.3, roi, 1, 0)
resized_img[top_y:bottom_y, left_x:right_x] = result

filename = "C:/Users/Sharon Xavier Jude/Desktop/cv images/picture6.png"
cv2.imwrite(filename, resized_img)
cv2.imshow("Resized Input Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


