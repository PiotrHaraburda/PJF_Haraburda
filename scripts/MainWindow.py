from datetime import datetime, timedelta
from tkinter import *
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkcalendar import Calendar
import matplotlib.pyplot as plt

whichButtonPressed = 1


class MainWindow(ctk.CTk):

    def __init__(self, master, login_window, main_image2, account_info_image, dashboard_image, account_image,
                 settings_image,
                 logout_image, fuel_image, service_image, car_image, plus_image, back_image, crud, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.login_window = login_window
        self.fuelRecordPanes = []
        self.fuelYearLabels = []
        self.fuelMonthLabels = []
        self.fuelDayLabels = []
        self.fuelMoneyLabels = []
        self.fuelLitersLabels = []
        self.fuelFueltypeLabels = []
        self.fuelStationLabels = []

        self.leftPane = ctk.CTkFrame(self.master, width=270, height=700, fg_color="#00a05e", bg_color="#e3e7e6",
                                     corner_radius=15)
        self.leftPane.place(x=0, y=0)

        self.leftStrip = ctk.CTkFrame(self.master, width=70, height=700, fg_color="#02ac69", bg_color="#00a05e",
                                      corner_radius=15)
        self.leftStrip.place(x=0, y=0)

        self.mainPane = ctk.CTkFrame(self.master, width=1130, height=700, fg_color="#e3e7e6", bg_color="#e3e7e6")
        self.mainPane.place(x=270, y=0)

        self.mainLabel = ctk.CTkLabel(self.leftPane, text="MileageMate", text_color="white",
                                      font=("Century Gothic", 22, "bold"),
                                      bg_color="#00a05e")
        self.mainLabel.place(x=100, y=20)

        self.mainImage = ctk.CTkLabel(self.leftStrip, image=main_image2, text="")
        self.mainImage.place(x=13, y=660)

        self.overviewButton = ctk.CTkButton(self.leftPane, text="   Overview", width=200, anchor="w",
                                            font=("Century Gothic", 12, "bold"), height=50, fg_color="#e3e7e6",
                                            corner_radius=8, text_color="#00a05e", hover_color="#e3e7e6",
                                            cursor="hand2")
        self.overviewButton.place(x=70, y=100)
        self.overviewButton.bind('<Enter>', lambda event, button=self.overviewButton: self.button_enter(button))
        self.overviewButton.bind('<Leave>', lambda event, button=self.overviewButton: self.button_leave(button, 1))

        self.fuelButton = ctk.CTkButton(self.leftPane, text="   Fuel", width=200, anchor="w",
                                        font=("Century Gothic", 12, "bold"), height=50, fg_color="#00a05e",
                                        hover_color="#e3e7e6", cursor="hand2")
        self.fuelButton.place(x=70, y=150)
        self.fuelButton.bind('<Enter>', lambda event, button=self.fuelButton: self.button_enter(button))
        self.fuelButton.bind('<Leave>', lambda event, button=self.fuelButton: self.button_leave(button, 2))

        self.servicesButton = ctk.CTkButton(self.leftPane, text="   Services", width=200, anchor="w",
                                            font=("Century Gothic", 12, "bold"), height=50, fg_color="#00a05e",
                                            hover_color="#e3e7e6", cursor="hand2")
        self.servicesButton.place(x=70, y=200)
        self.servicesButton.bind('<Enter>', lambda event, button=self.servicesButton: self.button_enter(button))
        self.servicesButton.bind('<Leave>', lambda event, button=self.servicesButton: self.button_leave(button, 3))

        self.carsButton = ctk.CTkButton(self.leftPane, text="   Cars", width=200, anchor="w",
                                        font=("Century Gothic", 12, "bold"), height=50, fg_color="#00a05e",
                                        hover_color="#e3e7e6", cursor="hand2")
        self.carsButton.place(x=70, y=250)
        self.carsButton.bind('<Enter>', lambda event, button=self.carsButton: self.button_enter(button))
        self.carsButton.bind('<Leave>', lambda event, button=self.carsButton: self.button_leave(button, 4))

        self.nearbyButton = ctk.CTkButton(self.leftPane, text="   Nearby", width=200, anchor="w",
                                          font=("Century Gothic", 12, "bold"), height=50, fg_color="#00a05e",
                                          hover_color="#e3e7e6", cursor="hand2")
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

        self.accInfoImage = ctk.CTkLabel(self.mainPane, image=account_info_image, text="")
        self.accInfoImage.place(x=810, y=5)

        self.firstPane = ctk.CTkFrame(self.mainPane, width=300, height=230, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")
        self.firstPane.place(x=20, y=60)

        self.carNameLabel = ctk.CTkLabel(self.firstPane, text="Lexus IS200",
                                         font=("Century Gothic", 25, "bold"), height=20,
                                         fg_color="white", text_color="#555555", width=260, justify=CENTER)
        self.carNameLabel.place(x=20, y=20)

        self.yourCarLabel = ctk.CTkLabel(self.firstPane, text="Your personal vehicle",
                                         font=("Century Gothic", 15, "bold"), height=20,
                                         fg_color="white", text_color="#00a05e", width=260, justify=CENTER)
        self.yourCarLabel.place(x=20, y=50)

        self.carImage = ctk.CTkLabel(self.firstPane, image=car_image, text="", width=260, justify=CENTER)
        self.carImage.place(x=20, y=95)

        self.secondPane = ctk.CTkFrame(self.mainPane, width=300, height=105, corner_radius=5, fg_color="white",
                                       bg_color="#e3e7e6")
        self.secondPane.place(x=342, y=60)

        self.nrOfRefuelingsLabel = ctk.CTkLabel(self.secondPane, text="99",
                                                font=("Century Gothic", 30, "bold"),
                                                fg_color="white", text_color="#00a05e")
        self.nrOfRefuelingsLabel.place(x=45, y=18)

        self.refuelLabel = ctk.CTkLabel(self.secondPane, text="Refuelings done",
                                        font=("Century Gothic", 15, "bold"),
                                        fg_color="white", text_color="#555555")
        self.refuelLabel.place(x=45, y=50)

        self.fuelImage = ctk.CTkLabel(self.secondPane, image=fuel_image, text="")
        self.fuelImage.place(x=210, y=27)

        self.thirdPane = ctk.CTkFrame(self.mainPane, width=300, height=105, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")
        self.thirdPane.place(x=342, y=185)

        self.nrOfServicesLabel = ctk.CTkLabel(self.thirdPane, text="99",
                                              font=("Century Gothic", 30, "bold"),
                                              fg_color="white", text_color="#00a05e")
        self.nrOfServicesLabel.place(x=45, y=20)

        self.serviceLabel = ctk.CTkLabel(self.thirdPane, text="Services made",
                                         font=("Century Gothic", 15, "bold"),
                                         fg_color="white", text_color="#555555")
        self.serviceLabel.place(x=45, y=50)

        self.serviceImage = ctk.CTkLabel(self.thirdPane, image=service_image, text="")
        self.serviceImage.place(x=210, y=27)

        self.fourthPane = ctk.CTkFrame(self.mainPane, width=622, height=375, corner_radius=5, fg_color="white",
                                       bg_color="#e3e7e6")
        self.fourthPane.place(x=20, y=309)

        self.makePlot()

        self.fifthPane = ctk.CTkFrame(self.mainPane, width=250, height=200, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")
        self.fifthPane.place(x=660, y=60)

        self.cal = Calendar(self.fifthPane, selectmode='day',
                            year=datetime.now().year, month=datetime.now().month,
                            day=datetime.now().day, selectbackground='gray80',
                            selectforeground='black',
                            normalbackground='white',
                            normalforeground='black',
                            background='gray90',
                            foreground='black',
                            bordercolor='gray90',
                            othermonthforeground='gray50',
                            othermonthbackground='white',
                            othermonthweforeground='gray50',
                            othermonthwebackground='white',
                            weekendbackground='white',
                            weekendforeground='black',
                            headersbackground='white',
                            headersforeground='gray70')
        self.cal.pack(fill="both", expand=True)
        self.cal.bind("<<CalendarSelected>>", self.calendar_click_callback)

        self.sixthPane = ctk.CTkFrame(self.mainPane, width=250, height=418, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")
        self.sixthPane.place(x=660, y=265)

        self.eventsOnLabel = ctk.CTkLabel(self.sixthPane, text="Events on:", font=("Century Gothic", 15, "bold"),
                                          fg_color="white", text_color="#00a05e")
        self.eventsOnLabel.place(x=55, y=20)

        self.dateLabel = ctk.CTkLabel(self.sixthPane,
                                      text=str(datetime.now().day) + "." + str(datetime.now().month) + "." + str(
                                          datetime.now().year), font=("Century Gothic", 15, "bold"),
                                      fg_color="white", text_color="#555555")
        self.dateLabel.place(x=135, y=20)

        self.seventhPane = ctk.CTkScrollableFrame(self.mainPane, width=800, height=610, corner_radius=5,
                                                  fg_color="white",
                                                  bg_color="#e3e7e6")

        self.fuelPaneHeaderLabel = ctk.CTkLabel(self.seventhPane, text="Fuel purchase history", width=800,
                                                fg_color="white", text_color="#00a05e",
                                                font=("Century Gothic", 18, "bold"))
        self.fuelPaneHeaderLabel.grid(row=0, column=0, pady=12)

        self.eighthPane = ctk.CTkFrame(self.mainPane, width=50, height=50, corner_radius=5, fg_color="#00a05e",
                                       bg_color="white")

        self.ninthPane = ctk.CTkFrame(self.mainPane, width=890, height=625, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")

        self.plusImage = ctk.CTkLabel(self.eighthPane, image=plus_image, text="", cursor="hand2")
        self.plusImage.place(x=1, y=1)
        self.plusImage.bind('<Button-1>', self.add_fuel_record_callback)

        self.backImage = ctk.CTkLabel(self.ninthPane, image=back_image, text="", cursor="hand2")
        self.backImage.place(x=5, y=5)
        self.backImage.bind('<Button-1>', lambda event, crud=crud: self.add_fuel_record_back_callback(crud))

        self.dashboardImage = ctk.CTkLabel(self.leftStrip, image=dashboard_image, text="", cursor="hand2")
        self.dashboardImage.place(x=16, y=150)
        self.dashboardImage.bind('<Button-1>', self.dash_button_callback)

        self.accountImage = ctk.CTkLabel(self.leftStrip, image=account_image, text="", cursor="hand2")
        self.accountImage.place(x=16, y=250)
        self.accountImage.bind('<Button-1>', self.acc_button_callback)

        self.settingsImage = ctk.CTkLabel(self.leftStrip, image=settings_image, text="", cursor="hand2")
        self.settingsImage.place(x=16, y=350)
        self.settingsImage.bind('<Button-1>', self.sett_button_callback)

        self.logoutImage = ctk.CTkLabel(self.leftStrip, image=logout_image, text="", cursor="hand2")
        self.logoutImage.place(x=19, y=450)
        self.logoutImage.bind('<Button-1>', self.log_button_callback)

        self.selectedTabIndicator = ctk.CTkFrame(self.leftStrip, width=5, height=40, fg_color="white")
        self.selectedTabIndicator.place(x=4, y=148)

        self.loadFuelRecords(crud)
        self.nrOfRefuelingsLabel.configure(text=str(len(self.fuelRecordPanes)))

    def add_fuel_record_callback(self, event):
        self.ninthPane.place(x=20, y=60)
        self.seventhPane.place_forget()
        # crud.createFuelRecord(self.login_window.accountLogin, 2023, 12, 23, 300, 40, "PB95", "Orlen")

    def add_fuel_record_back_callback(self, crud):
        self.seventhPane.place(x=20, y=60)
        self.ninthPane.place_forget()
        self.loadFuelRecords(crud)

    def calendar_click_callback(self, event):
        selected_date_str = self.cal.get_date()
        selected_date = datetime.strptime(selected_date_str, "%m/%d/%y")

        day = selected_date.day
        month = selected_date.month
        year = selected_date.year

        self.dateLabel.configure(text=str(day) + "." + str(month) + "." + str(year))
        self.dateLabel.update()

    def dash_button_callback(self, event):
        if self.leftPane.cget("width") == 70:
            self.selectedTabIndicator.place(x=4, y=148)
            self.master.after(1, self.dash_button_callback_effect)

    def dash_button_callback_effect(self):
        if self.leftPane.cget("width") != 270:
            self.leftPane.configure(width=self.leftPane.cget("width") + 4)
            self.mainPane.place(x=self.mainPane.winfo_x() + 4)
            self.leftPane.update()
            self.mainPane.update()
            self.master.after(1, self.dash_button_callback_effect)
        else:
            if whichButtonPressed == 1:
                self.showOverviewComponents()
            elif whichButtonPressed == 2:
                self.showFuelComponents()
            self.showAccountInfoComponents()
            self.leftPane.update()

    def acc_button_callback(self, event):
        if self.leftPane.cget("width") == 70:
            self.selectedTabIndicator.place(x=4, y=248)
        if self.leftPane.cget("width") == 270:
            self.selectedTabIndicator.place(x=4, y=248)
            self.hideAccountInfoComponents()
            self.hideOverviewComponents()
            self.hideFuelComponents()
            self.master.after(1, self.acc_button_callback_effect)

    def acc_button_callback_effect(self):
        if self.leftPane.cget("width") != 70:
            self.leftPane.configure(width=self.leftPane.cget("width") - 4)
            self.mainPane.place(x=self.mainPane.winfo_x() - 4)
            self.leftPane.update()
            self.mainPane.update()
            self.master.after(1, self.acc_button_callback_effect)
        else:
            self.leftPane.update()

    def sett_button_callback(self, event):
        if self.leftPane.cget("width") == 70:
            self.selectedTabIndicator.place(x=4, y=348)
        if self.leftPane.cget("width") == 270:
            self.selectedTabIndicator.place(x=4, y=348)
            self.hideAccountInfoComponents()
            self.hideOverviewComponents()
            self.hideFuelComponents()
            self.master.after(1, self.sett_button_callback_effect)

    def sett_button_callback_effect(self):
        if self.leftPane.cget("width") != 70:
            self.leftPane.configure(width=self.leftPane.cget("width") - 4)
            self.mainPane.place(x=self.mainPane.winfo_x() - 4)
            self.leftPane.update()
            self.mainPane.update()
            self.master.after(1, self.sett_button_callback_effect)
        else:
            self.leftPane.update()

    def log_button_callback(self, event):
        if self.leftPane.cget("width") == 70:
            self.selectedTabIndicator.place(x=4, y=448)
        if self.leftPane.cget("width") == 270:
            self.selectedTabIndicator.place(x=4, y=448)
            self.hideAccountInfoComponents()
            self.hideOverviewComponents()
            self.hideFuelComponents()
            self.master.after(1, self.log_button_callback_effect)

    def log_button_callback_effect(self):
        if self.leftPane.cget("width") != 70:
            self.leftPane.configure(width=self.leftPane.cget("width") - 4)
            self.mainPane.place(x=self.mainPane.winfo_x() - 4)
            self.leftPane.update()
            self.mainPane.update()
            self.master.after(1, self.log_button_callback_effect)
        else:
            self.leftPane.update()

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

        self.showOverviewComponents()
        self.hideFuelComponents()

    def fuel_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 2
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.showFuelComponents()
        self.hideOverviewComponents()

    def services_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 3
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.hideOverviewComponents()
        self.hideFuelComponents()

    def cars_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 4
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.hideOverviewComponents()
        self.hideFuelComponents()

    def nearby_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 5
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.hideOverviewComponents()
        self.hideFuelComponents()

    def hideOverviewComponents(self):
        self.firstPane.place_forget()
        self.secondPane.place_forget()
        self.thirdPane.place_forget()
        self.fourthPane.place_forget()
        self.fifthPane.place_forget()
        self.sixthPane.place_forget()

    def showOverviewComponents(self):
        self.firstPane.place(x=20, y=60)
        self.secondPane.place(x=342, y=60)
        self.thirdPane.place(x=342, y=185)
        self.fourthPane.place(x=20, y=309)
        self.fifthPane.place(x=660, y=60)
        self.sixthPane.place(x=660, y=265)

    def showFuelComponents(self):
        self.eighthPane.place(x=860, y=630)
        self.seventhPane.place(x=20, y=60)

    def hideFuelComponents(self):
        self.seventhPane.place_forget()
        self.eighthPane.place_forget()

    def showAccountInfoComponents(self):
        self.accInfoImage.place(x=810, y=5)
        self.accountInfo.place(x=834, y=10)

    def hideAccountInfoComponents(self):
        self.accInfoImage.place_forget()
        self.accountInfo.place_forget()

    def loadFuelRecords(self, crud):
        year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data = crud.readFuelRecord("123")
        i = 0
        j = 0

        self.fuelRecordPanes.clear()
        self.fuelYearLabels.clear()

        for record in year_data:
            self.fuelRecordPanes.append(
                ctk.CTkFrame(self.seventhPane, width=750, height=100, corner_radius=5, fg_color="#e3e7e6",
                             bg_color="white"))
            self.fuelYearLabels.append(
                ctk.CTkLabel(self.fuelRecordPanes[i], text=year_data[i], fg_color="#e3e7e6",
                             text_color="#02ac69"))
            i = i + 1

        for pane in self.fuelRecordPanes:
            pane.grid(row=j + 1, column=0, pady=15, padx=25)
            self.fuelYearLabels[j].place(x=20, y=20)
            j = j + 1
