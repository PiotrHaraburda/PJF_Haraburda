from datetime import datetime, timedelta
from tkinter import *
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkcalendar import Calendar
from PIL import Image
import matplotlib.pyplot as plt

whichButtonPressed = 1


class MainWindow(ctk.CTk):

    def __init__(self, master, login_window, mainImage2, accountInfoImage, dashboardImage, accountImage, settingsImage,
                 logoutImage, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.login_window = login_window

        self.leftPane = ctk.CTkFrame(self.master, width=270, height=700, fg_color="#00a05e", bg_color="#e3e7e6",
                                     corner_radius=15)
        self.leftPane.pack(side=LEFT)

        self.leftStrip = ctk.CTkFrame(self.leftPane, width=70, height=700, fg_color="#02ac69", bg_color="#00a05e",
                                      corner_radius=15)
        self.leftStrip.place(x=0, y=0)

        self.mainPane = ctk.CTkFrame(self.master, width=930, height=700, fg_color="#e3e7e6", bg_color="#e3e7e6")
        self.mainPane.pack(side=LEFT)

        self.mainLabel = ctk.CTkLabel(self.leftPane, text="MileageMate", text_color="white",
                                      font=("Century Gothic", 22, "bold"),
                                      bg_color="#00a05e")
        self.mainLabel.place(x=100, y=20)

        self.mainImage = ctk.CTkLabel(self.leftStrip, image=mainImage2, text="")
        self.mainImage.place(x=13, y=660)

        self.overviewButton = ctk.CTkButton(self.leftPane, text="   Overview", width=200, anchor="w",
                                            font=("Century Gothic", 12, "bold"), height=50, fg_color="#e3e7e6",
                                            corner_radius=8, text_color="#00a05e", hover_color="#e3e7e6")
        self.overviewButton.place(x=70, y=100)
        self.overviewButton.bind('<Enter>', lambda event, button=self.overviewButton: self.button_enter(button))
        self.overviewButton.bind('<Leave>', lambda event, button=self.overviewButton: self.button_leave(button, 1))

        self.fuelButton = ctk.CTkButton(self.leftPane, text="   Fuel", width=200, anchor="w",
                                        font=("Century Gothic", 12, "bold"), height=50, fg_color="#00a05e",
                                        hover_color="#e3e7e6")
        self.fuelButton.place(x=70, y=150)
        self.fuelButton.bind('<Enter>', lambda event, button=self.fuelButton: self.button_enter(button))
        self.fuelButton.bind('<Leave>', lambda event, button=self.fuelButton: self.button_leave(button, 2))

        self.servicesButton = ctk.CTkButton(self.leftPane, text="   Services", width=200, anchor="w",
                                            font=("Century Gothic", 12, "bold"), height=50, fg_color="#00a05e",
                                            hover_color="#e3e7e6")
        self.servicesButton.place(x=70, y=200)
        self.servicesButton.bind('<Enter>', lambda event, button=self.servicesButton: self.button_enter(button))
        self.servicesButton.bind('<Leave>', lambda event, button=self.servicesButton: self.button_leave(button, 3))

        self.carsButton = ctk.CTkButton(self.leftPane, text="   Cars", width=200, anchor="w",
                                        font=("Century Gothic", 12, "bold"), height=50, fg_color="#00a05e",
                                        hover_color="#e3e7e6")
        self.carsButton.place(x=70, y=250)
        self.carsButton.bind('<Enter>', lambda event, button=self.carsButton: self.button_enter(button))
        self.carsButton.bind('<Leave>', lambda event, button=self.carsButton: self.button_leave(button, 4))

        self.nearbyButton = ctk.CTkButton(self.leftPane, text="   Nearby", width=200, anchor="w",
                                          font=("Century Gothic", 12, "bold"), height=50, fg_color="#00a05e",
                                          hover_color="#e3e7e6")
        self.nearbyButton.place(x=70, y=300)
        self.nearbyButton.bind('<Enter>', lambda event, button=self.nearbyButton: self.button_enter(button))
        self.nearbyButton.bind('<Leave>', lambda event, button=self.nearbyButton: self.button_leave(button, 5))

        self.overviewButton.bind('<Button-1>', self.overview_button_callback)
        self.fuelButton.bind('<Button-1>', self.fuel_button_callback)
        self.servicesButton.bind('<Button-1>', self.services_button_callback)
        self.carsButton.bind('<Button-1>', self.cars_button_callback)
        self.nearbyButton.bind('<Button-1>', self.nearby_button_callback)

        self.accountInfo = ctk.CTkLabel(self.mainPane, text="<Login>", font=("Century Gothic", 15, "bold"), height=20,
                                        fg_color="#e3e7e6", bg_color="#e3e7e6", text_color="#555555")
        self.accountInfo.place(x=834, y=10)
        self.accountInfo.bind("<Map>", self.accountInfoUpdate)

        self.accInfoImage = ctk.CTkLabel(self.mainPane, image=accountInfoImage, text="")
        self.accInfoImage.place(x=810, y=5)

        self.firstPane = ctk.CTkFrame(self.mainPane, width=300, height=230, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")
        self.firstPane.place(x=20, y=60)

        self.secondPane = ctk.CTkFrame(self.mainPane, width=300, height=105, corner_radius=5, fg_color="white",
                                       bg_color="#e3e7e6")
        self.secondPane.place(x=342, y=60)

        self.thirdPane = ctk.CTkFrame(self.mainPane, width=300, height=105, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")
        self.thirdPane.place(x=342, y=185)

        self.fourthPane = ctk.CTkFrame(self.mainPane, width=622, height=375, corner_radius=5, fg_color="white",
                                       bg_color="#e3e7e6")
        self.fourthPane.place(x=20, y=309)

        self.fifthPane = ctk.CTkFrame(self.mainPane, width=250, height=230, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")
        self.fifthPane.place(x=660, y=60)

        self.sixthPane = ctk.CTkFrame(self.mainPane, width=250, height=375, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")
        self.sixthPane.place(x=660, y=309)

        self.makePlot()

        self.dashImage = ctk.CTkLabel(self.leftStrip, image=dashboardImage, text="")
        self.dashImage.place(x=16, y=150)

        self.accImage = ctk.CTkLabel(self.leftStrip, image=accountImage, text="")
        self.accImage.place(x=16, y=250)

        self.settImage = ctk.CTkLabel(self.leftStrip, image=settingsImage, text="")
        self.settImage.place(x=16, y=350)

        self.logImage = ctk.CTkLabel(self.leftStrip, image=logoutImage, text="")
        self.logImage.place(x=19, y=450)

        # cal = Calendar(self.firstPane, selectmode='day',
        #                year=2020, month=5,
        #                day=22,background="red")
        #
        # cal.pack(pady=20)

    def makePlot(self):
        current_date = datetime.now()

        # Lista nazw miesięcy
        month_names = []

        # Tworzenie listy nazw 7 ostatnich miesięcy
        for i in range(7):
            month_names.append(current_date.strftime('%B'))
            current_date -= timedelta(days=30)  # zakładamy, że miesiące mają średnio 30 dni

        month_names.reverse()

        data1 = {'Month': month_names,
                 '$ spent': [0, 0, 0, 0, 0, 0, 300.4]
                 }
        df1 = pd.DataFrame(data1)

        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        figure1.subplots_adjust(bottom=0.4)
        ax1 = figure1.add_subplot(111)
        ax1.tick_params(axis='x', labelsize=8)
        bar1 = FigureCanvasTkAgg(figure1, self.fourthPane)
        bar1.get_tk_widget().place(x=0, y=0)
        df1.plot(kind='bar', legend=True, ax=ax1, color="#085f3d")
        ax1.set_xticklabels(month_names, rotation=0)
        ax1.set_title('Money spent in recent months')


    def accountInfoUpdate(self, event):
        accountLogin = self.login_window.accountLogin
        self.accountInfo.configure(text=accountLogin)

    def button_enter(self, button):
        button.configure(fg_color="#e3e7e6", text_color="#00a05e")

    def button_leave(self, button, buttonNumber):
        global whichButtonPressed
        if buttonNumber != whichButtonPressed:
            button.configure(text_color="#e3e7e6", fg_color="#00a05e")

    def overview_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 1
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.firstPane.place(x=20, y=60)
        self.secondPane.place(x=342, y=60)
        self.thirdPane.place(x=342, y=185)
        self.fourthPane.place(x=20, y=309)
        self.fifthPane.place(x=660, y=60)
        self.sixthPane.place(x=660, y=309)

    def fuel_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 2
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.firstPane.place_forget()
        self.secondPane.place_forget()
        self.thirdPane.place_forget()
        self.fourthPane.place_forget()
        self.fifthPane.place_forget()
        self.sixthPane.place_forget()

    def services_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 3
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.firstPane.place_forget()
        self.secondPane.place_forget()
        self.thirdPane.place_forget()
        self.fourthPane.place_forget()
        self.fifthPane.place_forget()
        self.sixthPane.place_forget()

    def cars_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 4
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.firstPane.place_forget()
        self.secondPane.place_forget()
        self.thirdPane.place_forget()
        self.fourthPane.place_forget()
        self.fifthPane.place_forget()
        self.sixthPane.place_forget()

    def nearby_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 5
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.firstPane.place_forget()
        self.secondPane.place_forget()
        self.thirdPane.place_forget()
        self.fourthPane.place_forget()
        self.fifthPane.place_forget()
        self.sixthPane.place_forget()
