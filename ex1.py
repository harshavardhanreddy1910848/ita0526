import cv2

# Read the image (use raw string for Windows path)
image = cv2.imread(r"H:\Untitled.PNG")

# Check if image loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully")

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display grayscale image
    cv2.imshow("Grayscale Image", gray_image)

    # Wait for key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save grayscale image
    cv2.imwrite(r"H:\gray_output.jpg", gray_image)
    print("Grayscale image saved successfully")