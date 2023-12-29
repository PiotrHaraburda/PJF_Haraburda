import os
import re
from datetime import datetime, timedelta
from tkinter import *
import customtkinter as ctk
import pytesseract
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkcalendar import Calendar
import matplotlib.pyplot as plt
import cv2
import numpy as np

whichButtonPressed = 1


class MainWindow(ctk.CTk):

    def __init__(self, master, login_window, main_image2, account_info_image, dashboard_image, account_image,
                 settings_image,
                 logout_image, fuel_image, service_image, car_image, plus_image, back_image,receipt_image, crud, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.login_window = login_window
        self.fuelRecordPanes = []
        self.dateLabels = []
        self.infoLabels = []

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

        self.accInfoImage = ctk.CTkLabel(self.mainPane, image=account_info_image, text="")
        self.accInfoImage.place(x=810, y=5)

        self.carPane = ctk.CTkFrame(self.mainPane, width=300, height=230, corner_radius=5, fg_color="white",
                                    bg_color="#e3e7e6")
        self.carPane.place(x=20, y=60)

        self.carNameLabel = ctk.CTkLabel(self.carPane, text="Lexus IS200",
                                         font=("Century Gothic", 25, "bold"), height=20,
                                         fg_color="white", text_color="#555555", width=260, justify=CENTER)
        self.carNameLabel.place(x=20, y=20)

        self.yourCarLabel = ctk.CTkLabel(self.carPane, text="Your personal vehicle",
                                         font=("Century Gothic", 15, "bold"), height=20,
                                         fg_color="white", text_color="#00a05e", width=260, justify=CENTER)
        self.yourCarLabel.place(x=20, y=50)

        self.carImage = ctk.CTkLabel(self.carPane, image=car_image, text="", width=260, justify=CENTER)
        self.carImage.place(x=20, y=95)

        self.fuelNumberPane = ctk.CTkFrame(self.mainPane, width=300, height=105, corner_radius=5, fg_color="white",
                                           bg_color="#e3e7e6")
        self.fuelNumberPane.place(x=342, y=60)

        self.nrOfRefuelingsLabel = ctk.CTkLabel(self.fuelNumberPane, text="99",
                                                font=("Century Gothic", 30, "bold"),
                                                fg_color="white", text_color="#00a05e")
        self.nrOfRefuelingsLabel.place(x=45, y=18)

        self.refuelLabel = ctk.CTkLabel(self.fuelNumberPane, text="Refuelings done",
                                        font=("Century Gothic", 15, "bold"),
                                        fg_color="white", text_color="#555555")
        self.refuelLabel.place(x=45, y=50)

        self.fuelImage = ctk.CTkLabel(self.fuelNumberPane, image=fuel_image, text="")
        self.fuelImage.place(x=210, y=27)

        self.servicesNumberPane = ctk.CTkFrame(self.mainPane, width=300, height=105, corner_radius=5, fg_color="white",
                                               bg_color="#e3e7e6")
        self.servicesNumberPane.place(x=342, y=185)

        self.nrOfServicesLabel = ctk.CTkLabel(self.servicesNumberPane, text="99",
                                              font=("Century Gothic", 30, "bold"),
                                              fg_color="white", text_color="#00a05e")
        self.nrOfServicesLabel.place(x=45, y=20)

        self.serviceLabel = ctk.CTkLabel(self.servicesNumberPane, text="Services made",
                                         font=("Century Gothic", 15, "bold"),
                                         fg_color="white", text_color="#555555")
        self.serviceLabel.place(x=45, y=50)

        self.serviceImage = ctk.CTkLabel(self.servicesNumberPane, image=service_image, text="")
        self.serviceImage.place(x=210, y=27)

        self.plotPane = ctk.CTkFrame(self.mainPane, width=622, height=375, corner_radius=5, fg_color="white",
                                     bg_color="#e3e7e6")
        self.plotPane.place(x=20, y=309)

        self.make_plot()

        self.calendarPane = ctk.CTkFrame(self.mainPane, width=250, height=200, corner_radius=5, fg_color="white",
                                         bg_color="#e3e7e6")
        self.calendarPane.place(x=660, y=60)

        self.cal = Calendar(self.calendarPane, selectmode='day',
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
        self.cal.bind("<<CalendarSelected>>", lambda event, crud=crud: self.calendar_click_callback(crud))

        self.calendarInfoPane = ctk.CTkFrame(self.mainPane, width=250, height=300, corner_radius=5, fg_color="white",
                                             bg_color="#e3e7e6")
        self.calendarInfoPane.place(x=660, y=265)

        self.eventsOnLabel = ctk.CTkLabel(self.calendarInfoPane, text="Events on:", font=("Century Gothic", 18, "bold"),
                                          fg_color="white", text_color="#00a05e")
        self.eventsOnLabel.place(x=32, y=20)

        self.dateLabel = ctk.CTkLabel(self.calendarInfoPane,
                                      text=str(datetime.now().day) + "." + str(datetime.now().month) + "." + str(
                                          datetime.now().year), font=("Century Gothic", 18, "bold"),
                                      fg_color="white", text_color="#555555")
        self.dateLabel.place(x=128, y=20)

        self.refuelingsNumberOnDateLabel=ctk.CTkLabel(self.calendarInfoPane, text="0x", font=("Century Gothic", 19, "bold"),
                                                      fg_color="white", text_color="#00a05e", width=250, justify=CENTER)
        self.refuelingsNumberOnDateLabel.place(x=0, y=95)

        self.refuelingsOnDateLabel = ctk.CTkLabel(self.calendarInfoPane, text="Refuelings made", font=("Century Gothic", 15, "bold"),
                                                  fg_color="white", text_color="#555555", width=250, justify=CENTER)
        self.refuelingsOnDateLabel.place(x=0, y=120)

        self.servicesNumberOnDateLabel = ctk.CTkLabel(self.calendarInfoPane, text="0x", font=("Century Gothic", 19, "bold"),
                                                      fg_color="white", text_color="#00a05e", width=250,
                                                      justify=CENTER)
        self.servicesNumberOnDateLabel.place(x=0, y=180)

        self.servicesOnDateLabel = ctk.CTkLabel(self.calendarInfoPane, text="Services made",
                                                font=("Century Gothic", 15, "bold"),
                                                fg_color="white", text_color="#555555", width=250, justify=CENTER)
        self.servicesOnDateLabel.place(x=0, y=205)

        self.sloganPane = ctk.CTkFrame(self.mainPane, width=250, height=96, corner_radius=5, fg_color="white",
                                             bg_color="#e3e7e6")
        self.sloganPane.place(x=660, y=587)

        self.sloganLabel = ctk.CTkLabel(self.sloganPane,
                                      text="MileageMate:\nTrack Auto Costs Effortlessly!", font=("Century Gothic", 13, "bold"),
                                      fg_color="white", text_color="#00a05e",width=250,justify=CENTER)
        self.sloganLabel.place(x=0, y=30)

        self.seventhPane = ctk.CTkScrollableFrame(self.mainPane, width=800, height=610, corner_radius=5,
                                                  fg_color="white",
                                                  bg_color="#e3e7e6")

        self.fuelPaneHeaderLabel = ctk.CTkLabel(self.seventhPane, text="Fuel purchase history", width=800,
                                                fg_color="white", text_color="#00a05e",
                                                font=("Century Gothic", 20, "bold"))
        self.fuelPaneHeaderLabel.grid(row=0, column=0, pady=12)

        self.eighthPane = ctk.CTkFrame(self.mainPane, width=50, height=50, corner_radius=5, fg_color="#00a05e",
                                       bg_color="white")

        self.plusImage = ctk.CTkLabel(self.eighthPane, image=plus_image, text="", cursor="hand2")
        self.plusImage.place(x=1, y=1)
        self.plusImage.bind('<Button-1>', self.add_fuel_record_callback)

        self.ninthPane = ctk.CTkFrame(self.mainPane, width=890, height=625, corner_radius=5, fg_color="white",
                                      bg_color="#e3e7e6")

        self.backImage = ctk.CTkLabel(self.ninthPane, image=back_image, text="", cursor="hand2")
        self.backImage.place(x=5, y=15)
        self.backImage.bind('<Button-1>', lambda event, crud=crud: self.add_fuel_record_back_callback(crud))

        self.addNewFuelRecordLabel = ctk.CTkLabel(self.ninthPane, text="Adding new fuel purchase record",
                                                  text_color="#00a05e", width=810,
                                                  fg_color="white",
                                                  font=("Century Gothic", 20, "bold"), justify=CENTER)
        self.addNewFuelRecordLabel.place(x=40, y=20)

        self.dayTextBox = ctk.CTkTextbox(self.ninthPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                         bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                         border_spacing=10)

        self.monthTextBox = ctk.CTkTextbox(self.ninthPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                           border_spacing=10)

        self.yearTextBox = ctk.CTkTextbox(self.ninthPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                          bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                          border_spacing=10)

        self.moneyTextBox = ctk.CTkTextbox(self.ninthPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                           border_spacing=10)

        self.litersTextBox = ctk.CTkTextbox(self.ninthPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                            bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                            border_spacing=10)

        self.fueltypeTextBox = ctk.CTkTextbox(self.ninthPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                              bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                              border_spacing=10)

        self.stationTextBox = ctk.CTkTextbox(self.ninthPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                             bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                             border_spacing=10)

        self.dayLabel = ctk.CTkLabel(self.ninthPane, text="Day:", text_color="#555555", font=("Trebuchet", 15, "bold"),
                                     bg_color="white")
        self.monthLabel = ctk.CTkLabel(self.ninthPane, text="Month:", text_color="#555555",
                                       font=("Trebuchet", 15, "bold"),
                                       bg_color="white")
        self.yearLabel = ctk.CTkLabel(self.ninthPane, text="Year:", text_color="#555555",
                                      font=("Trebuchet", 15, "bold"),
                                      bg_color="white")
        self.moneyLabel = ctk.CTkLabel(self.ninthPane, text="Money Spent:", text_color="#555555",
                                       font=("Trebuchet", 15, "bold"),
                                       bg_color="white")
        self.litersLabel = ctk.CTkLabel(self.ninthPane, text="Liters Refueled:", text_color="#555555",
                                        font=("Trebuchet", 15, "bold"),
                                        bg_color="white")
        self.fueltypeLabel = ctk.CTkLabel(self.ninthPane, text="Fuel Type:", text_color="#555555",
                                          font=("Trebuchet", 15, "bold"),
                                          bg_color="white")
        self.stationLabel = ctk.CTkLabel(self.ninthPane, text="Gas Station:", text_color="#555555",
                                         font=("Trebuchet", 15, "bold"),
                                         bg_color="white")

        self.addNewFuelRecordButton = ctk.CTkButton(self.ninthPane, text="Add new record", fg_color="white",
                                                    font=("Trebuchet", 14, "bold"),
                                                    width=310, height=35, corner_radius=5, hover_color="#dbdbd9",
                                                    bg_color="white", border_width=1, text_color="#555555",
                                                    command=lambda: self.add_new_fuel_record(crud))

        self.dayTextBox.place(x=90, y=120)
        self.monthTextBox.place(x=90, y=220)
        self.yearTextBox.place(x=90, y=320)
        self.moneyTextBox.place(x=90, y=420)
        self.litersTextBox.place(x=490, y=120)
        self.fueltypeTextBox.place(x=490, y=220)
        self.stationTextBox.place(x=490, y=320)

        self.dayLabel.place(x=90, y=90)
        self.monthLabel.place(x=90, y=190)
        self.yearLabel.place(x=90, y=290)
        self.moneyLabel.place(x=90, y=390)
        self.litersLabel.place(x=490, y=90)
        self.fueltypeLabel.place(x=490, y=190)
        self.stationLabel.place(x=490, y=290)

        self.addNewFuelRecordButton.place(x=290, y=550)

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

        self.mainPane.bind("<Map>", lambda event, crud=crud: self.accountInfoUpdate(crud))


        self.scanReceiptImage()

    def scanReceiptImage(self):
        # Wczytaj obraz
        image = cv2.imread('images/receipt.jpg')

        # Konwersja na odcienie szarości
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Usunięcie szumu
        blurred = cv2.medianBlur(gray, 5)

        # Binaryzacja
        thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Dylatacja
        kernel = np.ones((1, 1), np.uint8)
        dilated = cv2.dilate(thresholded, kernel, iterations=1)

        # Erozja
        eroded = cv2.erode(dilated, kernel, iterations=1)

        # Otwarcie
        opened = cv2.morphologyEx(eroded, cv2.MORPH_OPEN, kernel)

        # Detekcja krawędzi Canny
        edges = cv2.Canny(opened, 50, 300)

        # Korekcja nachylenia
        coords = np.column_stack(np.where(edges > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = edges.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(edges, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

        resized_image = cv2.resize(blurred, (465, 855))
        cv2.imshow('Processed Image', resized_image)

        custom_config = r'--oem 3 --psm 11'
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        result=pytesseract.image_to_string(blurred,lang="pol",config=custom_config)

        pattern_dot = re.compile(r'PLN[^\d]*(\d+\.\d{2})')
        pattern_comma = re.compile(r'PLN[^\d]*(\d+,[^\d]\d{2})')

        # Szukanie informacji o kwocie wydanej na paliwo
        match_dot = re.search(pattern_dot, result)
        match_comma = re.search(pattern_comma, result)

        print(result)

        # Jeśli znaleziono kwotę z kropką, wyświetl ją
        if match_dot:
            spent_on_fuel_dot = float(match_dot.group(1))
            print(f'Kwota wydana na paliwo (kropka): {spent_on_fuel_dot} PLN')

        # Jeśli znaleziono kwotę z przecinkiem, wyświetl ją
        elif match_comma:
            spent_on_fuel_comma = float(match_comma.group(1).replace(',', '.').replace(' ', ''))
            print(f'Kwota wydana na paliwo (przecinek): {spent_on_fuel_comma} PLN')

        else:
            print('Nie znaleziono informacji o kwocie wydanej na paliwo.')

    def add_new_fuel_record(self, crud):
        year = self.yearTextBox.get("0.0", 'end-1c')
        month = self.monthTextBox.get("0.0", 'end-1c')
        day = self.dayTextBox.get("0.0", 'end-1c')
        money = self.moneyTextBox.get("0.0", 'end-1c')
        liters = self.litersTextBox.get("0.0", 'end-1c')
        fueltype = self.fueltypeTextBox.get("0.0", 'end-1c')
        station = self.stationTextBox.get("0.0", 'end-1c')
        crud.createFuelRecord(self.login_window.accountLogin, year, month, day, money, liters, fueltype, station)
        self.loadFuelRecords(crud)
        self.nrOfRefuelingsLabel.configure(text=str(len(self.fuelRecordPanes)))

    def add_fuel_record_callback(self, event):
        self.ninthPane.place(x=20, y=60)
        self.seventhPane.place_forget()

    def add_fuel_record_back_callback(self, crud):
        self.seventhPane.place(x=20, y=60)
        self.ninthPane.place_forget()

    def calendar_click_callback(self, crud):
        selected_date_str = self.cal.get_date()
        selected_date = datetime.strptime(selected_date_str, "%m/%d/%y")

        day = str(selected_date.day)
        if len(day)==1:
            day="0"+day
        month = str(selected_date.month)
        if len(month)==1:
            month="0"+month
        year = str(selected_date.year)

        self.dateLabel.configure(text=day + "." + month + "." + year)
        self.dateLabel.update()

        self.refuelingsNumberOnDateLabel.configure(text=str(crud.read_nr_of_fuel_records(self.login_window.accountLogin,day,month,year))+"x")

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

    def make_plot(self):
        current_date = datetime.now()
        # Lista nazw miesięcy
        month_names = []

        # Tworzenie listy nazw 7 ostatnich miesięcy
        for i in range(7):
            month_names.append(current_date.strftime('%B'))
            current_date -= timedelta(days=30)  # zakładamy, że miesiące mają średnio 30 dni

        month_names.reverse()

        data1 = {'Month': month_names,
                 '[zł] spent': [0, 0, 0, 0, 0, 0, 300.4]
                 }
        df1 = pd.DataFrame(data1)

        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        figure1.subplots_adjust(bottom=0.4)
        ax1 = figure1.add_subplot(111)
        ax1.tick_params(axis='x', labelsize=8)
        bar1 = FigureCanvasTkAgg(figure1, self.plotPane)
        bar1.get_tk_widget().place(x=0, y=0)
        df1.plot(kind='bar', legend=True, ax=ax1, color="#085f3d")
        ax1.set_xticklabels(month_names, rotation=0)
        ax1.set_title('Money spent in recent months')

    def accountInfoUpdate(self, crud):
        accountLogin = self.login_window.accountLogin
        self.accountInfo.configure(text=accountLogin)
        self.loadFuelRecords(crud)
        self.nrOfRefuelingsLabel.configure(text=str(len(self.fuelRecordPanes)))
        self.accountInfo.update()
        self.nrOfRefuelingsLabel.update()
        self.calendar_click_callback(crud)

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
        self.carPane.place_forget()
        self.fuelNumberPane.place_forget()
        self.servicesNumberPane.place_forget()
        self.plotPane.place_forget()
        self.calendarPane.place_forget()
        self.calendarInfoPane.place_forget()
        self.sloganPane.place_forget()

    def showOverviewComponents(self):
        self.carPane.place(x=20, y=60)
        self.fuelNumberPane.place(x=342, y=60)
        self.servicesNumberPane.place(x=342, y=185)
        self.plotPane.place(x=20, y=309)
        self.calendarPane.place(x=660, y=60)
        self.calendarInfoPane.place(x=660, y=265)
        self.sloganPane.place(x=660, y=587)

    def showFuelComponents(self):
        self.eighthPane.place(x=860, y=630)
        self.seventhPane.place(x=20, y=60)

    def hideFuelComponents(self):
        self.seventhPane.place_forget()
        self.eighthPane.place_forget()
        self.ninthPane.place_forget()

    def showAccountInfoComponents(self):
        self.accInfoImage.place(x=810, y=5)
        self.accountInfo.place(x=834, y=10)

    def hideAccountInfoComponents(self):
        self.accInfoImage.place_forget()
        self.accountInfo.place_forget()

    def loadFuelRecords(self, crud):

        for pane in self.fuelRecordPanes:
            pane.destroy()

        self.fuelRecordPanes.clear()
        self.dateLabels.clear()
        self.infoLabels.clear()

        year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data = crud.read_fuel_records(
            self.login_window.accountLogin)

        fuel_records = list(zip(year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data))

        fuel_records = [(int(record[0]), int(record[1]), int(record[2]), record[3], record[4], record[5], record[6]) for
                        record in fuel_records]

        fuel_records = [
            (record[0], f"{int(record[1]):02d}", f"{int(record[2]):02d}", record[3], record[4], record[5], record[6])
            for record in fuel_records]

        sorted_records = sorted(fuel_records, key=lambda x: (x[0], x[1], x[2]),reverse=True)

        year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data = zip(*sorted_records)

        i = 0
        j = 0

        for record in year_data:
            self.fuelRecordPanes.append(
                ctk.CTkFrame(self.seventhPane, width=750, height=100, corner_radius=5, fg_color="#e3e7e6",
                             bg_color="white"))
            self.dateLabels.append(
                ctk.CTkLabel(self.fuelRecordPanes[i],
                             text=str(day_data[i]) + "." + str(month_data[i]) + "." + str(year_data[i]),
                             fg_color="#e3e7e6",
                             text_color="#00a05e", width=750, font=("Century Gothic", 17, "bold"), justify=CENTER))
            self.infoLabels.append(
                ctk.CTkLabel(self.fuelRecordPanes[i],
                             text=str(money_data[i]) + "zł spent on " + str(liters_data[i]) + "l of " +
                                  str(fuel_data[i]) + " at " + str(station_data[i]) + " gas station.",
                             fg_color="#e3e7e6",
                             text_color="#555555", width=750, font=("Century Gothic", 18, "bold"), justify=CENTER))
            i = i + 1

        for pane in self.fuelRecordPanes:
            pane.grid(row=j + 1, column=0, pady=15, padx=25)
            self.dateLabels[j].place(x=0, y=15)
            self.infoLabels[j].place(x=0, y=50)
            j = j + 1
