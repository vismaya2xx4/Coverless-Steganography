
# 🛡️ Secure Image Hashing & Steganography Toolkit

This project demonstrates the integration of cryptographic hashing using **SIFT descriptors** and **Least Significant Bit (LSB) steganography** to build a simple system for secure image handling, covert communication, and data hiding.

---

## 📌 Features

- 🔍 **Image Hashing using SIFT Descriptors**
- 🗃️ **Image Database Storage using Hash**
- 🔐 **Binary Data Embedding using LSB**
- 🔓 **Data Extraction from Stego Images**
- 🖼️ **Supports Grayscale Image Processing**

---

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV (cv2)**
- **NumPy**

---

## 🔐 Cryptographic Method: SIFT Hashing

- **Tool Used**: SIFT (Scale-Invariant Feature Transform) from OpenCV.
- **Working**:
  - Convert the image to grayscale.
  - Compute keypoints and descriptors using `cv2.SIFT_create()`.
  - Generate a simple hash using the **number of descriptors**.
  - Store the image in a dictionary using this hash as the key.

> Note: This is a basic form of hashing based on feature detection. For production, consider using SHA-256 or image perceptual hashes for better uniqueness and collision resistance.

---

## 🕵️‍♂️ Steganography Method: LSB (Least Significant Bit)

- **Method**: Embed secret binary data into the **least significant bit** of pixel values in a grayscale image.
- **Process**:
  - The secret message is converted into a binary string.
  - One bit is inserted into the LSB of each pixel.
  - The process continues until the entire message is embedded.
- **Extraction**:
  - Read LSBs of pixels sequentially.
  - Reconstruct the secret binary message.

---

## 📂 Folder Structure

```
├── main.py                 # Main script containing logic
├── df1.jpg, df2.jpg ...    # Input images
├── stego_image.jpg         # Output image with hidden data
├── README.md               # Project documentation
```

---

## 🚀 How to Run

1. **Install Dependencies**
   ```bash
   pip install opencv-python numpy
   ```

2. **Place Your Images**
   - Add your images in the same directory as `main.py`.
   - Update the `image_paths` list accordingly.

3. **Run the Script**
   ```bash
   python main.py
   ```

4. **Check Output**
   - `stego_image.jpg` will contain the hidden message.
   - Console will show the extracted binary message.

---

## 📋 Example

```python
# Embedding
secret_data = "11111111111"
stego_image = embed_data_into_image(selected_image, secret_data)

# Extraction
extracted = extract_data_from_image(stego_image, len(secret_data))
```

---

## 🧠 Applications

- ✔️ Secure watermarking
- ✔️ Digital signature validation
- ✔️ Data hiding in images
- ✔️ Tamper detection
- ✔️ Cybersecurity training and demonstration

---

## ⚠️ Limitations

- Hashing method (based on descriptor count) is **not unique**; collisions possible.
- Only supports **grayscale images** for LSB encoding.
- Binary message embedding only; no string/ASCII support directly.

---

## 📌 Future Enhancements

- Use **SHA-256** or **perceptual hashing** for image uniqueness.
- Add **AES encryption** for secret data before embedding.
- Expand to **RGB images** for increased data capacity.
- Add GUI for user-friendly operation.
