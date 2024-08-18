import PIL.Image
import customtkinter as ctk

# Configuring stuff
app = ctk.CTk()
#app.after(0, lambda:app.state('zoomed'))
app.title("ExamWiz")
app.wm_iconbitmap('icon.ico')
app.geometry("600x500")

# Background
bg = PIL.Image.open("bg.jpg")
background_image = ctk.CTkImage(bg)

def bg_resizer(e):
    if e.widget is app:
        i = ctk.CTkImage(bg, size=(e.width, e.height))
        bg_lbl.configure(text="", image=i)

bg_lbl = ctk.CTkLabel(app, text="", image=background_image)
bg_lbl.place(x=0, y=0)

# Windows
def open_registration_window():
    registration_window = ctk.CTkToplevel()
    registration_window.title("Login")
    registration_window.geometry("600x500")
    registration_window.attributes('-topmost',True)

    name_label = ctk.CTkLabel(registration_window, text="Name:")
    name_entry = ctk.CTkEntry(registration_window)
    email_label = ctk.CTkLabel(registration_window, text="Email:")
    email_entry = ctk.CTkEntry(registration_window)
    password_label = ctk.CTkLabel(registration_window, text="Password:")
    password_entry = ctk.CTkEntry(registration_window, show="*")
    register_button = ctk.CTkButton(registration_window, text="Register", command=registration_window.destroy)

    name_label.grid(row=0, column=0, padx=10, pady=5)
    name_entry.grid(row=0, column=1, padx=10, pady=5)
    email_label.grid(row=1, column=0, padx=10, pady=5)
    email_entry.grid(row=1, column=1, padx=10, pady=5)
    password_label.grid(row=2, column=0, padx=10, pady=5)
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    register_button.grid(row=3, column=1, padx=10, pady=10)


button = ctk.CTkButton(app, text="Login", command=open_registration_window)
button.place(relx=0.5, rely=0.45, anchor="center")
button = ctk.CTkButton(app, text="Register")
button.place(relx=0.5, rely=0.55, anchor="center")

app.bind("<Configure>", bg_resizer)
app.mainloop()