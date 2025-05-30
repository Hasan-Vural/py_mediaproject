from entities.User import User
from services.UserService import UserService
from tkinter import *
from tkinter import font
from tkinter import PhotoImage
from register import Register

class UserProfile(Frame):

    def __init__(self, root,controller) -> None:
        Frame.__init__(self,root)
        self.root=self
        self.controller=controller
        self.user_profile_frame=Frame(self.root,bg="#070F2B")
        self.user_profile_frame.pack(fill=BOTH,expand=True)

        self.user_profile_child_frame=Frame(self.user_profile_frame,bg="#1B1A55")
        self.user_profile_child_frame.pack(expand=True)

        self.user_profile_child2_frame=Frame(self.user_profile_child_frame,bg='#1B1A55')
        self.user_profile_child2_frame.pack(padx=100,pady=55,expand=True)

        self.logo_user_profile_frame=Frame(self.user_profile_child2_frame, bg="#535C91")
        self.logo_user_profile_frame.grid(row=0,column=0,padx=150,pady=15) 
        
        self.logo_user_profile=PhotoImage(file="medias\logos\profilePng.png")
        self.logo_user_profile_label=Label(self.logo_user_profile_frame,image=self.logo_user_profile)
        self.logo_user_profile_label.img_reference=self.logo_user_profile
        self.logo_user_profile_label.pack(fill=BOTH)

        self.username_frame=Frame(self.user_profile_child2_frame,bg="#1B1A55")
        self.username_frame.grid(row=1,pady=30)

        self.label_username=Label(self.username_frame,text="Username",font=("Roboto",20),bg="#1B1A55",fg="#D8C4B6")
        self.label_username.grid(row=0,column=0)

        self.label_username_get=Label(self.username_frame,text="Username Example",font=("Roboto",24),bg="#1B1A55",fg="#D8C4B6")
        self.label_username_get.grid(row=1,column=0)


        self.first_name_frame=Frame(self.user_profile_child2_frame,bg="#1B1A55")
        self.first_name_frame.grid(row=2,pady=30)

        self.label_first_name=Label(self.first_name_frame,text="First Name",font=("Roboto",20),bg="#1B1A55",fg="#D8C4B6")
        self.label_first_name.grid(row=0,column=0)

        self.label_first_name_get=Label(self.first_name_frame,text="First Name Example",font=("Roboto",24),bg="#1B1A55",fg="#D8C4B6")
        self.label_first_name_get.grid(row=1,column=0)


        self.last_name_frame=Frame(self.user_profile_child2_frame,bg="#1B1A55")
        self.last_name_frame.grid(row=3,pady=30)

        self.label_last_name=Label(self.last_name_frame,text="Last Name",font=("Roboto",20),bg="#1B1A55",fg="#D8C4B6")
        self.label_last_name.grid(row=0,column=0)

        self.label_last_name_get=Label(self.last_name_frame,text="Last Name Example",font=("Roboto",24),bg="#1B1A55",fg="#D8C4B6")
        self.label_last_name_get.grid(row=1,column=0)