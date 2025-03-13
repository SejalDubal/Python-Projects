from tkinter import *
from tkinter import filedialog, messagebox
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import speech_recognition as sr
from moviepy.editor import VideoFileClip
import os
import hashlib

# AES requires a key of 16, 24, or 32 bytes
key = b'Sixteen byte key'
block_size = AES.block_size

# Global variables for login/signup screens
signup_screen = None
login_screen = None
reg_username = None
reg_password = None
login_username = None
login_password = None

def save_message(message):
    with open('message.txt', 'w') as f:
        f.write(message)
    messagebox.showinfo("Saved", "Message saved to 'message.txt'!")

def load_message():
    try:
        with open('message.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "No saved message found.")
        return ""

def get_message_hash(message):
    return hashlib.sha256(message.encode('utf-8')).hexdigest()

def verify_message(message, provided_hash):
    return get_message_hash(message) == provided_hash

def copy_to_clipboard(hash_value):
    screen.clipboard_clear()
    screen.clipboard_append(hash_value)
    messagebox.showinfo("Copied", "Hash copied to clipboard!")

def encrypt():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END).strip().encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(message, AES.block_size))
        iv = cipher.iv
        ct = base64.b64encode(iv + ct_bytes).decode('utf-8')
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x300")
        screen1.configure(bg="#ed3833")

        Label(screen1, text="ENCRYPT", font="Arial 12", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, ct)

        # Compute and display the hash of the original message
        message_hash = get_message_hash(message.decode('utf-8'))
        Label(screen1, text=f"Message Hash: {message_hash}", font="Arial 10", fg="white", bg="#ed3833").place(x=10, y=200)

        # Add a Copy Hash button
        Button(screen1, text="Copy Hash", command=lambda: copy_to_clipboard(message_hash)).place(x=10, y=230)

        # Add Save Message button
        Button(screen1, text="Save Message", command=lambda: save_message(ct)).place(x=100, y=230)
    elif password == "":
        messagebox.showerror("Encryption", "Input password")
    else:
        messagebox.showerror("Invalid", "Invalid Password")

def decrypt():
    password = code.get()
    if password == "1234":
        try:
            encrypted_message = text1.get(1.0, END).strip()
            raw = base64.b64decode(encrypted_message)
            iv = raw[:AES.block_size]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size).decode('utf-8')

            screen2 = Toplevel(screen)
            screen2.title("Decryption")
            screen2.geometry("400x300")
            screen2.configure(bg="#00bd56")

            Label(screen2, text="DECRYPT", font="Arial 12", fg="white", bg="#00bd56").place(x=10, y=0)

            text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, pt)

            # Display the hash of the decrypted message
            message_hash = get_message_hash(pt)
            Label(screen2, text=f"Message Hash: {message_hash}", font="Arial 10", fg="white", bg="#00bd56").place(x=10, y=200)
            # Add a Copy Hash button
            Button(screen2, text="Copy Hash", command=lambda: copy_to_clipboard(message_hash)).place(x=10, y=230)

            # Add Save Message button
            Button(screen2, text="Save Message", command=lambda: save_message(pt)).place(x=100, y=230)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Invalid", "Invalid Password")

def verify_hash():
    message = text1.get(1.0, END).strip()
    provided_hash = hash_entry.get().strip()
    if verify_message(message, provided_hash):
        messagebox.showinfo("Verification", "The message hash matches!")
    else:
        messagebox.showerror("Verification", "The message hash does not match!")

def reset():
    code.set("")
    text1.delete(1.0, END)
    hash_entry.delete(0, END)

def load_saved_message():
    loaded_message = load_message()
    if loaded_message:
        text1.delete(1.0, END)
        text1.insert(END, loaded_message)

def audio_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            Label(screen, text="Listening...", fg="black", font=("Calibri", 13)).place(x=10, y=350)
            audio_data = recognizer.listen(source)
            text = recognizer.recognize_google(audio_data)
            text1.insert(END, text)
            Label(screen, text="Listening completed.", fg="black", font=("Calibri", 13)).place(x=10, y=350)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Google Speech Recognition could not understand audio")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results from Google Speech Recognition service")

