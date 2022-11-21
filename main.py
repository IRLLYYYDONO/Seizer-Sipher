# Veriables
from tkinter import *

root = Tk()
root.title("MI6 Encryptor")
root.geometry("600x700")
root.configure(bg="blue")

font = "Arial"

lebal = Listbox(root, height=25, width=50, bg="blue", fg="white", bd=5, selectbackground="red")
lebal.grid(row=5, column=2, columnspan=3, pady=10)

Sipher_Array_Lower_Case = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z',"A","B","C","D",
    "E","F","G","H","I","J","K","L","M","N", 
    "O","P","Q","R","S","T","U","V","W","X",
    "Y","Z","1","2","3","4","5","6","7","8",
    "9","0"
]

message = ""
shift = 0
encrypted_message = ""
decrypt_message = ""
num_temp = 0

# Functions
def Show_message(going_to_show_message = ""):
    lebal.insert(END, f"{lebal.size() + 1}: {going_to_show_message}")

def Encrypt(Orriginal_Meassage = "", Shift_Encrypt = int):
    for x in range(len(Orriginal_Meassage)):
        global encrypted_message
        char = Orriginal_Meassage[x]
        if not char in Sipher_Array_Lower_Case: 
            encrypted_message += char
        else: 
            num = (Sipher_Array_Lower_Case.index(char) + Shift_Encrypt) % 62
            encrypted_message += Sipher_Array_Lower_Case[num]
    
    Show_message(str(encrypted_message))
    encrypted_message = ""

def Decrypt(Encrypted_Meassage = "", Shift_Decrypt = int):
    if Encrypted_Meassage != "" and Shift_Decrypt != 0:
        for x in range(len(Encrypted_Meassage)):
            global decrypt_message
            char = Encrypted_Meassage[x]
            if not char in Sipher_Array_Lower_Case: 
                decrypt_message += char
            else: 
                num = (Sipher_Array_Lower_Case.index(char) - Shift_Decrypt) % 62 # E_{n}(x)= ( x + n ) mod 26 (26 is the amount of characters you have in the dictionary, dont change it) I hate math, 
                decrypt_message += Sipher_Array_Lower_Case[num]                  #took me a long time to realize this equation from wikipedia, fuck u all https://en.wikipedia.org/wiki/Caesar_cipher, joking im just mad that it took me all this time to realize it, im dumb lmao
    
    Show_message(str(decrypt_message))
    decrypt_message = ""
    
# UI
main_lebel = Label(root, text="MI6 GPE - Version 3.32a", background="Blue", foreground="Yellow", font=("Times New Roman Bold", 25))

shift_lebel = Label(root, text="Shift: ", background="blue", foreground="white", font=("Arial Bold", 15))
message_lebel = Label(root, text="Message: ", background="blue", foreground="white", font=("Arial Bold", 15))

encrypt_button = Button(root, text="Enter Your Message", command= lambda: Encrypt(message_entry.get(), int(shift_entry.get())), background="blue", foreground="blue", font=("Arial Bold", 20))

shift_entry = Entry(root, width=50, background="blue", foreground="white", font=(font))
message_entry = Entry(root, width=50, background="blue", foreground="white", font=(font))

main_lebel.grid(row=1, column=2, pady=10, padx=10)

message_lebel.grid(row=2, column=1, pady=10)
shift_lebel.grid(row=3, column=1)

message_entry.grid(row=2, column=2)
shift_entry.grid(row=3, column=2)

encrypt_button.grid(row=4, column=2, pady=10)

root.mainloop()