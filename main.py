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


#function
#fonction dyal weahter
def getweather():
    #had code kay3ti l contunent
    ville = textfiled.get()
    geo = Nominatim(user_agent="nothinghere")
    localisation = geo.geocode(ville)
    obj = TimezoneFinder()
    resultas = obj.timezone_at(lng=localisation.longitude,lat=localisation.latitude)
    
    #speacifique place and zone
    home = pytz.timezone(resultas)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I %M %p")
    
    clocK.config(text=current_time)
    name.config(text="current Weather")
    exclude = "minutely,hourly,alerts"
    #weather finder
    api = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid=f0f15790d2c1e44d14900b2c42d171bc"
    data = requests.get(api).json()
    condition = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temp = int(data['main']['temp']-273.15)
    pressure = data['main']['pressure']
    humidity  = data['main']['humidity']
   
   
    
    
    temperature.config(text=(temp,"°"))
    c.config(text=(condition))
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)
    
    
#search box
search_image = PhotoImage(file="search.png")
myimage = Label(image=search_image)
myimage.place(x=20,y=20)

textfiled = Entry(window,justify="center",width=22,font=("poppins",20,"bold"),background="#434040",foreground="#dee2e6",border=0,borderwidth=0)

textfiled.place(x=50,y=35)
textfiled.focus()

search_icon = PhotoImage(file="search_icon.png")
my_icon = Button(image=search_icon,border=0,cursor="hand2",bg="#404040",command=getweather)
my_icon.place(x=400,y=32)
#logo
logo_image = PhotoImage(file="logo.png")
my_logo = Label(image=logo_image)
my_logo.place(x=150,y=100)
#button
button_image = PhotoImage(file="box.png")
my_button = Label(image=button_image)
my_button.pack(padx=5,pady=5,side=BOTTOM)


#time 
name = Label(window,font=("poppins",15))
name.place(x=30, y=100)
clocK = Label(window,font=("poppins",20))
clocK.place(x= 30 ,y=130)


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
temperature.place(x=400,y=130)
c = Label(font=("poppins",20,"bold"))
c.place(x=400,y=250)
w =Label(text="....",font=("poppins",15,"bold"),background="#1ab5ef")
w.place(x=120,y=426)
h =Label(text="....",font=("poppins",15,"bold"),background="#1ab5ef")
h.place(x=280,y=426)
d =Label(text="....",font=("poppins",15,"bold"),background="#1ab5ef")
d.place(x=450,y=426)
p =Label(text="....",font=("poppins",15,"bold"),background="#1ab5ef")
p.place(x=670,y=426)







window.mainloop()