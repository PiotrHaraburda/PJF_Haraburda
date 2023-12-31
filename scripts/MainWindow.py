import re
from datetime import datetime, timedelta
from tkinter import *
import customtkinter as ctk
import geocoder
import pytesseract
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkcalendar import Calendar
import matplotlib.pyplot as plt
import cv2
import numpy as np
from tkintermapview import TkinterMapView

whichButtonPressed = 1


class MainWindow(ctk.CTk):

    def __init__(self, master, login_app, login_window, main_image2, account_info_image, dashboard_image, account_image,
                 settings_image,
                 logout_image, fuel_image, service_image, car_image, plus_image, back_image, receipt_image, crud,
                 **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.login_app = login_app

        self.fuelRecordPanes = []
        self.dateLabels = []
        self.infoLabels = []

        self.serviceRecordPanes = []
        self.dateLabels2 = []
        self.infoLabels2 = []
        self.successfulLabels = []

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

        self.accountInfo = ctk.CTkLabel(self.mainPane, text="<Login>", font=("Century Gothic", 15, "bold"), height=20,
                                        fg_color="#e3e7e6", bg_color="#e3e7e6", text_color="#555555")
        self.accountInfo.place(x=44, y=18)

        self.accInfoImage = ctk.CTkLabel(self.mainPane, image=account_info_image, text="")
        self.accInfoImage.place(x=20, y=13)

        self.carPane = ctk.CTkFrame(self.mainPane, width=300, height=230, corner_radius=5, fg_color="white",
                                    bg_color="#e3e7e6")
        self.carPane.place(x=20, y=60)

        self.carNameLabel = ctk.CTkLabel(self.carPane, text="Car not added!",
                                         font=("Century Gothic", 22, "bold"), height=20,
                                         fg_color="white", text_color="#555555", width=300, justify=CENTER)
        self.carNameLabel.place(x=0, y=20)

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
        self.nrOfServicesLabel.place(x=45, y=18)

        self.serviceLabel = ctk.CTkLabel(self.servicesNumberPane, text="Services made",
                                         font=("Century Gothic", 15, "bold"),
                                         fg_color="white", text_color="#555555")
        self.serviceLabel.place(x=45, y=50)

        self.serviceImage = ctk.CTkLabel(self.servicesNumberPane, image=service_image, text="")
        self.serviceImage.place(x=210, y=27)

        self.plotPane = ctk.CTkFrame(self.mainPane, width=622, height=375, corner_radius=5, fg_color="white",
                                     bg_color="#e3e7e6")
        self.plotPane.place(x=20, y=309)

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

        self.refuelingsNumberOnDateLabel = ctk.CTkLabel(self.calendarInfoPane, text="0x",
                                                        font=("Century Gothic", 19, "bold"),
                                                        fg_color="white", text_color="#00a05e", width=250,
                                                        justify=CENTER)
        self.refuelingsNumberOnDateLabel.place(x=0, y=95)

        self.refuelingsOnDateLabel = ctk.CTkLabel(self.calendarInfoPane, text="Refuelings made",
                                                  font=("Century Gothic", 15, "bold"),
                                                  fg_color="white", text_color="#555555", width=250, justify=CENTER)
        self.refuelingsOnDateLabel.place(x=0, y=120)

        self.servicesNumberOnDateLabel = ctk.CTkLabel(self.calendarInfoPane, text="0x",
                                                      font=("Century Gothic", 19, "bold"),
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
                                        text="MileageMate:\nTrack Auto Costs Effortlessly!",
                                        font=("Century Gothic", 13, "bold", "italic"),
                                        fg_color="white", text_color="#00a05e", width=250, justify=CENTER)
        self.sloganLabel.place(x=0, y=30)

        self.fuelListPane = ctk.CTkScrollableFrame(self.mainPane, width=800, height=610, corner_radius=5,
                                                   fg_color="white",
                                                   bg_color="#e3e7e6")

        self.fuelPaneHeaderLabel = ctk.CTkLabel(self.fuelListPane, text="Fuel purchase history", width=800,
                                                fg_color="white", text_color="#00a05e",
                                                font=("Century Gothic", 20, "bold"))
        self.fuelPaneHeaderLabel.grid(row=0, column=0, pady=12)

        self.addFuelButtonPane = ctk.CTkFrame(self.mainPane, width=50, height=50, corner_radius=5, fg_color="#00a05e",
                                              bg_color="white")

        self.plusImage = ctk.CTkLabel(self.addFuelButtonPane, image=plus_image, text="", cursor="hand2")
        self.plusImage.place(x=1, y=1)
        self.plusImage.bind('<Button-1>', self.add_fuel_record_callback)

        self.addFuelPane = ctk.CTkFrame(self.mainPane, width=890, height=625, corner_radius=5, fg_color="white",
                                        bg_color="#e3e7e6")

        self.backImage = ctk.CTkLabel(self.addFuelPane, image=back_image, text="", cursor="hand2")
        self.backImage.place(x=5, y=15)
        self.backImage.bind('<Button-1>', lambda event, crud=crud: self.add_fuel_record_back_callback(crud))

        self.addNewFuelRecordLabel = ctk.CTkLabel(self.addFuelPane, text="Adding new fuel purchase record",
                                                  text_color="#00a05e", width=810,
                                                  fg_color="white",
                                                  font=("Century Gothic", 20, "bold"), justify=CENTER)
        self.addNewFuelRecordLabel.place(x=40, y=20)

        self.dayTextBox = ctk.CTkTextbox(self.addFuelPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                         bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                         border_spacing=10)

        self.monthTextBox = ctk.CTkTextbox(self.addFuelPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                           border_spacing=10)

        self.yearTextBox = ctk.CTkTextbox(self.addFuelPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                          bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                          border_spacing=10)

        self.moneyTextBox = ctk.CTkTextbox(self.addFuelPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                           border_spacing=10)

        self.litersTextBox = ctk.CTkTextbox(self.addFuelPane, width=310, height=50, corner_radius=5, fg_color="#dbfde7",
                                            bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                            border_spacing=10)

        self.fueltypeTextBox = ctk.CTkTextbox(self.addFuelPane, width=310, height=50, corner_radius=5,
                                              fg_color="#dbfde7",
                                              bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                              border_spacing=10)

        self.stationTextBox = ctk.CTkTextbox(self.addFuelPane, width=310, height=50, corner_radius=5,
                                             fg_color="#dbfde7",
                                             bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                             border_spacing=10)

        self.dayLabel = ctk.CTkLabel(self.addFuelPane, text="Day:", text_color="#555555",
                                     font=("Trebuchet", 15, "bold"),
                                     bg_color="white")
        self.monthLabel = ctk.CTkLabel(self.addFuelPane, text="Month:", text_color="#555555",
                                       font=("Trebuchet", 15, "bold"),
                                       bg_color="white")
        self.yearLabel = ctk.CTkLabel(self.addFuelPane, text="Year:", text_color="#555555",
                                      font=("Trebuchet", 15, "bold"),
                                      bg_color="white")
        self.moneyLabel = ctk.CTkLabel(self.addFuelPane, text="Money Spent:", text_color="#555555",
                                       font=("Trebuchet", 15, "bold"),
                                       bg_color="white")
        self.litersLabel = ctk.CTkLabel(self.addFuelPane, text="Liters Refueled:", text_color="#555555",
                                        font=("Trebuchet", 15, "bold"),
                                        bg_color="white")
        self.fueltypeLabel = ctk.CTkLabel(self.addFuelPane, text="Fuel Type:", text_color="#555555",
                                          font=("Trebuchet", 15, "bold"),
                                          bg_color="white")
        self.stationLabel = ctk.CTkLabel(self.addFuelPane, text="Gas Station:", text_color="#555555",
                                         font=("Trebuchet", 15, "bold"),
                                         bg_color="white")

        self.addNewFuelRecordButton = ctk.CTkButton(self.addFuelPane, text="Add new record", fg_color="white",
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

        self.servicesListPane = ctk.CTkScrollableFrame(self.mainPane, width=800, height=610, corner_radius=5,
                                                       fg_color="white",
                                                       bg_color="#e3e7e6")

        self.servicesPaneHeaderLabel = ctk.CTkLabel(self.servicesListPane, text="Services history", width=800,
                                                    fg_color="white", text_color="#00a05e",
                                                    font=("Century Gothic", 20, "bold"))
        self.servicesPaneHeaderLabel.grid(row=0, column=0, pady=12)

        self.addServicesButtonPane = ctk.CTkFrame(self.mainPane, width=50, height=50, corner_radius=5,
                                                  fg_color="#00a05e",
                                                  bg_color="white")

        self.plusImage = ctk.CTkLabel(self.addServicesButtonPane, image=plus_image, text="", cursor="hand2")
        self.plusImage.place(x=1, y=1)
        self.plusImage.bind('<Button-1>', self.add_service_record_callback)

        self.addServicesPane = ctk.CTkFrame(self.mainPane, width=890, height=625, corner_radius=5, fg_color="white",
                                            bg_color="#e3e7e6")

        self.backImage = ctk.CTkLabel(self.addServicesPane, image=back_image, text="", cursor="hand2")
        self.backImage.place(x=5, y=15)
        self.backImage.bind('<Button-1>', lambda event, crud=crud: self.add_service_record_back_callback(crud))

        self.addNewServiceRecordLabel = ctk.CTkLabel(self.addServicesPane, text="Adding new service record",
                                                     text_color="#00a05e", width=810,
                                                     fg_color="white",
                                                     font=("Century Gothic", 20, "bold"), justify=CENTER)
        self.addNewServiceRecordLabel.place(x=40, y=20)

        self.dayTextBox2 = ctk.CTkTextbox(self.addServicesPane, width=310, height=50, corner_radius=5,
                                          fg_color="#dbfde7",
                                          bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                          border_spacing=10)

        self.monthTextBox2 = ctk.CTkTextbox(self.addServicesPane, width=310, height=50, corner_radius=5,
                                            fg_color="#dbfde7",
                                            bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                            border_spacing=10)

        self.yearTextBox2 = ctk.CTkTextbox(self.addServicesPane, width=310, height=50, corner_radius=5,
                                           fg_color="#dbfde7",
                                           bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                           border_spacing=10)

        self.moneyTextBox2 = ctk.CTkTextbox(self.addServicesPane, width=310, height=50, corner_radius=5,
                                            fg_color="#dbfde7",
                                            bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                            border_spacing=10)

        self.serviceTypeTextBox = ctk.CTkTextbox(self.addServicesPane, width=310, height=50, corner_radius=5,
                                                 fg_color="#dbfde7",
                                                 bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                                 border_spacing=10)

        self.ifSuccessfulTextBox = ctk.CTkTextbox(self.addServicesPane, width=310, height=50, corner_radius=5,
                                                  fg_color="#dbfde7",
                                                  bg_color="white", text_color="#555555",
                                                  font=("Trebuchet", 19, "bold"),
                                                  border_spacing=10)

        self.repairShopTextBox = ctk.CTkTextbox(self.addServicesPane, width=310, height=50, corner_radius=5,
                                                fg_color="#dbfde7",
                                                bg_color="white", text_color="#555555", font=("Trebuchet", 19, "bold"),
                                                border_spacing=10)

        self.dayLabel2 = ctk.CTkLabel(self.addServicesPane, text="Day:", text_color="#555555",
                                      font=("Trebuchet", 15, "bold"),
                                      bg_color="white")
        self.monthLabel2 = ctk.CTkLabel(self.addServicesPane, text="Month:", text_color="#555555",
                                        font=("Trebuchet", 15, "bold"),
                                        bg_color="white")
        self.yearLabel2 = ctk.CTkLabel(self.addServicesPane, text="Year:", text_color="#555555",
                                       font=("Trebuchet", 15, "bold"),
                                       bg_color="white")
        self.moneyLabel2 = ctk.CTkLabel(self.addServicesPane, text="Money Spent:", text_color="#555555",
                                        font=("Trebuchet", 15, "bold"),
                                        bg_color="white")
        self.serviceTypeLabel = ctk.CTkLabel(self.addServicesPane, text="Service Type:", text_color="#555555",
                                             font=("Trebuchet", 15, "bold"),
                                             bg_color="white")
        self.ifSuccessfulLabel = ctk.CTkLabel(self.addServicesPane, text="Was Successful:", text_color="#555555",
                                              font=("Trebuchet", 15, "bold"),
                                              bg_color="white")
        self.repairShopLabel = ctk.CTkLabel(self.addServicesPane, text="Repair Shop:", text_color="#555555",
                                            font=("Trebuchet", 15, "bold"),
                                            bg_color="white")

        self.addNewServiceRecordButton = ctk.CTkButton(self.addServicesPane, text="Add new record", fg_color="white",
                                                       font=("Trebuchet", 14, "bold"),
                                                       width=310, height=35, corner_radius=5, hover_color="#dbdbd9",
                                                       bg_color="white", border_width=1, text_color="#555555",
                                                       command=lambda: self.add_new_service_record(crud))

        self.dayTextBox2.place(x=90, y=120)
        self.monthTextBox2.place(x=90, y=220)
        self.yearTextBox2.place(x=90, y=320)
        self.moneyTextBox2.place(x=90, y=420)
        self.serviceTypeTextBox.place(x=490, y=120)
        self.ifSuccessfulTextBox.place(x=490, y=220)
        self.repairShopTextBox.place(x=490, y=320)

        self.dayLabel2.place(x=90, y=90)
        self.monthLabel2.place(x=90, y=190)
        self.yearLabel2.place(x=90, y=290)
        self.moneyLabel2.place(x=90, y=390)
        self.serviceTypeLabel.place(x=490, y=90)
        self.ifSuccessfulLabel.place(x=490, y=190)
        self.repairShopLabel.place(x=490, y=290)

        self.addNewServiceRecordButton.place(x=290, y=550)

        self.carsPane = ctk.CTkFrame(self.mainPane, width=600, height=300, corner_radius=15,
                                     fg_color="white",
                                     bg_color="#e3e7e6")

        self.carsHeaderLabel = ctk.CTkLabel(self.carsPane, text="Choose your car", width=600,
                                            fg_color="white", text_color="#00a05e",
                                            font=("Century Gothic", 22, "bold"), justify=CENTER)
        self.carsHeaderLabel.place(x=0, y=40)

        self.carMakeLabel = ctk.CTkLabel(self.carsPane, text="Make:", text_color="#555555",
                                         font=("Trebuchet", 14, "bold"),
                                         bg_color="white")
        self.carMakeLabel.place(x=50, y=90)

        self.carMakeComboBox = ctk.CTkComboBox(self.carsPane, width=150, height=30, corner_radius=5, fg_color="#dbfde7",
                                               bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                               border_width=0, button_color="#878787",
                                               # values=self.api_callback("makes", "", "", "", ""),
                                               dropdown_fg_color="#878787", dropdown_font=("Trebuchet", 12, "bold"),
                                               command=self.makeComboBox_callback)
        self.carMakeComboBox.place(x=50, y=120)

        self.carTypeLabel = ctk.CTkLabel(self.carsPane, text="Body type:", text_color="#555555",
                                         font=("Trebuchet", 14, "bold"),
                                         bg_color="white")
        self.carTypeLabel.place(x=50, y=190)

        self.carTypeComboBox = ctk.CTkComboBox(self.carsPane, width=150, height=30, corner_radius=5, fg_color="#dbfde7",
                                               bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                               border_width=0, button_color="#878787",
                                               # values=self.api_callback("types", "", "", "", ""),
                                               dropdown_fg_color="#878787", dropdown_font=("Trebuchet", 12, "bold"),
                                               command=self.typeComboBox_callback)
        self.carTypeComboBox.place(x=50, y=220)

        self.carModelLabel = ctk.CTkLabel(self.carsPane, text="Model:", text_color="#555555",
                                          font=("Trebuchet", 14, "bold"),
                                          bg_color="white")
        self.carModelLabel.place(x=250, y=90)

        self.carModelComboBox = ctk.CTkComboBox(self.carsPane, width=150, height=30, corner_radius=5,
                                                fg_color="#dbfde7",
                                                bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                                border_width=0, button_color="#878787",
                                                # values=self.api_callback("models", self.carMakeComboBox.get(),
                                                #                          self.carTypeComboBox.get(), "", ""),
                                                dropdown_fg_color="#878787", dropdown_font=("Trebuchet", 12, "bold"),
                                                command=self.modelComboBox_callback)
        self.carModelComboBox.place(x=250, y=120)

        self.carYearLabel = ctk.CTkLabel(self.carsPane, text="Year:", text_color="#555555",
                                         font=("Trebuchet", 14, "bold"),
                                         bg_color="white")
        self.carYearLabel.place(x=250, y=190)

        self.carYearComboBox = ctk.CTkComboBox(self.carsPane, width=150, height=30, corner_radius=5,
                                               fg_color="#dbfde7",
                                               bg_color="white", text_color="#555555", font=("Trebuchet", 12, "bold"),
                                               border_width=0, button_color="#878787",
                                               # values=self.api_callback("years", self.carMakeComboBox.get(),
                                               #                          self.carTypeComboBox.get(),
                                               #                          self.carModelComboBox.get(), ""),
                                               dropdown_fg_color="#878787", dropdown_font=("Trebuchet", 12, "bold"))
        self.carYearComboBox.place(x=250, y=220)

        self.addCar = ctk.CTkButton(self.carsPane, text="Save your\nchoice", fg_color="#146734",
                                    font=("Trebuchet", 14, "bold"),
                                    width=120, height=50, corner_radius=5, hover_color="#12552d", bg_color="white",
                                    command=lambda: self.add_car_callback(crud))
        self.addCar.place(x=440, y=160)

        self.nearbyPane = ctk.CTkFrame(self.mainPane, width=700, height=550, corner_radius=15,
                                     fg_color="white",
                                     bg_color="#e3e7e6")

        self.nearbyHeaderLabel = ctk.CTkLabel(self.nearbyPane, text="Nearby locations", width=700,
                                            fg_color="white", text_color="#00a05e",
                                            font=("Century Gothic", 20, "bold"), justify=CENTER)
        self.nearbyHeaderLabel.place(x=0, y=10)

        self.map_widget = TkinterMapView(self.nearbyPane, width=700, height=500, corner_radius=0)
        self.map_widget.place(x=0,y=50)

        # google normal tile server
        self.map_widget.set_tile_server("https://tile.openstreetmap.org/{z}/{x}/{y}.png",max_zoom=17)

        g = geocoder.ip('me')
        marker_1 =self.map_widget.set_position(g.latlng[0],g.latlng[1],marker=True)
        marker_1.set_text("Your approx. location")
        self.map_widget.set_zoom(17)

        self.logoutPane = ctk.CTkFrame(self.mainPane, width=400, height=200, corner_radius=15,
                                       fg_color="white",
                                       bg_color="#e3e7e6")

        self.logoutHeaderLabel = ctk.CTkLabel(self.logoutPane, text="Are you sure you want to logout?", width=400,
                                              fg_color="white", text_color="#00a05e",
                                              font=("Century Gothic", 20, "bold"), justify=CENTER)
        self.logoutHeaderLabel.place(x=5, y=40)

        self.logoutButton = ctk.CTkButton(self.logoutPane, text="Yes", fg_color="#146734",
                                          font=("Trebuchet", 14, "bold"),
                                          width=80, height=40, corner_radius=5, hover_color="#12552d", bg_color="white",
                                          cursor="hand2", command=lambda: self.logout_callback(login_window))
        self.logoutButton.place(x=160, y=115)

        self.mainPane.bind("<Map>", lambda event, crud=crud: self.accountInfoUpdate(crud))

        # self.scanReceiptImage()

    def add_car_callback(self, crud):

        if self.carMakeComboBox.get() != "" and self.carTypeComboBox.get() != "" and self.carModelComboBox.get() != "" and self.carYearComboBox.get() != "":
            crud.create_car_data(self.login_app.accountLogin, self.carMakeComboBox.get(), self.carTypeComboBox.get(),
                                 self.carModelComboBox.get(), self.carYearComboBox.get())
            self.carNameLabel.configure(text=self.carMakeComboBox.get() + " " + self.carModelComboBox.get())

    def makeComboBox_callback(self, choice):
        models = self.api_callback("models", choice, self.carTypeComboBox.get(), "", "")
        self.carModelComboBox.configure(values=models)
        if models:
            self.carModelComboBox.set(models[0])
        else:
            self.carModelComboBox.set("")

        self.modelComboBox_callback("")

    def typeComboBox_callback(self, choice):
        models = self.api_callback("models", self.carMakeComboBox.get(), choice, "", "")
        self.carModelComboBox.configure(values=models)
        if models:
            self.carModelComboBox.set(models[0])
        else:
            self.carModelComboBox.set("")

        self.modelComboBox_callback("")

    def modelComboBox_callback(self, choice):
        years = self.api_callback("years", self.carMakeComboBox.get(), self.carTypeComboBox.get(),
                                  self.carModelComboBox.get(), "")
        self.carYearComboBox.configure(values=years)
        if years:
            self.carYearComboBox.set(years[0])
        else:
            self.carYearComboBox.set("")

    def api_callback(self, desired_data, make, type, model, year):
        self.master.after(1000)
        url = ""
        querystring = None

        headers = {
            "X-RapidAPI-Key": "0d60092979msh78b87b91e9028b8p198953jsn379580c215bb",
            "X-RapidAPI-Host": "car-data.p.rapidapi.com"
        }

        if desired_data == "makes":
            url = "https://car-data.p.rapidapi.com/cars/makes"
            response = requests.get(url, headers=headers, params=querystring)
            return sorted(response.json())
        elif desired_data == "types":
            url = "https://car-data.p.rapidapi.com/cars/types"
            response = requests.get(url, headers=headers, params=querystring)
            return sorted(response.json())
        elif desired_data == "models":
            url = "https://car-data.p.rapidapi.com/cars"
            querystring = {"limit": "50", "page": "0", "make": make, "type": type}
            response = requests.get(url, headers=headers, params=querystring)
            models = set(car['model'] for car in response.json())
            return sorted(models)
        elif desired_data == "years":
            url = "https://car-data.p.rapidapi.com/cars"
            querystring = {"limit": "50", "page": "0", "make": make, "type": type, "model": model}
            response = requests.get(url, headers=headers, params=querystring)
            years = set(str(car['year']) for car in response.json())
            return sorted(years)
        elif desired_data == "car":
            url = "https://car-data.p.rapidapi.com/cars"
            querystring = {"limit": "50", "page": "0", "make": make, "type": type, "model": model, "year": year}
            response = requests.get(url, headers=headers, params=querystring)
            return response.json()

        return

    def logout_callback(self, login_window):
        self.selectedTabIndicator.place(x=4, y=148)
        self.master.after(1, self.dash_button_callback_effect)
        self.hideLogoutComponents()
        self.master.withdraw()
        self.login_app.accountLogin = ""
        self.login_app.loginTextBox.delete('1.0', END)
        self.login_app.passwordTextBox.delete(0, END)
        login_window.deiconify()

    def scanReceiptImage(self):
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
        result = pytesseract.image_to_string(blurred, lang="pol", config=custom_config)

        pattern_dot = re.compile(r'PLN[^\d]*(\d+\.\d{2})')
        pattern_comma = re.compile(r'PLN[^\d]*(\d+,[^\d]\d{2})')

        match_dot = re.search(pattern_dot, result)
        match_comma = re.search(pattern_comma, result)

        print(result)

        if match_dot:
            spent_on_fuel_dot = float(match_dot.group(1))
            print(f'Kwota wydana na paliwo (kropka): {spent_on_fuel_dot} PLN')

        elif match_comma:
            spent_on_fuel_comma = float(match_comma.group(1).replace(',', '.').replace(' ', ''))
            print(f'Kwota wydana na paliwo (przecinek): {spent_on_fuel_comma} PLN')

        else:
            print('Nie znaleziono informacji o kwocie wydanej na paliwo.')

    def add_new_fuel_record(self, crud):
        accountLogin = self.login_app.accountLogin
        year = self.yearTextBox.get("0.0", 'end-1c')
        month = self.monthTextBox.get("0.0", 'end-1c')
        day = self.dayTextBox.get("0.0", 'end-1c')
        money = self.moneyTextBox.get("0.0", 'end-1c')
        liters = self.litersTextBox.get("0.0", 'end-1c')
        fueltype = self.fueltypeTextBox.get("0.0", 'end-1c')
        station = self.stationTextBox.get("0.0", 'end-1c')
        crud.createFuelRecord(self.login_app.accountLogin, year, month, day, money, liters, fueltype, station)
        self.loadFuelRecords(crud)
        self.make_plot(crud, accountLogin)
        self.nrOfRefuelingsLabel.configure(text=str(len(self.fuelRecordPanes)))

    def add_new_service_record(self, crud):
        accountLogin = self.login_app.accountLogin
        year = self.yearTextBox2.get("0.0", 'end-1c')
        month = self.monthTextBox2.get("0.0", 'end-1c')
        day = self.dayTextBox2.get("0.0", 'end-1c')
        money = self.moneyTextBox2.get("0.0", 'end-1c')
        serviceType = self.serviceTypeTextBox.get("0.0", 'end-1c')
        ifSuccessful = self.ifSuccessfulTextBox.get("0.0", 'end-1c')
        repairShop = self.repairShopTextBox.get("0.0", 'end-1c')
        crud.createServiceRecord(self.login_app.accountLogin, year, month, day, money, serviceType, ifSuccessful,
                                 repairShop)
        self.loadServicesRecords(crud)
        self.make_plot(crud, accountLogin)
        self.nrOfServicesLabel.configure(text=str(len(self.serviceRecordPanes)))

    def add_fuel_record_callback(self, event):
        self.addFuelPane.place(x=20, y=60)
        self.fuelListPane.place_forget()

    def add_fuel_record_back_callback(self, crud):
        self.fuelListPane.place(x=20, y=60)
        self.addFuelPane.place_forget()

    def add_service_record_callback(self, event):
        self.addServicesPane.place(x=20, y=60)
        self.servicesListPane.place_forget()

    def add_service_record_back_callback(self, crud):
        self.servicesListPane.place(x=20, y=60)
        self.addServicesPane.place_forget()

    def calendar_click_callback(self, crud):
        selected_date_str = self.cal.get_date()
        selected_date = datetime.strptime(selected_date_str, "%m/%d/%y")

        day = str(selected_date.day)
        if len(day) == 1:
            day = "0" + day
        month = str(selected_date.month)
        if len(month) == 1:
            month = "0" + month
        year = str(selected_date.year)

        self.dateLabel.configure(text=day + "." + month + "." + year)
        self.dateLabel.update()

        self.refuelingsNumberOnDateLabel.configure(
            text=str(crud.read_nr_of_fuel_records(self.login_app.accountLogin, day, month, year)) + "x")
        self.servicesNumberOnDateLabel.configure(
            text=str(crud.read_nr_of_service_records(self.login_app.accountLogin, day, month, year)) + "x")

    def dash_button_callback(self, event):
        if self.leftPane.cget("width") == 70:
            self.selectedTabIndicator.place(x=4, y=148)
            self.master.after(1, self.dash_button_callback_effect)
            self.hideLogoutComponents()

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
            elif whichButtonPressed == 3:
                self.showServicesComponents()
            elif whichButtonPressed == 4:
                self.showCarsComponents()
            elif whichButtonPressed == 5:
                self.showNearbyComponents()
            self.showAccountInfoComponents()
            self.leftPane.update()

    def acc_button_callback(self, event):
        if self.leftPane.cget("width") == 70:
            self.selectedTabIndicator.place(x=4, y=248)
            self.hideLogoutComponents()
        if self.leftPane.cget("width") == 270:
            self.selectedTabIndicator.place(x=4, y=248)
            self.hideAccountInfoComponents()
            self.hideOverviewComponents()
            self.hideFuelComponents()
            self.hideServicesComponents()
            self.hideCarsComponents()
            self.hideNearbyComponents()
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
            self.hideLogoutComponents()
        if self.leftPane.cget("width") == 270:
            self.selectedTabIndicator.place(x=4, y=348)
            self.hideAccountInfoComponents()
            self.hideOverviewComponents()
            self.hideFuelComponents()
            self.hideServicesComponents()
            self.hideCarsComponents()
            self.hideNearbyComponents()
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
            self.showLogoutComponents()
        if self.leftPane.cget("width") == 270:
            self.selectedTabIndicator.place(x=4, y=448)
            self.hideAccountInfoComponents()
            self.hideOverviewComponents()
            self.hideFuelComponents()
            self.hideServicesComponents()
            self.hideCarsComponents()
            self.hideNearbyComponents()
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
            self.showLogoutComponents()

    def make_plot(self, crud, accountLogin):
        month_data, money_data = crud.read_money_spent(accountLogin)
        current_date = datetime.now()
        months = [
            'January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December'
        ]

        last_seven_months = []

        for i in range(6, -1, -1):
            current_month = current_date - timedelta(days=current_date.day)
            current_month = current_month.replace(month=current_date.month - i)

            last_seven_months.append(months[current_month.month - 1])

        data = {'Month': last_seven_months,
                '[zł] spent': [0] * 7
                }

        for month, money in zip(month_data, money_data):
            month_name = months[int(month) - 1]
            index = last_seven_months.index(month_name)
            data['[zł] spent'][index] += money

        df = pd.DataFrame(data)

        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        figure1.subplots_adjust(bottom=0.4)
        ax1 = figure1.add_subplot(111)
        ax1.tick_params(axis='x', labelsize=8)
        bar1 = FigureCanvasTkAgg(figure1, self.plotPane)
        bar1.get_tk_widget().place(x=0, y=0)
        df.plot(kind='bar', x='Month', y='[zł] spent', legend=True, ax=ax1, color="#085f3d")
        ax1.set_xticklabels(last_seven_months, rotation=0)
        ax1.set_title('Money spent in recent months')

    def accountInfoUpdate(self, crud):
        accountLogin = self.login_app.accountLogin
        self.loadCarData(crud, accountLogin)
        self.make_plot(crud, accountLogin)
        self.accountInfo.configure(text=accountLogin)
        self.loadFuelRecords(crud)
        self.nrOfRefuelingsLabel.configure(text=str(len(self.fuelRecordPanes)))
        self.loadServicesRecords(crud)
        self.nrOfServicesLabel.configure(text=str(len(self.serviceRecordPanes)))
        self.accountInfo.update()
        self.nrOfRefuelingsLabel.update()
        self.nrOfServicesLabel.update()
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
        self.hideServicesComponents()
        self.hideCarsComponents()
        self.hideNearbyComponents()

    def fuel_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 2
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.showFuelComponents()
        self.hideOverviewComponents()
        self.hideServicesComponents()
        self.hideCarsComponents()
        self.hideNearbyComponents()

    def services_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 3
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.showServicesComponents()
        self.hideOverviewComponents()
        self.hideFuelComponents()
        self.hideCarsComponents()
        self.hideNearbyComponents()

    def cars_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 4
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.nearbyButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.showCarsComponents()
        self.hideOverviewComponents()
        self.hideFuelComponents()
        self.hideServicesComponents()
        self.hideNearbyComponents()

    def nearby_button_callback(self, event):
        global whichButtonPressed
        whichButtonPressed = 5
        self.overviewButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.fuelButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.servicesButton.configure(text_color="#e3e7e6", fg_color="#00a05e")
        self.carsButton.configure(text_color="#e3e7e6", fg_color="#00a05e")

        self.showNearbyComponents()
        self.hideOverviewComponents()
        self.hideFuelComponents()
        self.hideServicesComponents()
        self.hideCarsComponents()

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
        self.addFuelButtonPane.place(x=860, y=630)
        self.fuelListPane.place(x=20, y=60)

    def hideFuelComponents(self):
        self.fuelListPane.place_forget()
        self.addFuelButtonPane.place_forget()
        self.addFuelPane.place_forget()

    def showServicesComponents(self):
        self.addServicesButtonPane.place(x=860, y=630)
        self.servicesListPane.place(x=20, y=60)

    def hideServicesComponents(self):
        self.servicesListPane.place_forget()
        self.addServicesButtonPane.place_forget()
        self.addServicesPane.place_forget()

    def showCarsComponents(self):
        self.carsPane.place(x=165, y=200)

    def hideCarsComponents(self):
        self.carsPane.place_forget()

    def showNearbyComponents(self):
        self.nearbyPane.place(x=115, y=100)

    def hideNearbyComponents(self):
        self.nearbyPane.place_forget()

    def showAccountInfoComponents(self):
        self.accountInfo.place(x=44, y=18)
        self.accInfoImage.place(x=20, y=13)

    def hideAccountInfoComponents(self):
        self.accInfoImage.place_forget()
        self.accountInfo.place_forget()

    def showLogoutComponents(self):
        self.logoutPane.place(x=365, y=250)

    def hideLogoutComponents(self):
        self.logoutPane.place_forget()

    def loadFuelRecords(self, crud):

        for pane in self.fuelRecordPanes:
            pane.destroy()

        self.fuelRecordPanes.clear()
        self.dateLabels.clear()
        self.infoLabels.clear()

        year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data = crud.read_fuel_records(
            self.login_app.accountLogin)

        if not year_data:
            return

        fuel_records = list(zip(year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data))

        fuel_records = [(int(record[0]), int(record[1]), int(record[2]), record[3], record[4], record[5], record[6]) for
                        record in fuel_records]

        fuel_records = [
            (record[0], f"{int(record[1]):02d}", f"{int(record[2]):02d}", record[3], record[4], record[5], record[6])
            for record in fuel_records]

        sorted_records = sorted(fuel_records, key=lambda x: (x[0], x[1], x[2]), reverse=True)

        year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data = zip(*sorted_records)

        i = 0
        j = 0

        for record in year_data:
            self.fuelRecordPanes.append(
                ctk.CTkFrame(self.fuelListPane, width=750, height=100, corner_radius=5, fg_color="#e3e7e6",
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

    def loadServicesRecords(self, crud):

        for pane in self.serviceRecordPanes:
            pane.destroy()

        self.serviceRecordPanes.clear()
        self.dateLabels2.clear()
        self.infoLabels2.clear()
        self.successfulLabels.clear()

        year_data, month_data, day_data, money_data, serviceType_data, ifSuccessful_data, repairShop_data = crud.read_services_records(
            self.login_app.accountLogin)

        if not year_data:
            return

        service_records = list(
            zip(year_data, month_data, day_data, money_data, serviceType_data, ifSuccessful_data, repairShop_data))

        service_records = [(int(record[0]), int(record[1]), int(record[2]), record[3], record[4], record[5], record[6])
                           for
                           record in service_records]

        service_records = [
            (record[0], f"{int(record[1]):02d}", f"{int(record[2]):02d}", record[3], record[4], record[5], record[6])
            for record in service_records]

        sorted_records = sorted(service_records, key=lambda x: (x[0], x[1], x[2]), reverse=True)

        year_data, month_data, day_data, money_data, serviceType_data, ifSuccessful_data, repairShop_data = zip(
            *sorted_records)

        i = 0
        j = 0

        for record in year_data:
            self.serviceRecordPanes.append(
                ctk.CTkFrame(self.servicesListPane, width=750, height=100, corner_radius=5, fg_color="#e3e7e6",
                             bg_color="white"))
            self.dateLabels2.append(
                ctk.CTkLabel(self.serviceRecordPanes[i],
                             text=str(day_data[i]) + "." + str(month_data[i]) + "." + str(year_data[i]),
                             fg_color="#e3e7e6",
                             text_color="#00a05e", font=("Century Gothic", 17, "bold")))
            self.infoLabels2.append(
                ctk.CTkLabel(self.serviceRecordPanes[i],
                             text=str(money_data[i]) + "zł spent on " + str(serviceType_data[i]) + " service" +
                                  " at " + str(repairShop_data[i]) + " repair shop.",
                             fg_color="#e3e7e6",
                             text_color="#555555", font=("Century Gothic", 18, "bold")))
            self.successfulLabels.append(
                ctk.CTkLabel(self.serviceRecordPanes[i],
                             text="Was this service successful?: " + str(ifSuccessful_data[i]),
                             fg_color="#e3e7e6",
                             text_color="#00a05e", font=("Century Gothic", 17, "bold")))
            i = i + 1

        for pane in self.serviceRecordPanes:
            pane.grid(row=j + 1, column=0, pady=15, padx=25)
            self.dateLabels2[j].place(x=20, y=15)
            self.infoLabels2[j].place(x=20, y=50)
            self.successfulLabels[j].place(x=430, y=15)
            j = j + 1

    def loadCarData(self, crud, accountLogin):
        make, type, model, year = crud.read_car_data(accountLogin)
        if make and model:
            self.carNameLabel.configure(text=make + " " + model)
            self.carMakeComboBox.set(make)
            self.carTypeComboBox.set(type)
            self.carModelComboBox.set(model)
            self.carYearComboBox.set(year)
        else:
            self.carNameLabel.configure(text="Car not added!")
            self.carMakeComboBox.set("")
            self.carTypeComboBox.set("")
            self.carModelComboBox.set("")
            self.carYearComboBox.set("")
