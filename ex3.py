import cv2

# Read image
image = cv2.imread(r"H:\Untitled.PNG")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Show results
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output
cv2.imwrite("canny_output.jpg", edges)