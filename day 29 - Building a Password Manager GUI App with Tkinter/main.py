import tkinter
import string
import random
import tkinter.messagebox
import pyperclip

def save_account(*args):
    if args[0] != '' and args[1] != '' and args[2] != '' :
        try:
            with open("password.txt", "x") as file:
                file.write("|        SERVICE         |          Email/Username          |        Password         |\n"
                           +"|------------------------|----------------------------------|-------------------------|\n"
                           +f"{' | '.join(args)}\n")
        except:
            with open("password.txt", "a") as file:
                file.write(f"{' | '.join(args)}\n")
        tkinter.messagebox.showinfo("Info", f"Your {args[0].capitalize()} account details are successfully saved!")
        entry_1.delete(0, tkinter.END)
        entry_2.delete(0, tkinter.END)
        entry_3.delete(0, tkinter.END)
        pyperclip.copy(args[2])

    else:
        tkinter.messagebox.showinfo("Error","Complete all the fields!")
        
    
def generate_password():
    entry_3.delete(0, tkinter.END)
    password = ''
    for i in range(16):
        password += random.choice(list(string.ascii_letters)+list(string.digits))
    entry_3.insert(0, password)
    
window = tkinter.Tk()
window.geometry("710x610")
window.configure(bg="grey")
window.title("Password Manager")

canvas = tkinter.Canvas(window, width=500, height=370, bg="gray", highlightthickness=0)
image = tkinter.PhotoImage(file="password.png")
image = image.subsample(2, 2)
canvas.create_image(500 // 2, 720 // 2, image=image, anchor='s')
canvas.grid(row=0, column=1, padx=0, columnspan=2)

label_1 = tkinter.Label(text="Service", font=("Calibri", 16, "bold"), bg="grey")
label_1.grid(row=1, column=0, padx=20, pady=5,)

label_2 = tkinter.Label(text="Email/\nUsername", font=("Calibri", 16, "bold"), bg="grey")
label_2.grid(row=2, column=0, padx=20, pady=5)

label_3 = tkinter.Label(text="Password", font=("Calibri", 16, "bold"), bg="grey")
label_3.grid(row=3, column=0, padx=20, pady=5)


entry_1 = tkinter.Entry(width=67)
entry_1.grid(row=1, column=1, padx=50, columnspan=2, sticky='w')

entry_2 = tkinter.Entry(width=67)
entry_2.grid(row=2, column=1, padx=50, columnspan=2, sticky='w')

entry_3 = tkinter.Entry(width=30, show="*")
entry_3.grid(row=3, column=1, padx=50, columnspan=2, sticky="w")


button_save = tkinter.Button(window,width=35, text="Save", fg="white", bg="#C44030", command=lambda: save_account(entry_1.get(), entry_2.get(), entry_3.get()))
button_save.grid(row=4, column=1, columnspan=2, pady=10)
button_generate = tkinter.Button(window, text="Generate Password", width=28, bg="black", fg="white", command=generate_password)
button_generate.place(x=378, y=487)

window.mainloop()