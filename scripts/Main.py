import tkinter as tk
import customtkinter as ctk
import scripts.LoginWindow
import scripts.RegisterWindow
import scripts.FirebaseCRUD
import scripts.MainWindow
from PIL import Image

root = ctk.CTk()
root2 = ctk.CTkToplevel()
root3 = ctk.CTkToplevel()

root.withdraw()
root2.withdraw()
root3.withdraw()

mainImage = ctk.CTkImage(light_image=Image.open("images/mainImg.png"), size=(45, 45))
mainImage2 = ctk.CTkImage(light_image=Image.open("images/mainImg2.png"), size=(45, 45))
accountInfoImage = ctk.CTkImage(light_image=Image.open("images/accountInfo.png"), size=(20, 20))

dashboardImage = ctk.CTkImage(light_image=Image.open("images/dashboard.png"), size=(35, 35))
accountImage = ctk.CTkImage(light_image=Image.open("images/account.png"), size=(35, 35))
settingsImage = ctk.CTkImage(light_image=Image.open("images/settings.png"), size=(35, 35))
logoutImage = ctk.CTkImage(light_image=Image.open("images/logout.png"), size=(35, 35))
fuelImage = ctk.CTkImage(light_image=Image.open("images/fuel.png"), size=(45, 45))
serviceImage = ctk.CTkImage(light_image=Image.open("images/service.png"), size=(45, 45))
carImage = ctk.CTkImage(light_image=Image.open("images/car.png"), size=(100, 100))
plusImage = ctk.CTkImage(light_image=Image.open("images/plus.png"), size=(48, 48))
backImage = ctk.CTkImage(light_image=Image.open("images/back.png"), size=(35, 35))

receiptImage = Image.open("images/receipt.jpg")

crud = scripts.FirebaseCRUD.FirebaseCRUD()

app = scripts.LoginWindow.LoginWindow(root, root2, root3, mainImage, crud)
app2 = scripts.RegisterWindow.RegisterWindow(root2, root, mainImage, crud)
app3 = scripts.MainWindow.MainWindow(root3, app, mainImage2, accountInfoImage,dashboardImage,accountImage,settingsImage,logoutImage,fuelImage,serviceImage,carImage,plusImage,backImage,receiptImage,crud)


def main():
    root.geometry("400x540")
    root.title("MileageMate Login Page")
    root._set_appearance_mode("light")
    w = 400
    h = 540
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('+%d+%d' % (x, y))
    root.config(background="white")
    root.resizable(False, False)

    root2.geometry("600x540")
    root2.title("MileageMate Register Page")
    root2._set_appearance_mode("light")
    w = 600
    h = 540
    ws = root2.winfo_screenwidth()
    hs = root2.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root2.geometry('+%d+%d' % (x, y))
    root2.config(background="white")
    root2.resizable(False, False)

    root3.geometry("1200x700")
    root3.title("MileageMate")
    root3._set_appearance_mode("light")
    w = 1200
    h = 700
    ws = root3.winfo_screenwidth()
    hs = root3.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root3.geometry('+%d+%d' % (x, y))
    root3.config(background="white")
    root3.resizable(False, False)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root2.protocol("WM_DELETE_WINDOW", on_closing)
    root3.protocol("WM_DELETE_WINDOW", on_closing)
    root.deiconify()
    root.update()
    root2.update()
    root3.update()
    tk.mainloop()


def on_closing():
    exit()


if __name__ == '__main__':
    main()
