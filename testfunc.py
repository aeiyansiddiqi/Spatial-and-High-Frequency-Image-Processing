import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# Step 1: Apply the Fast Fourier Transform (FFT)
image_float = np.float32(image)
f = np.fft.fft2(image_float)
fshift = np.fft.fftshift(f)

# Step 2: Create a Circular Mask using loops
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2  # center of the image
radius = 30  # Radius of the circular low-frequency region to remove

# Initialize the mask with ones (keeping all frequencies)
mask = np.ones((rows, cols), np.uint8)

# Loop over each pixel in the frequency domain
for i in range(rows):
    for j in range(cols):
        # Calculate the distance from the center (crow, ccol)
        distance = np.sqrt((i - crow)**2 + (j - ccol)**2)
        
        # If the distance is less than or equal to the radius, set it to 0 (inside the circle)
        if distance <= radius:
            mask[i, j] = 0

# Step 3: Apply the mask to the FFT image
fshift_masked = fshift * mask

# Step 4: Apply the inverse FFT to bring the image back to the spatial domain
f_ishift = np.fft.ifftshift(fshift_masked)
image_filtered = np.fft.ifft2(f_ishift)
image_filtered = np.abs(image_filtered)

# Step 5: Display the results
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Image after high-pass filtering (with center carved out)
plt.subplot(1, 2, 2)
plt.imshow(image_filtered, cmap='gray')
plt.title("Filtered Image (High-Pass)")
plt.axis('off')

plt.show()
