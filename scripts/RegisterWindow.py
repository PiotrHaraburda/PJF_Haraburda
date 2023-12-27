from tkinter import *
import customtkinter as ctk
from PIL import Image


class RegisterWindow(ctk.CTk):

    def __init__(self, master, other_window, mainImage, crud, **kwargs):
        super().__init__(**kwargs)
        self.master = master

        self.imageLabel = ctk.CTkLabel(self.master, image=mainImage, text="", bg_color="white")
        self.imageLabel.place(x=380, y=35)

        self.mainLabel = ctk.CTkLabel(self.master, text="MileageMate", text_color="#555555",
                                      font=("Trebuchet", 28, "bold"),
                                      bg_color="white")
        self.mainLabel.place(x=190, y=40)

        self.logIntoLabel = ctk.CTkLabel(self.master, text="Sign up into your account", text_color="#12833b",
                                         font=("Trebuchet", 12, "bold"),
                                         bg_color="white")
        self.logIntoLabel.pack(pady=75)

        self.firstNameLabel = ctk.CTkLabel(self.master, text="First Name:", text_color="#555555",
                                           font=("Trebuchet", 12, "bold"),
                                           bg_color="white")
        self.firstNameLabel.place(x=50, y=125)
        self.firstNameTextBox = ctk.CTkTextbox(self.master, width=225, height=30, corner_radius=5, fg_color="#dbfde7",
                                               bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                               border_spacing=0)
        self.firstNameTextBox.place(x=50, y=155)

        self.loginLabel = ctk.CTkLabel(self.master, text="Login:", text_color="#555555",
                                       font=("Trebuchet", 12, "bold"),
                                       bg_color="white")
        self.loginLabel.place(x=325, y=125)
        self.loginTextBox = ctk.CTkTextbox(self.master, width=225, height=30, corner_radius=5, fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                           border_spacing=0)
        self.loginTextBox.place(x=325, y=155)

        self.emailLabel = ctk.CTkLabel(self.master, text="Email:", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                       bg_color="white")
        self.emailLabel.place(x=50, y=195)
        self.emailTextBox = ctk.CTkTextbox(self.master, width=225, height=30, corner_radius=5, fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                           border_spacing=0)
        self.emailTextBox.place(x=50, y=225)

        self.ageLabel = ctk.CTkLabel(self.master, text="What's your age?", text_color="#555555",
                                     font=("Trebuchet", 12, "bold"),
                                     bg_color="white")
        self.ageLabel.place(x=325, y=195)
        self.ageComboBox = ctk.CTkComboBox(self.master, width=225, height=30, corner_radius=5, fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                           border_width=0, button_color="#878787",
                                           values=["<18", "18 to 25", "26 to 35", "36 to 50", "51 to 60", ">60"],
                                           dropdown_fg_color="#878787", dropdown_font=("Trebuchet", 12, "bold"))
        self.ageComboBox.place(x=325, y=225)

        self.passwordLabel = ctk.CTkLabel(self.master, text="Password:", text_color="#555555",
                                          font=("Trebuchet", 12, "bold"),
                                          bg_color="white")
        self.passwordLabel.place(x=50, y=265)
        self.passwordTextBox = ctk.CTkEntry(self.master, width=225, height=30, corner_radius=5, fg_color="#dbfde7",
                                            bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                            border_width=0, show="*")
        self.passwordTextBox.place(x=50, y=295)

        self.registerButton = ctk.CTkButton(self.master, text="Register", fg_color="#146734",
                                            font=("Trebuchet", 14, "bold"),
                                            width=500, height=40, corner_radius=5, hover_color="#12552d",
                                            bg_color="white", command=lambda: self.register_callback(crud))
        self.registerButton.place(x=50, y=375)

        self.alreadyRegisteredLabel = ctk.CTkLabel(self.master, text="Already registered?", text_color="#555555",
                                                   font=("Trebuchet", 12, "bold"),
                                                   bg_color="white")
        self.alreadyRegisteredLabel.place(x=50, y=430)

        self.loginButton = ctk.CTkButton(self.master, text="Login now", fg_color="white",
                                         font=("Trebuchet", 14, "bold"),
                                         width=500, height=35, corner_radius=5, hover_color="#dbdbd9",
                                         bg_color="white", border_width=1, text_color="#555555",
                                         command=lambda: self.login_callback(other_window))
        self.loginButton.place(x=50, y=455)

    def login_callback(self, other_window):
        self.master.withdraw()
        other_window.deiconify()

    def register_callback(self, crud):
        first_name = self.firstNameTextBox.get("0.0", 'end-1c')
        login = self.loginTextBox.get("0.0", 'end-1c')
        email = self.emailTextBox.get("0.0", 'end-1c')
        age = self.ageComboBox.get()
        password = self.passwordTextBox.get()

        if first_name != "" and login != "" and email != "" and password != "":
            crud.createData(first_name, login, email, age, password)
