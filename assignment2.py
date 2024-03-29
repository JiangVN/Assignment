import cv2
import numpy as np
from scipy.fftpack import fft2, fftshift, ifft2
import tkinter as tk
from tkinter import filedialog

def filter_image(image, filter_type):
    # Perform Fourier Transform
    img_ft = fft2(image)
    img_ft_shift = fftshift(img_ft)

    # Create filter
    if filter_type == 'lowpass':
        filter_array = np.zeros(image.shape)
        filter_array[(image.shape[0]//2 - image.shape[0]//5):(image.shape[0]//2 + image.shape[0]//5),
        (image.shape[1]//2 - image.shape[1]//5):(image.shape[1]//2 + image.shape[1]//5)] = 1
    elif filter_type == 'highpass':
        filter_array = np.ones(image.shape)
        filter_array[(image.shape[0]//2 - image.shape[0]//5):(image.shape[0]//2 + image.shape[0]//5),
        (image.shape[1]//2 - image.shape[1]//5):(image.shape[1]//2 + image.shape[1]//5)] = 0

    # Apply filter
    filtered_img_ft = img_ft_shift * filter_array

    # Perform inverse Fourier Transform
    filtered_img = np.abs(ifft2(np.fft.ifftshift(filtered_img_ft)))

    return filtered_img

def browse_file():
    global img
    filename = filedialog.askopenfilename(filetypes=(("Image files", "*.jpg *.jpeg *.png"),("All files", "*.*")))
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

def apply_lowpass_filter():
    global img
    filter_type = 'lowpass' # Set filter type
    filtered_img = filter_image(img, filter_type)

    # Display filtered image
    cv2.imshow('Filtered Image', filtered_img)

    # Wait for a key press and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def apply_highpass_filter():
    global img
    filter_type = 'highpass' # Set filter type
    filtered_img = filter_image(img, filter_type)

    # Display filtered image
    cv2.imshow('Filtered Image', filtered_img)

    # Wait for a key press and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Create GUI
window = tk.Tk()
window.title('Image Filtering Tool')

# Add buttons
browse_button = tk.Button(window, text='Browse Image', command=browse_file)
browse_button.pack()

apply_button = tk.Button(window, text='Apply Filter', command=apply_highpass_filter)
apply_button.pack()

apply_button = tk.Button(window, text='Apply Filter', command=apply_lowpass_filter)
apply_button.pack()

window.mainloop()