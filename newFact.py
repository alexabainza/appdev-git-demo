from tkinter import *
from math import sqrt

#################################### FUNCTION DEFINITIONS ####################################
# function to calculate factorial of a number

def clicked_factorial():
    try:
        num = int(input.get())
        if(num<0):
            factorial_result.configure(text="Factorial for negative numbers are not defined")
        else:
            res =  1
            for i in range(2, num+1):
                res *= i
            factorial_result.configure(text=f"Factorial of {num} is {res}")
    except ValueError:
        factorial_result.configure(text = "Can't process float or string inputs!")

# function to clear input and results
def clearInput():
    input.delete(0, END)
    factorial_result.configure(text="")
    prime_result.configure(text="")

# function to check if number is prime or not
def clicked_prime():
    try:
        num = int(input.get())
        if num <= 1:
            prime_result.configure(text=f"{num} is not prime")
        else:
            is_prime = all(num % i != 0 for i in range(2, int(sqrt(num)) + 1))
            prime_result.configure(text=f"{num} is {'prime' if is_prime else 'not prime'}")
    except ValueError:
        prime_result.configure(text = "Can't process float or string inputs!")

def display_greeting():
    name = name_input.get().strip()
    if name:
        greeting_label.configure(text=f"Hello, {name}!")
    else:
        greeting_label.configure(text="Please enter your name.")


#################################### GUI LAYOUT ####################################

root = Tk()

root.title("CHECK IF PRIME AND FACTORIAL")
root.geometry('550x300')

root.configure(bg='lightblue', padx=20, pady=20)

# prompt, input, and clear button will be displayed beside each other
prompt = Label(root, text = "Input a number", bg='lightblue', width=15, anchor="w")
prompt.grid(column=0, row=0,)

input = Entry(root, width=20,)
input.grid(column=1, row=0,)

#Layout for the clear button
btnClear = Button(root, text="Clear", command=clearInput,width=10,)
btnClear.grid(column=2, row=0, pady=(10, 0), sticky=W, padx=(10, 0))

# Layout for the calculate factorial button and result, they will be displayed beside each other
factorial_result = Label(root, text="", bg='lightblue', width=40, anchor="w")
factorial_result.grid(column=1, row=5)
btnFactorial = Button(root, text="Find Factorial", command=clicked_factorial,)
btnFactorial.grid(column=0, row=5, pady=(10, 0),  sticky=W, padx=(10, 0))
# Greeting section
name_label = Label(root, text="Enter your name:", bg='lightblue', width=15, anchor="w")
name_label.grid(column=0, row=11)

name_input = Entry(root, width=20)
name_input.grid(column=0, row=12)

greet_button = Button(root, text="Greet", command=display_greeting, width=10)
greet_button.grid(column=0, row=13, padx=(10, 0))

greeting_label = Label(root, text="", bg='lightblue', width=40, anchor="w")
greeting_label.grid(column=1, row=11, columnspan=2)

# Layout for the is prime button and result, they will be displayed beside each other
prime_result = Label(root, text="", bg='lightblue', width=40, anchor='w')
prime_result.grid(column=1, row=6)
btnPrime = Button(root, text="Is prime?", command=clicked_prime,width=10)
btnPrime.grid(column=0, row=6, pady=(10, 0), sticky=W, padx=(10, 0))

root.mainloop()  # Start the Tkinter event loop
