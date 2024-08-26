import customtkinter as ctk
import pywinstyles
from tkinter import messagebox
class login(ctk.CTk):
    count = 0

    @classmethod
    def counter(cls):
        cls.count+=1

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        login.counter()
        self.geometry("500x500")
        self.title("Login Page")
        self.resizable(False,False)
        self._fg_color = "#1c1616"
        self.attributes("-alpha",0.85)
        pywinstyles.apply_style(self,style="aero")
        self.create()
        self.add_to_page()
        self.mainloop()

    # Creating label and entry widgets for fields
    def create(self):

        self.log_stat = False

        #Creating frames to contain the labels and widgets
        self.frame1 = ctk.CTkFrame(self,height=50,corner_radius=5,fg_color=None)
        self.frame2 = ctk.CTkFrame(self,height=50,corner_radius=5,fg_color=None)
        self.frame3 = ctk.CTkFrame(self,height=50,corner_radius=5,fg_color=None)
        self.frame4 = ctk.CTkFrame(self,height=50,corner_radius=5,fg_color=None,width=30)

        # Creating labels for entry widgets 
        self.id = ctk.CTkLabel(self.frame1,text="Institution ID: ",text_color="white",font=(("Trebuchet",15,"bold","roman")))
        self.mail = ctk.CTkLabel(self.frame2,text="E-mail : ",text_color="white",font=(("Trebuchet",15,"bold","roman")))
        self.pswd = ctk.CTkLabel(self.frame3,text="Password : ",text_color="white",font=(("Trebuchet",15,"bold","roman")))
        self.log = ctk.CTkButton(self.frame4,text="Login",text_color="white",border_width=2,corner_radius=4,font=(("Trebuchet",15,"bold","roman")),hover=True)
        pywinstyles.set_opacity(self.log,color="#240273",value=1)
        

        # Creating entry widgets for respective fields
        self.id_entry = ctk.CTkEntry(self.frame1,text_color="black",placeholder_text="Enter your name",placeholder_text_color="#121214",border_color="#111117",fg_color="white",border_width=2,font=(("Trebuchet",15,"roman")),width=200,justify=ctk.CENTER)
        self.mail_entry = ctk.CTkEntry(self.frame2,text_color="black",placeholder_text="Enter your Institution ID",placeholder_text_color="#121214",border_color="#111117",fg_color="white",border_width=2,font=(("Trebuchet",15,"roman")),width=200,justify=ctk.CENTER)
        self.pswd_entry = ctk.CTkEntry(self.frame3,text_color="black",placeholder_text="Enter your password",placeholder_text_color="#121214",border_color="#111117",fg_color="white",border_width=2,font=(("Trebuchet",15,"roman")),show="*",width=200,justify=ctk.CENTER)
        

        # Adding event to entry widgets and login button
        self.log.bind(sequence="<Enter>",command=lambda event : self.login_cred(event,"Enter"))
        self.log.bind(sequence="<Leave>",command=lambda event : self.login_cred(event,"Leave"))
        self.log.bind(sequence="<Button-1>",command=lambda event : self.login_cred(event,"Button Click"))

    def add_to_page(self):
        # Adding the frames to the page
        self.frame1.pack(padx = 10, pady = 5,fill = ctk.X)
        self.frame2.pack(padx = 10, pady = 5,fill = ctk.X)
        self.frame3.pack(padx = 10, pady = 5,fill = ctk.X)
        self.frame4.pack(padx = 10, pady = 80)
        
        # Adding the widgets to the frames
        self.id.pack(padx = 20,pady = 10,side = ctk.LEFT)
        self.id_entry.pack(padx = 50,pady = 10,side = ctk.RIGHT)
        self.mail.pack(padx = 20,pady = 10,side = ctk.LEFT)
        self.mail_entry.pack(padx = 50,pady = 10,side = ctk.RIGHT)
        self.pswd.pack(padx = 20,pady = 10,side = ctk.LEFT)
        self.pswd_entry.pack(padx = 50,pady = 10,side = ctk.RIGHT)
        self.log.pack(padx = 50,pady = 10)

    def login_cred(self,event,*args):
        if args[0]=='Enter':
            print("Login button entered")
            if self.id_entry.get().strip()!='' and self.mail_entry.get().strip()!='' and self.pswd_entry.get().strip()!='':
                self.log_stat = True
                self.log._hover_color = None
                self.log._hover_color = "green"
                pywinstyles.set_opacity(self.log,color="#240273",value=1)
            else:
                self.log._hover_color = None
                self.log._hover_color = "#f50d05"
                pywinstyles.set_opacity(self.log,color="#240273",value=1)
        elif args[0]=='Leave':
            print("Login button left")
            pywinstyles.set_opacity(self.log,color="#240273",value=1)
        elif args[0]=='Button Click':
            print("Login button clicked")
            if self.log_stat==True:
                self.log_stat = False
                login.counter()
                try:
                    if login.count<=3:
                        self.id_entry.delete(0,len(self.id_entry.get().strip()))
                        self.mail_entry.delete(0,len(self.mail_entry.get().strip()))
                        self.pswd_entry.delete(0,len(self.pswd_entry.get().strip()))
                        print("Login allowed")
                    else:
                        raise Exception("Maximum number of login times exceeded! ")
                except Exception as e:
                    print(e)
                    c = messagebox.showerror("Login Error","You've the maximum attempts to login! Please retry sometime later.")
                    if c:
                        self.quit()
            


l = login()
