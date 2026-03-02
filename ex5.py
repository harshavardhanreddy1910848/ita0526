import cv2
import numpy as np
from matplotlib import pyplot as plt

def analyze_histogram(image_path):
    # Read the image
    image = cv2.imread(r"H:\Untitled.PNG")

    # Check if image loaded successfully
    if image is None:
        print("Error: Image not found!")
        return

    # Split into BGR channels
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')

    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")

    # Plot histogram for each channel
    for channel, color in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)

    plt.xlim([0, 256])
    plt.show()

# Call function with path
analyze_histogram(r"H:\Untitled.PNG")