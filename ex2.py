import cv2

# Read image
image = cv2.imread(r"H:\Untitled.PNG")

# Apply Gaussian Blur
blur_image = cv2.GaussianBlur(image, (5, 5), 0)

# Show images
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blur Image", blur_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output
cv2.imwrite("blur_output.jpg", blur_image)