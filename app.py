from PIL import Image
import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk
from registration import registration_page

# Configuring stuff
app = ctk.CTk()
app.after(0, lambda:app.state('zoomed'))
app.title("ExamWiz")
app.wm_iconbitmap('icon.ico')

# Background
bg_image = ctk.CTkImage(Image.open("bg.jpg"),size=(app.winfo_screenwidth(), app.winfo_screenheight()))
bg_image_label = ctk.CTkLabel(app, image=bg_image)
bg_image_label.grid(row=0, column=0)

# creating button class to handle all buttons
class button():
    b = dict()
    @classmethod
    def make(cls,*args):
        t = args[0]
        cls.b[t] = ctk.CTkButton(app,text=t,font=(("Garamond",15,"bold")),fg_color="#225ff0",text_color="white",corner_radius=5)
        cls.b[t].bind('<Enter>',lambda event: change_enter(event,cls.b[t]))
        cls.b[t].bind('<Leave>',lambda event: change_leave(event,cls.b[t]))
        # return cls.b[t]

def change_enter(event,ar):
    ar.configure(text_color = "black",fg_color="#37f0ac")

def change_leave(event,ar):
    ar.configure(text_color = "white",fg_color="#225ff0")

# Ask for Confirmation before exiting
def confirm():
    c = messagebox.askyesno("Exit","Do you want to exit?") 
    if c==1:
        app.quit()

# Windows


button.make("Login")
button.b['Login'].place(relx=0.5, rely=0.45, anchor="center")
button.make("Register")
button.b['Register'].place(relx=0.5, rely=0.55, anchor="center")
button.b['Register'].configure(command = registration_page)
button.make("Exit")
button.b['Exit'].place(relx=0.5,rely=0.75,anchor="center")
button.b['Exit'].configure(command = confirm)

app.mainloop()