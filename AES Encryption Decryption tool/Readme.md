# AES Encryption/Decryption Tool with Audio/Video Support

This project is a Python-based application that provides **AES encryption and decryption** functionality. It also supports **audio-to-text** and **video-to-text** conversion using the `speech_recognition` and `moviepy` libraries. The application is built using the `tkinter` library for the graphical user interface (GUI).

## Features
- **AES Encryption/Decryption**:
  - Encrypt and decrypt text using AES (Advanced Encryption Standard).
  - Supports 16-byte keys for encryption and decryption.
- **Audio-to-Text Conversion**:
  - Convert speech from a microphone input to text using Google Speech Recognition.
- **Video-to-Text Conversion**:
  - Extract audio from a video file and convert it to text.
- **File Encryption/Decryption**:
  - Encrypt and decrypt files (e.g., text files, images).
- **Hash Verification**:
  - Verify the integrity of messages using SHA-256 hashes.
- **User Authentication**:
  - Simple login and signup system for user authentication.

## Prerequisites
- Python 3.x
- Required Python libraries:
  - `pycryptodome` (for AES encryption/decryption)
  - `speech_recognition` (for audio-to-text conversion)
  - `moviepy` (for video-to-text conversion)
  - `pyaudio` (optional, for microphone input)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/aes-encryption-tool.git
   cd aes-encryption-tool
**Install Dependencies**:
Install the required Python libraries using pip:

   ```bash
   pip install pycryptodome SpeechRecognition moviepy pyaudio
```
*If you encounter issues installing pyaudio, you can download a precompiled binary from PyAudio's unofficial binaries.*

### Run the Application:
Run the Python script to start the application:

```bash
Copy
python main.py
```
## How to Use

- Encrypt/Decrypt Text:
 Enter the text you want to encrypt or decrypt in the text box.
 Enter the secret key (default key is 1234).
 Click Encrypt or Decrypt to perform the operation.
- Audio-to-Text Conversion:
 Click Audio to Text to start recording from your microphone.
 The recognized text will be displayed in the text box.
- Video-to-Text Conversion:
  Place your video file in the video/ folder (e.g., video/Cryptography.mp4).
  Click Video to Text to extract audio from the video and convert it to text.
- File Encryption/Decryption:
  Click Encrypt File or Decrypt File to encrypt or decrypt a file.
  Select the file from the file dialog.
- Image Encryption/Decryption:
  Click Encrypt Image or Decrypt Image to encrypt or decrypt an image file.
  Select the image from the file dialog.
- Hash Verification:
 Enter the hash of the message in the hash field.
 Click Verify Hash to check if the message matches the provided hash.
- User Authentication:
 Use the Signup and Login buttons to register and log in.

**Acknowledgments**
- pycryptodome for AES encryption/decryption.
- SpeechRecognition for audio-to-text conversion.
- moviepy for video-to-text conversion.

## User Interface: 
### Signup & Login Functionality: 
**0. Signup (Registration)** 
Purpose: To create a new user account by collecting a username and password. 
The password is securely hashed before being stored to ensure security. 
Process: 
**1. Input Collection:**
- Username: Users provide a unique username. 
- Password: Users provide a password, which is then hashed. 
**2. Password Hashing:**
- The password is hashed using the SHA-256 algorithm to ensure it 
is stored securely. Hashing transforms the password into a fixed
size string that is not reversible. 
- The hashed password is stored in a file or a database alongside the 
username. 
**3. File Handling:** 
 -Registration File: A file is used to store usernames and their 
corresponding hashed passwords. This file is checked during login 
to verify credentials. 
**4. User Feedback:**
- The tool provides feedback to users on the success or failure of the 
registration process, typically via messages in the user interface.

![image](https://github.com/user-attachments/assets/42c4f32b-0d85-4aa1-9a32-5499945ef351)

## 2. Login (Authentication) 
Purpose: To verify the credentials of a user trying to access the tool. This 
involves checking the provided username and password against the stored 
hashed credentials. 
- Process: 
**1. Input Collection:**
- Username: Users enter their username. 
- Password: Users enter their password. 
**2. Password Hashing:**
  - The entered password is hashed using the same SHA-256 
algorithm. 
**3. Credential Verification:**
- The tool reads the stored usernames and hashed passwords from 
the file. 
- It compares the hashed version of the entered password with the 
stored hash for the provided username. 
**4. User Feedback:**
  - The tool informs the user whether the login was successful or if 
there was an error, such as incorrect credentials. 

### After logging in, users can access various functionalities of the tool. 
• *Encrypt:* Encrypts a text message using AES encryption with a user
provided key. 
• *Decrypt:* Decrypts an encrypted text message using AES decryption with 
a user-provided key. 
• *Reset:* Clears all input fields and resets the state of the application. 
• *Audio to Text:* Converts spoken audio from a microphone into text using 
speech recognition. 
• *Verify Hash:* Compares the hash of a message with a provided hash to 
verify integrity. 
• *Video to Text:* Extracts audio from a video file and converts it to text 
using speech recognition. 
• *Encrypt File:* Encrypts a selected file using AES encryption. 
• *Decrypt File:* Decrypts an encrypted file using AES decryption. 
• *Encrypt Image:* Encrypts a selected image file using AES encryption. 
• *Decrypt Image:* Decrypts an encrypted image file using AES decryption. 
• *Load Message:* Loads a previously saved encrypted or decrypted 
message from a file into the text field.

![image](https://github.com/user-attachments/assets/531ccf4b-3e4e-490f-bb07-52d08b25a9b1)
