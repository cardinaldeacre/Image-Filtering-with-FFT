import cv2
import numpy as np

def apply_frequency_filter(image_path, filter_type='low', radius=30):

    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if original_image is None:
        print(f"Error: Tidak dapat membuka gambar di path: {image_path}")
        return None, None

    f_transform = np.fft.fft2(original_image)
    f_transform_shifted = np.fft.fftshift(f_transform)

    rows, cols = original_image.shape
    crow, ccol = rows // 2, cols // 2  

    mask = np.zeros((rows, cols), np.uint8)
    
    if filter_type == 'low':
        cv2.circle(mask, (ccol, crow), radius, 1, thickness=-1)
    elif filter_type == 'high':
        mask = np.ones((rows, cols), np.uint8)
        cv2.circle(mask, (ccol, crow), radius, 0, thickness=-1)
    else:
        raise ValueError("filter_type harus 'low' atau 'high'")

    f_transform_shifted_filtered = f_transform_shifted * mask

    f_ishift = np.fft.ifftshift(f_transform_shifted_filtered)

    img_back = np.fft.ifft2(f_ishift)
    filtered_image = np.abs(img_back)

    return original_image, filtered_image
    
