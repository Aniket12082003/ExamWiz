import PIL.Image
import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk
# Configuring stuff
app = ctk.CTk()
#app.after(0, lambda:app.state('zoomed'))
app.title("ExamWiz")
app.wm_iconbitmap('icon.ico')
app.geometry("600x500")
app.attributes("-fullscreen",True)

# Background
bg = PIL.Image.open("bg.jpg")
background_image = ctk.CTkImage(bg)
img = ctk.CTkImage(bg, size=(app._max_width, app._max_height))

'''def bg_resizer(e):
    if e.widget is app:
        i = ctk.CTkImage(bg, size=(e.width, e.height))
        bg_lbl.configure(text="", image=i)'''

# creating button class to handle all buttons
class button():
    b = dict()
    @classmethod
    def make(cls,*args):
        t = args[0]
        cls.b[t] = ctk.CTkButton(app,text=t,font=(("Garamond",15,"bold")),fg_color="#225ff0",
                               text_color="white",corner_radius=5)
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


bg_lbl = ctk.CTkLabel(app, text="", image=background_image)
bg_lbl.place(x=0, y=0)

# Windows
def open_registration_window():
    app.iconify()
    print("registration button clicked!")
    registration_window = ctk.CTk()
    registration_window.title("Login")
    registration_window.attributes('-fullscreen',True)
    registration_window._set_appearance_mode("light")
    name_label = ctk.CTkLabel(registration_window, text="Name:",text_color="black",fg_color="white")
    name_entry = ctk.CTkEntry(registration_window,fg_color="#ebf2e9")
    email_label = ctk.CTkLabel(registration_window, text="Email:",fg_color="#ebf2e9")
    email_entry = ctk.CTkEntry(registration_window,show="*",placeholder_text="Enter Valid Email",
                               placeholder_text_color="#3f4240",corner_radius=5,
                               font=(("Cambria",15,"bold")),text_color="black",fg_color="#ebf2e9")
    password_label = ctk.CTkLabel(registration_window, text="Password:",fg_color="#ebf2e9")
    password_entry = ctk.CTkEntry(registration_window, show="*",fg_color="#ebf2e9")
    register_button = ctk.CTkButton(registration_window, text="Register", command=registration_window.destroy)

    name_label.grid(row=0, column=0, padx=10, pady=5)
    name_entry.grid(row=0, column=1, padx=10, pady=5)
    email_label.grid(row=1, column=0, padx=10, pady=5)
    email_entry.grid(row=1, column=1, padx=10, pady=5)
    password_label.grid(row=2, column=0, padx=10, pady=5)
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    register_button.grid(row=3, column=1, padx=10, pady=10)
    registration_window.mainloop()

button.make("Login")
button.b['Login'].place(relx=0.5, rely=0.45, anchor="center")
button.make("Register")
button.b['Register'].place(relx=0.5, rely=0.55, anchor="center")
button.b['Register'].configure(command = open_registration_window)
button.make("Exit")
button.b['Exit'].place(relx=0.5,rely=0.75,anchor="center")
button.b['Exit'].configure(command = confirm)


app.mainloop()