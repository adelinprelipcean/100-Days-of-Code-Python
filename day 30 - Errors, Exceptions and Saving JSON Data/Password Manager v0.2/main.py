import tkinter
import string
import random
import tkinter.messagebox
import pyperclip
import json

def show_details(service, email, password, error):
    popup = tkinter.Toplevel(window)
    popup.title(f"{service} Details")
    popup.geometry("300x163")
    popup.configure(bg="lightgrey")
    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = window.winfo_x() + (window.winfo_width() // 2) - (width // 2)
    y = window.winfo_y() + (window.winfo_height() // 2) - (height // 2)
    popup.geometry(f"+{x}+{y}")


    if error == False:
        tkinter.Label(popup, text="Email/Username:", font=("Calibri", 12, "bold"), bg="lightgrey").pack(anchor="w", padx=10, pady=5)
        tkinter.Label(popup, text=email, font=("Calibri", 12), bg="lightgrey").pack(anchor="w", padx=20)

        tkinter.Label(popup, text="Password:", font=("Calibri", 12, "bold"), bg="lightgrey").pack(anchor="w", padx=10, pady=5)
        tkinter.Label(popup, text=password, font=("Calibri", 12), bg="lightgrey").pack(anchor="w", padx=20)

        tkinter.Button(popup, text="OK",width=7, command=popup.destroy).pack(pady=10)
        
    else:
        popup.geometry("300x90")
        
        tkinter.Label(popup, text="No service was found for your entry.", font=("Calibri", 12, "bold"), bg="lightgrey").pack(anchor="w", padx=10, pady=5)
        
        tkinter.Button(popup, text="OK",width=7, command=popup.destroy).pack(pady=10)
        



def save_account(*args):
    if args[0] != '' and args[1] != '' and args[2] != '' :
        new_data = {
            args[0].capitalize(): {
                "email/username": args[1],
                "password": args[2]
        }}
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_1.delete(0, tkinter.END)
            entry_2.delete(0, tkinter.END)
            entry_3.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showinfo("Error","Complete all the fields!")
        

def search():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        if entry_1.get().capitalize() in [key for key in data.keys()]:
            email = data[entry_1.get().capitalize()]["email/username"]
            password = data[entry_1.get().capitalize()]["password"]
            show_details(entry_1.get().capitalize(), email, password, False)
        else:
            show_details(entry_1.get().capitalize(), None, None, True)
            # tkinter.messagebox.showwarning("",f"The details for {entry_1.get().capitalize()} are:\nemail/username: {email}\npassword: {password}")
    
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


entry_1 = tkinter.Entry(width=38)
entry_1.grid(row=1, column=1, padx=50, columnspan=2, sticky='w')

entry_2 = tkinter.Entry(width=67)
entry_2.grid(row=2, column=1, padx=50, columnspan=2, sticky='w')

entry_3 = tkinter.Entry(width=30, show="*")
entry_3.grid(row=3, column=1, padx=50, columnspan=2, sticky="w")


button_save = tkinter.Button(window,width=35, text="Save", fg="white", bg="#C44030", command=lambda: save_account(entry_1.get(), entry_2.get(), entry_3.get()))
button_save.grid(row=4, column=1, columnspan=2, pady=10)

button_generate = tkinter.Button(window, text="Generate Password", width=29, bg="black", fg="white", command=generate_password)
button_generate.place(x=378, y=487)

button_search = tkinter.Button(window, width=22, text="Search",bg="black", fg="white", command=search)
button_search.place(x=427, y=378)

window.mainloop()