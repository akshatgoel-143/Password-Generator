from tkinter import *
import string
import random


def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers= string.digits
    special_char = string.punctuation

    all_char = small_alphabets+capital_alphabets+numbers+special_char
    password_len= int(password_length_input.get())   

    password = random.sample(all_char, password_len)
    print(password)

    generated_pass.delete(0,"end")
    generated_pass.insert(0,password)


def clear():
    password_length_input.delete(0,"end")
    generated_pass.delete(0,"end")
    user_name_input.delete(0,"end")


root=Tk()
root.geometry("450x350")
root.title("Password Generator")

passlebel= Label(root, text="Password Generator",font=("times new roman", 18, "bold"))
passlebel.pack()

user_name = Label(root, text = "Enter Username:", font=("times new roman", 14))
user_name.place(x = 30, y = 60) 
   
length = Label(root, text = "Enter Password Length:", font=("times new roman", 14))
length.place(x = 30,y = 100) 

password = Label(root, text = "Generated Password:", font=("times new roman", 14,))
password.place(x = 30,y = 140) 

user_name_input = Entry(root, width = 30)
user_name_input.place(x = 220,y = 60) 
   
password_length_input = Entry(root, width = 30)
password_length_input.place(x = 220, y = 100)

generated_pass = Entry(root, width = 30, fg="red")
generated_pass.place(x = 220, y = 140)
   
generate_btn = Button(root, text = "Generate password", font=("times new roman", 14),pady=10, command=generator)
generate_btn.pack(anchor= CENTER)
generate_btn.place(x=125,y=200)

generate_btn = Button(root, text = "Reset", font=("times new roman", 14), command=clear)
generate_btn.pack(anchor= CENTER)
generate_btn.place(x=180,y=270)

root.mainloop()