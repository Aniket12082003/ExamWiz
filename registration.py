
import customtkinter as ctk
from tktooltip import ToolTip
import string
class registration_page(ctk.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("500x550")
        self.configure(fg_color = "#1c1616")
        self.prepare()
        self.resizable(False,False)
        self.add_to_page()
        self.mainloop()

    # Preparing entire registration page
    def prepare(self):
        # Creating frames to put the label and entry widgets into
        self.frame1 = ctk.CTkFrame(self,fg_color="#1c1616",height=50,bg_color="#1c1616",corner_radius=5)
        self.frame2 = ctk.CTkFrame(self,fg_color="#1c1616",height=50,bg_color="#1c1616",corner_radius=5)
        self.frame3 = ctk.CTkFrame(self,fg_color="#1c1616",height=50,bg_color="#1c1616",corner_radius=5)
        self.frame4 = ctk.CTkFrame(self,fg_color="#1c1616",height=50,bg_color="#1c1616",corner_radius=5)
        self.frame5 = ctk.CTkFrame(self,fg_color="#1c1616",height=50,bg_color="#1c1616",corner_radius=5)
        self.frame6 = ctk.CTkFrame(self,fg_color="#1c1616",height=50,bg_color="#1c1616",corner_radius=5)
        
        # Creating Labels for all fields
        self.name = ctk.CTkLabel(self.frame1,text="Name : ",font=(("Trebuchet",15,"bold","roman")),text_color="white")
        self.roll = ctk.CTkLabel(self.frame2,text="Institution ID : ",font=(("Trebuchet",15,"bold","roman")),text_color="white")
        self.mail = ctk.CTkLabel(self.frame3,text="E-Mail : ",font=(("Trebuchet",15,"bold","roman")),text_color="white")
        self.pswd = ctk.CTkLabel(self.frame4,text="Password : ",font=(("Trebuchet",15,"bold","roman")),text_color="white")
        self.cpswd = ctk.CTkLabel(self.frame5,text="Confirm Password : ",font=(("Trebuchet",15,"bold","roman")),text_color="white")
    
        # Creating entry fields & adding tooltips to each of them
        self.name_entry = ctk.CTkEntry(self.frame1,text_color="black",placeholder_text="Enter your name",placeholder_text_color="#121214",border_color="#111117",fg_color="white",border_width=2,font=(("Trebuchet",15,"roman")),width=200,justify=ctk.CENTER)
        self.tip_name = ToolTip(self.name_entry,msg="Name can contain only alphabets, eg. Abcde",follow=True,delay=0.6)
        self.id_entry = ctk.CTkEntry(self.frame2,text_color="black",placeholder_text="Enter your Institution ID",placeholder_text_color="#121214",border_color="#111117",fg_color="white",border_width=2,font=(("Trebuchet",15,"roman")),width=200,justify=ctk.CENTER)
        self.tip_id = ToolTip(self.id_entry,msg="ID can contain only digits and letters, eg. abc123",follow=True,delay=0.6)
        self.mail_entry = ctk.CTkEntry(self.frame3,text_color="black",placeholder_text="Enter your Email ID",placeholder_text_color="#121214",border_color="#111117",fg_color="white",border_width=2,font=(("Trebuchet",15,"roman")),width=200,justify=ctk.CENTER)
        self.tip_mail = ToolTip(self.mail_entry,msg="Email Id must be in a valid format, eg. abc@xyz.com",follow=True,delay=0.6)
        self.pswd_entry = ctk.CTkEntry(self.frame4,text_color="black",placeholder_text="Enter your password",placeholder_text_color="#121214",border_color="#111117",fg_color="white",border_width=2,font=(("Trebuchet",15,"roman")),show="*",width=200,justify=ctk.CENTER)
        self.tip_pswd = ToolTip(self.pswd_entry,msg="Password must contain atleast one letter, digit and special character",follow=True,delay=1)
        self.cpswd_entry = ctk.CTkEntry(self.frame5,text_color="black",placeholder_text="Re-enter your password",placeholder_text_color="#121214",border_color="#111117",fg_color="white",border_width=2,font=(("Trebuchet",15,"roman")),show="*",width=200,justify=ctk.CENTER)
        self.tip_cpswd = ToolTip(self.cpswd_entry,msg="Password must be the same as above",follow=True,delay=0.6)

        # Adding event handlers to each entry widget
        self.name_entry.bind(sequence="<FocusOut>",command = lambda event : self.param(event,"name"))
        self.id_entry.bind(sequence="<FocusOut>",command = lambda event : self.param(event,"id"))
        self.pswd_entry.bind(sequence="<FocusOut>",command = lambda event : self.param(event,"pswd"))
        self.cpswd_entry.bind(sequence="<FocusOut>",command = lambda event : self.param(event,"cpswd"))

        # Creating Register button
        self.regis = ctk.CTkButton(self.frame6,text="Register",text_color="white",hover_color="#2bcf02",hover=True,fg_color="#0a0263",border_spacing=2,font=(("Trebuchet",15,"roman")),state=ctk.DISABLED)
        self.regis.bind(sequence="<Enter>",command = lambda event : self.param(event,"register"))

    # Event Handler function
    def param(self,event,*args):
        b = True
        if args[0]=="name":
            if self.name_entry.get().strip()!='':
                for i in self.name_entry.get().strip():
                    if i not in string.ascii_letters and i!=" ":
                        b = False
                        break
                if b==False:   
                    self.name_entry.configure(border_color = "#e60202",text_color = "#e60202")
                    self.tip_name.msg = "Name must not contain anything other than letters and white spaces!"
                else:
                    self.name_entry.configure(border_color = "#048f14",text_color="#048f14")
                    self.tip_name.msg = "Valid name"
            else:
                self.tip_name.msg = "Name can contain only alphabets, eg. Abcde"
                self.name_entry['border_color'] = "#111117"
                self.name_entry['text_color'] = "black" 
            b = True
        elif args[0]=="id":
            if self.id_entry.get().strip()!='':
                for i in self.id_entry.get().strip():
                    if i not in string.ascii_letters and i not in string.digits:
                        b = False
                        break
                if b==False:   
                    self.id_entry.configure(border_color = "#e60202",text_color = "#e60202")
                    self.tip_id.msg = "ID must not contain anything other than letters and digits!"
                else:
                    self.id_entry.configure(border_color = "#048f14",text_color="#048f14")
                    self.tip_id.msg = "Valid ID"
            else:
                self.tip_id.msg = "ID can contain only digits and letters, eg. abc123"
                self.id_entry['border_color'] = "#111117"
                self.id_entry['text_color'] = "black"   
            b = True
        elif args[0]=="pswd":
            if self.pswd_entry.get().strip()!='':
                s = set(self.pswd_entry.get().strip())
                sl = set(string.ascii_letters)
                sd = set(string.ascii_letters)
                sp = set(['.','*','#',"!","@","&","^","?","+","-","/","%","_","=","|"])
                if len(s.intersection(sl))==0 or len(s.intersection(sd))==0 or len(s.intersection(sp))==0:
                    b = False
                if b==False:
                    self.pswd_entry.configure(border_color = "#e60202",text_color = "#e60202")
                    self.tip_pswd.msg = "Password not containing atleast one of the required characters!"
                else:
                    self.pswd_entry.configure(border_color = "#048f14",text_color="#048f14")
                    self.tip_pswd.msg = "Valid password"
            else:
                self.tip_pswd.msg = "ID can contain only digits and letters, eg. abc123"
                self.pswd_entry['border_color'] = "#111117"
                self.pswd_entry['text_color'] = "black" 
            b = True
        elif args[0]=="cpswd":
            if self.pswd_entry.get().strip()=='':
                self.cpswd_entry.configure(state=ctk.DISABLED)
                self.tip_cpswd.msg = "Password not yet entered!"
            else:
                if self.cpswd_entry.get().strip()!='':
                    if self.pswd_entry.get().strip()!=self.cpswd_entry.get().strip():
                        b = False
                    if b==False:
                        self.cpswd_entry.configure(border_color = "#e60202",text_color = "#e60202")
                        self.tip_cpswd.msg = "Password not matching with the above!"
                    else:
                        self.cpswd_entry.configure(border_color = "#048f14",text_color="#048f14")
                        self.tip_cpswd.msg = "Password confirmed"
                else:
                    self.tip_cpswd.msg = "Password must be the same as above"
                    self.cpswd_entry['border_color'] = "#111117"
                    self.cpswd_entry['text_color'] = "black" 
                b = True
        elif args[0]=="register":
            if self.tip_name.msg=="Valid name" and self.tip_id.msg=="Valid ID" and self.tip_pswd.msg=="Valid password" and self.tip_cpswd.msg=="Password Confirmed":
                self.regis.configure(state = ctk.NORMAL)
            else:
                self.regis.configure(fg_color = "#f2110a")

    # Positioning widgets on the page
    def add_to_page(self):
        self.frame1.pack(padx = 10, pady = 20,fill = ctk.X)
        self.frame2.pack(padx = 10, pady = 20,fill = ctk.X)
        self.frame3.pack(padx = 10, pady = 20,fill = ctk.X)
        self.frame4.pack(padx = 10, pady = 20,fill = ctk.X)
        self.frame5.pack(padx = 10, pady = 20,fill = ctk.X)
        self.frame6.pack(padx = 10, pady = 20,fill = ctk.X)
        self.name.pack(padx = 10,pady = 10,side = ctk.LEFT)
        self.name_entry.pack(padx = 50,pady = 10,side = ctk.RIGHT)
        self.roll.pack(padx = 10,pady = 10,side = ctk.LEFT)
        self.id_entry.pack(padx = 50,pady = 10,side = ctk.RIGHT)
        self.mail.pack(padx = 10,pady = 10,side = ctk.LEFT)
        self.mail_entry.pack(padx = 50,pady = 10,side = ctk.RIGHT)
        self.pswd.pack(padx = 10,pady = 10,side = ctk.LEFT)
        self.pswd_entry.pack(padx = 50,pady = 10,side = ctk.RIGHT)
        self.cpswd.pack(padx = 10,pady = 10,side = ctk.LEFT)
        self.cpswd_entry.pack(padx = 50,pady = 10,side = ctk.RIGHT)
        self.regis.pack(padx = 10,pady = 10)
r = registration_page()
