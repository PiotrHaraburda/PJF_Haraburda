import customtkinter as ctk

j = 0
i = -50
k = 0


class LoginWindow(ctk.CTk):

    def __init__(self, master, other_window, main_app_window, mainImage, crud, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.main_app_window=main_app_window

        self.accountLogin=""

        self.imageLabel = ctk.CTkLabel(self.master, image=mainImage, text="", bg_color="white")
        self.imageLabel.place(x=280, y=35)

        self.mainLabel = ctk.CTkLabel(self.master, text="MileageMate", text_color="#555555",
                                      font=("Trebuchet", 28, "bold"),
                                      bg_color="white")
        self.mainLabel.place(x=90, y=40)

        self.logIntoLabel = ctk.CTkLabel(self.master, text="Login into your account", text_color="#12833b",
                                         font=("Trebuchet", 12, "bold"),
                                         bg_color="white")
        self.logIntoLabel.pack(pady=75)

        self.loginLabel = ctk.CTkLabel(self.master, text="Login:", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                       bg_color="white")
        self.loginLabel.place(x=50, y=145)

        self.loginTextBox = ctk.CTkTextbox(self.master, width=310, height=30, corner_radius=5, fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                           border_spacing=0)
        self.loginTextBox.pack(pady=0)

        self.invalidLoginLabel = ctk.CTkLabel(self.master, text="User not registered!", text_color="red",
                                              font=("Trebuchet", 12, "bold"),
                                              bg_color="white")

        self.passwordLabel = ctk.CTkLabel(self.master, text="Password:", text_color="#555555",
                                          font=("Trebuchet", 12, "bold"),
                                          bg_color="white")
        self.passwordLabel.place(x=50, y=235)

        self.passwordTextBox = ctk.CTkEntry(self.master, width=310, height=30, corner_radius=5, fg_color="#dbfde7",
                                            bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                            border_width=0, show="*")
        self.passwordTextBox.pack(pady=60)

        self.invalidPasswordLabel = ctk.CTkLabel(self.master, text="Invalid password!", text_color="red",
                                                 font=("Trebuchet", 12, "bold"),
                                                 bg_color="white")

        self.loginButton = ctk.CTkButton(self.master, text="Login", fg_color="#146734", font=("Trebuchet", 14, "bold"),
                                         width=310, height=40, corner_radius=5, hover_color="#12552d", bg_color="white",
                                         command=lambda: self.login_callback(crud, "password"))
        self.loginButton.pack()

        self.registerButton = ctk.CTkButton(self.master, text="Register now", fg_color="white",
                                            font=("Trebuchet", 14, "bold"),
                                            width=310, height=35, corner_radius=5, hover_color="#dbdbd9",
                                            bg_color="white", border_width=1, text_color="#555555",
                                            command=lambda: self.register_callback(other_window))
        self.registerButton.pack(pady=50)

        self.notRegisteredLabel = ctk.CTkLabel(self.master, text="Not registered?", text_color="#555555",
                                               font=("Trebuchet", 12, "bold"),
                                               bg_color="white")
        self.notRegisteredLabel.place(x=50, y=420)

        self.welcomeLabel = ctk.CTkLabel(self.master, text="Hello, ", text_color="#12833b",
                                         font=("Trebuchet", 28, "bold"),
                                         bg_color="white")
        self.slidingCarLabel = ctk.CTkLabel(self.master, image=mainImage, text="", bg_color="white")

    def register_callback(self, other_window):
        self.master.withdraw()
        other_window.deiconify()

    def login_callback(self, crud, desired_item):
        self.master.withdraw()
        self.main_app_window.deiconify()

        # self.invalidLoginLabel.place_forget()
        # self.invalidPasswordLabel.place_forget()
        #
        # if crud.readData(self.loginTextBox.get("0.0", 'end-1c'), desired_item) == "":
        #     self.invalidLoginLabel.place(x=240, y=210)
        #     return
        #
        # if crud.readData(self.loginTextBox.get("0.0", 'end-1c'), desired_item) == self.passwordTextBox.get():
        #     self.accountLogin=self.loginTextBox.get("0.0", 'end-1c')
        #     self.welcomeLabel.configure(
        #         text="Hello, " + crud.readData(self.loginTextBox.get("0.0", 'end-1c'), "first_name") + "!")
        #     self.mainLabel.destroy()
        #     self.logIntoLabel.destroy()
        #     self.loginLabel.destroy()
        #     self.loginTextBox.destroy()
        #     self.invalidLoginLabel.destroy()
        #     self.passwordLabel.destroy()
        #     self.passwordTextBox.destroy()
        #     self.invalidPasswordLabel.destroy()
        #     self.loginButton.destroy()
        #     self.notRegisteredLabel.destroy()
        #     self.registerButton.destroy()
        #     self.imageLabel.destroy()
        #     self.master.overrideredirect(True)
        #     self.master.after(1, self.resizeWindow)
        # else:
        #     self.invalidPasswordLabel.place(x=254, y=298)

    def resizeWindow(self):
        global j
        j += 1
        if j < 400:
            w = int(self.master.winfo_width() + 1)
            h = 540
            ws = self.master.winfo_screenwidth()
            hs = self.master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            self.master.geometry('+%d+%d' % (x, y))
            self.master.geometry(str(w) + "x540")
            self.master.update()
            self.master.after(1, self.resizeWindow)
        else:
            self.master.update()
            self.welcomeLabel.place(x=0, y=0)
            self.master.after(1, self.welcomeSlide)

    def welcomeSlide(self):
        global i
        i += 1
        if i < 1600:
            if i < 240:
                self.welcomeLabel.place(x=335, y=i)
                self.welcomeLabel.update()
            if i < 900:
                self.slidingCarLabel.place(x=i-0.8, y=400)
                self.slidingCarLabel.update()
            self.master.after(1, self.welcomeSlide)
        else:
            self.master.update()
            self.master.withdraw()
            self.main_app_window.deiconify()
