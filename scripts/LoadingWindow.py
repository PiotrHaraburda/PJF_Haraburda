from tkinter import *
import customtkinter as ctk
from PIL import Image

j = 0
i = -50
k = 0


class LoadingWindow(ctk.CTk):
    def __init__(self, master,login_app, main_app_window, mainImage,crud, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.main_app_window = main_app_window
        self.login_app = login_app

        self.welcomeLabel = ctk.CTkLabel(self.master, text="Hello, ", text_color="#12833b",
                                         font=("Trebuchet", 28, "bold"),
                                         bg_color="white",width=850,justify=CENTER)
        self.welcomeLabel.place(x=0, y=-100)
        self.slidingCarLabel = ctk.CTkLabel(self.master, image=mainImage, text="", bg_color="white")

        self.welcomeLabel.bind("<Map>", lambda event,crud=crud: self.windowInit(crud))

    def windowInit(self,crud):
        global i, j, k

        self.master.geometry("400x540")
        w = 400
        h = 540
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('+%d+%d' % (x, y))
        self.master.update()

        accountLogin = self.login_app.accountLogin
        self.welcomeLabel.configure(
            text="Hello, " + crud.readUser(accountLogin, "first_name") + "!")

        j = 0
        i = -50
        k = 0
        self.master.overrideredirect(True)
        self.master.after(1, self.resizeWindow)

    def resizeWindow(self):
        global j
        j += 1
        if j < 800:
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
                self.welcomeLabel.place(x=0, y=i)
                self.welcomeLabel.update()
            if i < 900:
                self.slidingCarLabel.place(x=i - 0.3, y=400)
                self.slidingCarLabel.update()
            self.master.after(1, self.welcomeSlide)
        else:
            self.master.update()
            self.welcomeLabel.place(x=0, y=-100)
            self.slidingCarLabel.place_forget()
            self.master.withdraw()
            self.main_app_window.deiconify()
