import cv2
import numpy as np

# Function to compute SIFT-based hash for an image
def compute_sift_hash(image_path):
    try:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        sift = cv2.SIFT_create()
        keypoints, descriptors = sift.detectAndCompute(img, None)
        # Calculate a simple hash based on descriptor count (you can enhance this)
        hash_value = len(descriptors)
        return hash_value
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Function to add an image to the image database
def add_image_to_database(image_path, database):
    hash_value = compute_sift_hash(image_path)
    if hash_value is not None:
        database[hash_value] = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        print(f"Image added to the database with hash value: {hash_value}")

# Function to embed secret data into an image using LSB
def embed_data_into_image(image, secret_data):
    stego_image = image.copy()
    secret_data = str(secret_data)
    data_length = len(secret_data)
    data_index = 0

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            pixel_value = image[y, x]
            if data_index < data_length:
                # Embed one bit of data in the least significant bit (LSB) of the pixel value
                pixel_value = (pixel_value & 254) | int(secret_data[data_index])
                stego_image[y, x] = pixel_value
                data_index += 1
            else:
                break

    return stego_image

# Function to extract secret data from an image using LSB
def extract_data_from_image(image, data_length):
    extracted_data = ""
    data_index = 0

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            pixel_value = image[y, x]
            # Extract one bit of data from the LSB of the pixel value
            extracted_bit = pixel_value & 1
            extracted_data += str(extracted_bit)
            data_index += 1
            if data_index == data_length:
                return extracted_data

    return extracted_data

# Create an empty image database (dictionary)
image_database = {}

# Paths to your images
image_paths = ["df1.jpg", "df2.jpg", "df3.jpg","wallpaper.jpg"]  # Add paths to your images

# Add each image to the image database
for image_path in image_paths:
    add_image_to_database(image_path, image_database)

# Secret data to be embedded
secret_data = "11111111111"
print('sec_length = ',len(secret_data))

# Choose a random hash value from the secret data to find a corresponding image
chosen_hash = int(secret_data[:80000], 2)
selected_image = image_database.get(212)

if selected_image is None:
    print("Image not found in the database.")
else:
    stego_image = embed_data_into_image(selected_image, secret_data)
    cv2.imwrite("stego_image.jpg", stego_image)  # Save the stego image
    print("Stego image saved successfully.")
    stego_image = embed_data_into_image(selected_image, secret_data)
    cv2.imwrite("stego_image.jpg", stego_image)

# Extract data from the stego image
stego_image = embed_data_into_image(selected_image, secret_data)
cv2.imwrite("stego_image.jpg", stego_image)

extracted_data = extract_data_from_image(stego_image, len(secret_data))
print("Extracted data:", extracted_data)
print('ext_length = ',len( extracted_data))

