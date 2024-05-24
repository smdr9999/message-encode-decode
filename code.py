
#import required packages
from tkinter import *
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

# Initialize window
root = Tk()
root.geometry('1000x500')
#root.iconbitmap('icon.ico')
root.title("Message Encode and Decode")

# Set window to full screen

root.attributes("-fullscreen", True)

# Load and set background image
bg_image = PhotoImage(file="bg3.png")
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Define variables
Text = StringVar()
private_key = StringVar()
iv = StringVar()
mode = StringVar()
Result = StringVar()

# Define functions
def encrypt(key, iv, data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    return ciphertext

def decrypt(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

def Mode():
    if mode.get() == 'e':
        key = private_key.get().encode()
        iv_value = iv.get().encode()
        Result.set(encrypt(key, iv_value, Text.get()).hex())
    elif mode.get() == 'd':
        key = private_key.get().encode()
        iv_value = iv.get().encode()
        ciphertext = bytes.fromhex(Text.get())
        Result.set(decrypt(key, iv_value, ciphertext))
    else:
        Result.set('Invalid Mode')

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    iv.set("")
    mode.set("")
    Result.set("")

# Label and Button
Label(root, text='AES ENCRYPTION-DECRYPTION', font='arial 20 bold', bg='white').pack()

Label(root, font='arial 12 bold', text='MESSAGE').place(x=250, y=250)
Entry(root, font='arial 10', textvariable=Text, bg='ghost white').place(x=540, y=250)

Label(root, font='arial 12 bold', text='KEY 32-Byte').place(x=250, y=300)
Entry(root, font='arial 10', textvariable=private_key, bg='ghost white').place(x=540, y=300)

Label(root, font='arial 12 bold', text='INITIALIZATION VECTOR 16-Byte').place(x=250, y=350)
Entry(root, font='arial 10', textvariable=iv, bg='ghost white').place(x=540, y=350)

Label(root, font='arial 12 bold', text='MODE(e-encrypt, d-decrypt)').place(x=250, y=400)
Entry(root, font='arial 10', textvariable=mode, bg='ghost white').place(x=540, y=400)

Entry(root, font='arial 10 bold', state="readonly", textvariable=Result, bg='ghost white').place(x=540, y=460)

Button(root, font='arial 10 bold', text='RESULT',width=8, height=2, padx=2, bg='LightGray', command=Mode).place(x=400, y=450)
Button(root, font='arial 10 bold', text='RESET', width=10, height=2, command=Reset, bg='LimeGreen', padx=2).place(x=350, y=550)
Button(root, font='arial 10 bold', text='EXIT', width=10, height=2, command=Exit, bg='OrangeRed', padx=2, pady=2).place(x=550, y=550)


root.mainloop()
