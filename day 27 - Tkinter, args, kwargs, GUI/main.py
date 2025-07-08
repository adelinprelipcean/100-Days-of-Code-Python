import tkinter
import turtle

def button_clicked():
    label_2 = tkinter.Label()
    label_2.pack()
    label_2.config(text=f"Distance of {user_input.get()} miles is {int(user_input.get())*1.6} km.")

window = tkinter.Tk()
window.title("GUI Converter")
window.minsize(400, 500)

label_1 = tkinter.Label()
label_1.pack()
label_1.config(text="Insert distance in miles", font=("Arial", 16))

user_input = tkinter.Entry()
user_input.pack()
user_input.config(width=10)

button_1 = tkinter.Button()
button_1.pack()
button_1.config(text="Convert", bg="lightblue", command=button_clicked)

window.mainloop()
    
    
    
    
    
    
    
    
    
# # def add(*args):
# #     sum = 0
# #     for n in args:
# #         sum += n
# #     return sum  
# # print(add(1,2,3,4,5,6))

# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# calculate(2, add=8, multiply=5)

# class Car:
    
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make", "Volvo")
#         self.model = kwargs.get("model", "S60")
#         self.year = kwargs.get("year", "2005")
#         self.color = kwargs.get("color", "Black")
        
#     def print(self):
#         print(f"Make - {self.make} : Model - {self.model} : Year - {self.year} : Color - {self.color}")
        
# my_car = Car(make="BMW", model="3 Series", year="2007")
# my_car.print()