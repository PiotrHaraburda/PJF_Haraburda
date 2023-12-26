import tkinter as tk
import customtkinter as ctk
import package.LoginWindow
import package.RegisterWindow
import package.FirebaseCRUD
from PIL import Image

root = ctk.CTk()
root2 = ctk.CTkToplevel()

root.withdraw()
root2.withdraw()

mainImage = ctk.CTkImage(light_image=Image.open("package/mainImg.png"), size=(45, 45))
crud = package.FirebaseCRUD.FirebaseCRUD()

app = package.LoginWindow.LoginWindow(root, root2, mainImage, crud)
app2 = package.RegisterWindow.RegisterWindow(root2, root, mainImage, crud)


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

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root2.protocol("WM_DELETE_WINDOW", on_closing)
    root.deiconify()
    root.update()
    root2.update()
    tk.mainloop()


def on_closing():
    exit()


if __name__ == '__main__':
    main()
