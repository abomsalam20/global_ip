from tkinter import *
from tkinter import messagebox
import requests
# Define the URL to request
url = "https://api.ipify.org"

window = Tk()

window.title("Welcome to Glopal IP app")

window.geometry('400x150')


lbl = Label(window, text="")
lbl.grid(column=0, row=0)
response_Url="IP : 0.0.0.0"

def clicked():
    global url
    # Send a GET request to the URL
    response = requests.get(url)  
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        #print(f"Successfully retrieved content from: {response.url}")
       # print("Response content (first 50 characters):")
       global  response_Url  # Print the first 50 characters of the response text
       response_Url=response.text[:50]
     
      
       lbl.configure(text="IP : "+response_Url)
       
       

    else:
       # print(f"Failed to retrieve content. Status code: {response.status_code}")
       print("Error")
def ext_func():

    window = Tk()
    window.title("about us")
    window.geometry('150x150')
    lbl = Label(window, text="Soundworld")
    lbl.grid(column=0, row=0)
    window.mainloop()
    


lbl.configure(text=response_Url)

btn = Button(window, text="Get Global IP ", command=clicked)
ext = Button(window, text="about", command=ext_func)
btn.grid(column=0, row=2)
ext.grid(column=1, row=3)
window.mainloop()