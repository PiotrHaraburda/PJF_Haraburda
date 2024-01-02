import tkinter as tk
import customtkinter as ctk
import scripts.LoginWindow
import scripts.RegisterWindow
import scripts.FirebaseCRUD
import scripts.MainWindow
import scripts.LoadingWindow
from PIL import Image

login_window = ctk.CTk()
loading_window = ctk.CTkToplevel()
register_window = ctk.CTkToplevel()
main_window = ctk.CTkToplevel()

login_window.withdraw()
loading_window.withdraw()
register_window.withdraw()
main_window.withdraw()

mainImage = ctk.CTkImage(light_image=Image.open("images/mainImg.png"), size=(45, 45))
mainImage2 = ctk.CTkImage(light_image=Image.open("images/mainImg2.png"), size=(45, 45))
accountInfoImage = ctk.CTkImage(light_image=Image.open("images/accountInfo.png"), size=(20, 20))

dashboardImage = ctk.CTkImage(light_image=Image.open("images/dashboard.png"), size=(35, 35))
accountImage = ctk.CTkImage(light_image=Image.open("images/account.png"), size=(35, 35))
creditsImage = ctk.CTkImage(light_image=Image.open("images/credits.png"), size=(35, 35))
logoutImage = ctk.CTkImage(light_image=Image.open("images/logout.png"), size=(35, 35))
fuelImage = ctk.CTkImage(light_image=Image.open("images/fuel.png"), size=(45, 45))
serviceImage = ctk.CTkImage(light_image=Image.open("images/service.png"), size=(45, 45))
carImage = ctk.CTkImage(light_image=Image.open("images/car.png"), size=(100, 100))
plusImage = ctk.CTkImage(light_image=Image.open("images/plus.png"), size=(48, 48))
backImage = ctk.CTkImage(light_image=Image.open("images/back.png"), size=(35, 35))
backgroundImage = ctk.CTkImage(light_image=Image.open("images/background.png"), size=(1130, 700))
showImage = ctk.CTkImage(light_image=Image.open("images/show.png"), size=(20, 20))
hideImage = ctk.CTkImage(light_image=Image.open("images/hide.png"), size=(20, 20))

receiptImage = Image.open("images/receipt.jpg")

crud = scripts.FirebaseCRUD.FirebaseCRUD()

login_app = scripts.LoginWindow.LoginWindow(login_window, register_window, loading_window, mainImage, crud)
loading_app = scripts.LoadingWindow.LoadingWindow(loading_window, login_app, main_window, mainImage, crud)
register_app = scripts.RegisterWindow.RegisterWindow(register_window, login_window, mainImage, crud)
main_app = scripts.MainWindow.MainWindow(main_window, login_app, login_window, backgroundImage, mainImage2,
                                         accountInfoImage,
                                         dashboardImage, accountImage, creditsImage, logoutImage, fuelImage,
                                         serviceImage, carImage, plusImage, backImage,hideImage,showImage, receiptImage, crud)


def main():
    login_window.geometry("400x540")
    login_window.title("MileageMate Login Page")
    login_window._set_appearance_mode("light")
    w = 400
    h = 540
    ws = login_window.winfo_screenwidth()
    hs = login_window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    login_window.geometry('+%d+%d' % (x, y))
    login_window.config(background="white")
    login_window.resizable(False, False)

    loading_window.title("")
    loading_window._set_appearance_mode("light")
    loading_window.config(background="white")
    loading_window.resizable(False, False)

    register_window.geometry("600x540")
    register_window.title("MileageMate Register Page")
    register_window._set_appearance_mode("light")
    w = 600
    h = 540
    ws = register_window.winfo_screenwidth()
    hs = register_window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    register_window.geometry('+%d+%d' % (x, y))
    register_window.config(background="white")
    register_window.resizable(False, False)

    main_window.geometry("1200x700")
    main_window.title("MileageMate")
    main_window._set_appearance_mode("light")
    w = 1200
    h = 700
    ws = main_window.winfo_screenwidth()
    hs = main_window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    main_window.geometry('+%d+%d' % (x, y))
    main_window.config(background="white")
    main_window.resizable(False, False)

    login_window.protocol("WM_DELETE_WINDOW", on_closing)
    register_window.protocol("WM_DELETE_WINDOW", on_closing)
    main_window.protocol("WM_DELETE_WINDOW", on_closing)
    loading_window.protocol("WM_DELETE_WINDOW", on_closing)
    login_window.deiconify()
    login_window.update()
    loading_window.update()
    register_window.update()
    main_window.update()
    tk.mainloop()


def on_closing():
    exit()


if __name__ == '__main__':
    main()
