import cv2
import numpy as np

# Load an image
image = cv2.imread('tieulienan.jpg')

# Resize the image
resized_image = cv2.resize(image, (400, 400))

# Convert the image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
ret, thresh_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

_, otsu_threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

_, triangle_threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)

# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Thresholded Image', thresh_image)
cv2.imshow('Otsu thresholeded', otsu_threshold)
cv2.imshow('Triangle thresholeded', triangle_threshold)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()