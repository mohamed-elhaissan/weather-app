from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


window = Tk()
window.title("weather")
window.geometry("900x500+300+200")
window.resizable(False,False)
search_image = PhotoImage(file="search.png") 

myimage = Label(image=search_image)
myimage.place(x=20,y=20)

textfiled = Entry(window,justify="center",width=22,font=("poppins",20,"bold"),background="#434040",foreground="#dee2e6",border=0,borderwidth=0)

textfiled.place(x=50,y=35)
textfiled.focus()

search_icon = PhotoImage(file="search_icon.png")
my_icon = Label(image=search_icon,border=0,cursor="hand2",bg="#404040")
my_icon.place(x=400,y=32)
#logo
logo_image = PhotoImage(file="logo.png")
my_logo = Label(image=logo_image)
my_logo.place(x=150,y=100)
#button
button_image = PhotoImage(file="box.png")
my_button = Label(image=button_image)
my_button.pack(padx=5,pady=5,side=BOTTOM)

#label
label1 = Label(window,text="wind",font=("poppins",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)
label2 = Label(window,text="HUMDITY",font=("poppins",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=260,y=400)
label3 = Label(window,text="DESCRIPTION",font=("poppins",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)
label4 = Label(window,text="PRESSURE",font=("poppins",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

temperature = Label(font=("poppins",70,"bold"),fg="#ee666d")
temperature.place(x=400,y=150)













window.mainloop()