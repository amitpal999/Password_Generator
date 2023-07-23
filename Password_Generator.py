from tkinter import *
import string
import random
import pyperclip

def generator():
  small_alphabet=string.ascii_lowercase
  capital_alphabet=string.ascii_uppercase
  numbers=string.digits
  special_characters=string.punctuation

  all=small_alphabet+capital_alphabet+numbers+special_characters

  password_length=int(length_box.get())

  if choice.get()==1:
        password_field.insert(0,random.sample(small_alphabet,password_length))
  if choice.get()==2:
        password_field.insert(0,random.sample(small_alphabet+capital_alphabet,password_length))
  if choice.get()==3:
        password_field.insert(0,random.sample(small_alphabet+capital_alphabet+numbers+special_characters,password_length))

def copy():
     random_password=password_field.get()
     pyperclip.copy(random_password)

#   password=random.sample(all,password_length)
#   password_field.insert(0,password)

obj=Tk()
obj.config(bg="Black")
obj.geometry("250x370")
obj.resizable(0,0)
choice=IntVar()
Font=("Arial",13,"bold")
passwordlabel=Label(obj,text="Password Generator",font=("Times new roman",20,"bold"),bg="black",fg="white")
passwordlabel.grid(pady=10)

simplebutton=Radiobutton(obj,text="Simple",value=1,variable=choice,font=Font)
simplebutton.grid(pady=5)
avergebutton=Radiobutton(obj,text="Average",value=2,variable=choice,font=Font)
avergebutton.grid(pady=5)
advancedbutton=Radiobutton(obj,text="Advanced",value=3,variable=choice,font=Font)
advancedbutton.grid(pady=5)

lengthlabel=Label(obj,text="Password Length",font=Font,bg="black",fg="white")
lengthlabel.grid()

length_box=Spinbox(obj,from_=5,to_=15,width=5,font=Font)
length_box.grid(pady=5)

generate_button=Button(obj,text="Generate",font=Font,command=generator)
generate_button.grid(pady=5)

password_field=Entry(obj,width=20,bd=2,font=Font)
password_field.grid(pady=5)

copy_button=Button(obj,text="Copy",font=Font,command=copy)
copy_button.grid(pady=5)
obj.mainloop()