def video_to_text():
    try:
        # Extract audio from video
        video = VideoFileClip("video/Cryptography.mp4")
        audio = video.audio
        audio_file = "extracted_audio.wav"
        audio.write_audiofile(audio_file)

        # Convert audio to text
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

            # Insert the extracted text into the text widget
            text1.insert(END, text)

        # Cleanup: Remove the temporary audio file
        os.remove(audio_file)

    except sr.UnknownValueError:
        messagebox.showerror("Error", "Google Speech Recognition could not understand the audio")
    except sr.RequestError:
        messagebox.showerror("Error", "Could not request results from Google Speech Recognition service")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def encrypt_file():
    filename = filedialog.askopenfilename(title="Select a file to encrypt")
    if filename:
        try:
            with open(filename, 'rb') as file:
                plaintext = file.read()
            # Create AES cipher object and encrypt the data
            cipher = AES.new(key, AES.MODE_CBC)
            ciphertext = cipher.encrypt(pad(plaintext, block_size))
            iv = cipher.iv

            # Combine IV and ciphertext, then encode in base64
            encrypted_data = base64.b64encode(iv + ciphertext)

            # Save encrypted data to a new file
            enc_filename = filename + ".enc"
            with open(enc_filename, 'wb') as enc_file:
                enc_file.write(encrypted_data)

            messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as {enc_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during encryption: {e}")

def decrypt_file():
    enc_filename = filedialog.askopenfilename(title="Select a file to decrypt", filetypes=[("Encrypted files", "*.enc")])
    if enc_filename:
        try:
            with open(enc_filename, 'rb') as enc_file:
                encrypted_data = base64.b64decode(enc_file.read())

            # Extract IV and ciphertext
            iv = encrypted_data[:block_size]
            ciphertext = encrypted_data[block_size:]

            # Create AES cipher object with the extracted IV and decrypt the data
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), block_size)

            # Save decrypted data to a new file
            dec_filename = enc_filename.replace('.enc', '_decrypted')
            with open(dec_filename, 'wb') as dec_file:
                dec_file.write(plaintext)

            messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as {dec_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during decryption: {e}")

def encrypt_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        try:
            with open(file_path, 'rb') as f:
                data = f.read()

            iv = os.urandom(block_size)  # Generate a random IV
            cipher = AES.new(key, AES.MODE_CBC, iv)
            encrypted_data = cipher.encrypt(pad(data, block_size))

            # Save the encrypted image
            encrypted_file_path = file_path + "_encrypted"
            with open(encrypted_file_path, 'wb') as ef:
                ef.write(iv + encrypted_data)  # Save IV + encrypted data

            messagebox.showinfo("Success", f"Image encrypted successfully! Saved as {encrypted_file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during encryption: {e}")

def decrypt_image():
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*_encrypted")])
    if file_path:
        try:
            with open(file_path, 'rb') as ef:
                iv = ef.read(block_size)  # Read the first block size bytes for IV
                encrypted_data = ef.read()  # Read the remaining bytes for the encrypted data

            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted_data = unpad(cipher.decrypt(encrypted_data), block_size)

            # Determine the original file extension
            base_path, _ = os.path.splitext(file_path.replace("_encrypted", ""))
            original_extension = os.path.splitext(file_path.replace("_encrypted", ""))[1]
            if not original_extension:  # Default to .png if extension is missing
                original_extension = '.png'

            # Save decrypted image with the original extension
            decrypted_file_path = f"{base_path}_decrypted{original_extension}"
            with open(decrypted_file_path, 'wb') as df:
                df.write(decrypted_data)

            messagebox.showinfo("Success", f"Image decrypted successfully! Saved as {decrypted_file_path}")

        except (ValueError, KeyError):
            messagebox.showerror("Decryption Failed", "Decryption failed: incorrect key or corrupted data.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during decryption: {e}")

def register():
    username = reg_username.get()
    password = reg_password.get()

    if username and password:
        with open("users.txt", "a") as file:
            file.write(f"{username},{hashlib.sha256(password.encode()).hexdigest()}\n")
        messagebox.showinfo("Registration Successful", "You have been registered successfully!")
        reg_username.set("")
        reg_password.set("")
    else:
        messagebox.showerror("Error", "Please enter both username and password.")

def login():
    username = login_username.get()
    password = login_password.get()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open("users.txt", "r") as file:
        users = file.readlines()
        for user in users:
            user_info = user.strip().split(',')
            if user_info[0] == username and user_info[1] == hashed_password:
                messagebox.showinfo("Login Successful", "Welcome back!")
                screen.deiconify()
                login_screen.withdraw()
                return
    messagebox.showerror("Login Failed", "Incorrect username or password.")

def show_signup():
    login_screen.withdraw()
    signup_screen.deiconify()

def show_login():
    signup_screen.withdraw()
    login_screen.deiconify()

def create_signup_screen():
    global signup_screen, reg_username, reg_password
    signup_screen = Toplevel(screen)
    signup_screen.title("Signup")
    signup_screen.geometry("400x300")
    signup_screen.configure(bg="#d9d9d9")

    reg_username = StringVar()
    reg_password = StringVar()

    Label(signup_screen, text="Signup", font=("Arial", 14), bg="#d9d9d9").pack(pady=10)
    Label(signup_screen, text="Username", font=("Arial", 10), bg="#d9d9d9").pack()
    Entry(signup_screen, textvariable=reg_username).pack(pady=5)
    Label(signup_screen, text="Password", font=("Arial", 10), bg="#d9d9d9").pack()
    Entry(signup_screen, textvariable=reg_password, show='*').pack(pady=5)
    Button(signup_screen, text="Register", command=register).pack(pady=10)
    Button(signup_screen, text="Go to Login", command=show_login).pack()

def create_login_screen():
    global login_screen, login_username, login_password
    login_screen = Toplevel(screen)
    login_screen.title("Login")
    login_screen.geometry("400x300")
    login_screen.configure(bg="#d9d9d9")

    login_username = StringVar()
    login_password = StringVar()

    Label(login_screen, text="Login", font=("Arial", 14), bg="#d9d9d9").pack(pady=10)
    Label(login_screen, text="Username", font=("Arial", 10), bg="#d9d9d9").pack()
    Entry(login_screen, textvariable=login_username).pack(pady=5)
    Label(login_screen, text="Password", font=("Arial", 10), bg="#d9d9d9").pack()
    Entry(login_screen, textvariable=login_password, show='*').pack(pady=5)
    Button(login_screen, text="Login", command=login).pack(pady=10)
    Button(login_screen, text="Go to Signup", command=show_signup).pack()

def main_screen():
    global screen, code, text1, hash_entry

    screen = Tk()
    screen.geometry("1000x600")
    screen.title("AES Encryption/Decryption")
    screen.configure(bg="#d9d9d9")

    Label(text="Enter text for encryption or decryption", fg="black", font=("Calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 12", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=40, width=980, height=200)

    Label(text="Enter secret key", fg="black", font=("Calibri", 13)).place(x=10, y=260)
    code = StringVar()
    Entry(textvariable=code, width=20, bd=1, font=("Arial", 13), show="*").place(x=180, y=260)

    Label(text="Enter hash for verification", fg="black", font=("Calibri", 13)).place(x=10, y=300)
    hash_entry = Entry(width=80, bd=1, font=("Arial", 10))
    hash_entry.place(x=200, y=300)

    Button(text="Encrypt", height=2, width=20, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=380)
    Button(text="Decrypt", height=2, width=20, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=180, y=380)
    Button(text="Reset", height=2, width=20, bg="#1089ff", fg="white", bd=0, command=reset).place(x=350, y=380)
    Button(text="Audio to Text", height=2, width=20, bg="#ffbd33", fg="white", bd=0, command=audio_to_text).place(x=520, y=380)
    Button(text="Verify Hash", height=2, width=20, bg="#d1ff33", fg="black", bd=0, command=verify_hash).place(x=690, y=380)
    Button(text="Video to Text", height=2, width=20, bg="#6a33ff", fg="white", bd=0, command=video_to_text).place(x=860, y=380)
    Button(text="Encrypt File", height=2, width=20, bg="#d633ff", fg="white", bd=0, command=encrypt_file).place(x=10, y=450)
    Button(text="Decrypt File", height=2, width=20, bg="#ff33d6", fg="white", bd=0, command=decrypt_file).place(x=180, y=450)
    Button(text="Encrypt Image", height=2, width=20, bg="#53868B", fg="white", bd=0, command=encrypt_image).place(x=350, y=450)
    Button(text="Decrypt Image", height=2, width=20, bg="#7FFF00", fg="white", bd=0, command=decrypt_image).place(x=520, y=450)
    Button(text="Load Message", height=2, width=20, bg="#33ffb8", fg="black", bd=0, command=load_saved_message).place(x=350, y=520)

    create_signup_screen()
    create_login_screen()

    screen.withdraw()  # Start with the main screen hidden
    signup_screen.withdraw()  # Start with the signup screen hidden
    login_screen.deiconify()  # Show the login screen

    screen.mainloop()

# Run the program
main_screen()

