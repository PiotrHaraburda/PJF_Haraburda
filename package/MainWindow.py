from tkinter import *
import customtkinter as ctk
from PIL import Image


class MainWindow(ctk.CTk):

    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master

        self.leftPane = ctk.CTkFrame(self.master,width=300,height=700,fg_color="#f0fdf4",bg_color="white")
        self.leftPane.pack(side=LEFT)

        self.topPane = ctk.CTkFrame(self.master, width=900, height=100, fg_color="white",bg_color="white")
        self.topPane.pack(side=TOP)

        self.mainPane = ctk.CTkFrame(self.master, width=900, height=600, fg_color="white",bg_color="white")
        self.mainPane.pack(side=TOP)

        self.overviewButton=ctk.CTkButton(self.topPane, text="Overview",width=100, fg_color="#dbfde7",
                                            font=("Trebuchet", 12),
                                             corner_radius=5, hover_color="#146732",
                                            bg_color="white", border_width=1, text_color="#12833b",border_color="#12833b")
        self.overviewButton.grid(column=0,row=0,pady=20,padx=20)

        self.fuelButton = ctk.CTkButton(self.topPane, text="Fuel",width=100, fg_color="white",
                                            font=("Trebuchet", 12),
                                             corner_radius=5, hover_color="#dbfde7",
                                            bg_color="white", border_width=1, text_color="#12833b",border_color="#12833b")
        self.fuelButton.grid(column=1, row=0,pady=20,padx=20)

        self.servicesButton = ctk.CTkButton(self.topPane, text="Services",width=100, fg_color="white",
                                            font=("Trebuchet", 12),
                                             corner_radius=5, hover_color="#dbfde7",
                                            bg_color="white", border_width=1, text_color="#12833b",border_color="#12833b")
        self.servicesButton.grid(column=2, row=0,pady=20,padx=20)

        self.carsButton = ctk.CTkButton(self.topPane, text="Cars",width=100, fg_color="white",
                                            font=("Trebuchet", 12),
                                             corner_radius=5, hover_color="#dbfde7",
                                            bg_color="white", border_width=1, text_color="#12833b",border_color="#12833b")
        self.carsButton.grid(column=3, row=0, pady=20, padx=20)

        self.nearbyButton = ctk.CTkButton(self.topPane, text="Nearby",width=100, fg_color="white",
                                            font=("Trebuchet", 12),
                                             corner_radius=5, hover_color="#dbfde7",
                                            bg_color="white", border_width=1, text_color="#12833b",border_color="#12833b")
        self.nearbyButton.grid(column=4, row=0, pady=20, padx=20)
