import cv2

# Read image
image = cv2.imread(r"H:\Untitled.PNG")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Show comparison
cv2.imshow("Original Gray Image", gray)
cv2.imshow("Histogram Equalized Image", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output
cv2.imwrite("equalized_output.jpg", equalized)