import os
import cv2
import numpy as np

# Suppress warnings from libpng
os.environ["OPENCV_IO_ENABLE_JASPER"] = "1"

# Read the image in BGR format
img = cv2.imread('object.jpg', cv2.IMREAD_COLOR)

if img is None:
    print("Error: Could not read the image file.")
    exit()

# Resize the image to 20% of its original size
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

# Convert the BGR image to an HSV image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the HSV mask
lower_range = np.array([167, 100, 100], dtype=np.uint8)
upper_range = np.array([187, 255, 255], dtype=np.uint8)

# Create a mask that isolates the specified color range
mask = cv2.inRange(hsv, lower_range, upper_range)

# Display the original image and the mask side-by-side
cv2.imshow('Original Image', img)
cv2.imshow('Color Mask', mask)

print("Press [ESC] to exit.")

# Wait for user to press [ESC] key to exit
while True:
    key = cv2.waitKey(0)
    if key == 27:  # ASCII code for ESC key
        break

# Clean up and close windows
cv2.destroyAllWindows()
