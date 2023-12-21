import tkinter
from tkinter import *
import customtkinter as ctk
import PIL.Image


ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("MileageMate")
root.geometry("1200x700")

def leftPaneEnter():
    button.configure(state="disabled")
    if leftPane.cget("width")==100:
        for i in range(leftPane.cget("width"), 300, 10):
            headersPane.place(x=headersPane.winfo_x()+5, y=25)
            leftPane.update()
            leftPane.configure(True, width=i+10)
            mainPane.place(x=mainPane.winfo_x()+10, y=75)
            mainPane.update()
            mainPane.configure(True, width=mainPane.winfo_width()-5)
        mainImageLabel.place_forget()
        mainLabel.place(anchor=N, relx=0.5, rely=0.05)
    else:
        mainLabel.place_forget()
        mainImageLabel.place(anchor=N, relx=0.5, rely=0.02)
        for i in range(leftPane.cget("width"), 100, -10):
            headersPane.place(x=headersPane.winfo_x()-5, y=25)
            leftPane.update()
            leftPane.configure(True, width=i-10)
    button.configure(state="normal")


body = ctk.CTkFrame(root, width=1200, height=700, fg_color="#0d0f1c", corner_radius=10)
body.pack()

leftPane = ctk.CTkFrame(body, width=100, height=680, fg_color="#F0ECE5", corner_radius=10)
leftPane.place(x=10, y=10)

button = ctk.CTkButton(leftPane, text="Open", fg_color="#7F7B82", hover_color="#444554",
                        font=("Helvetica", 13, "bold"),cursor="hand2",command=leftPaneEnter,width=50)
button.place(anchor=N, relx=0.5, rely=0.95)

mainLabel = ctk.CTkLabel(leftPane, text="MileageMate", font=("Helvetica", 22, "bold"),text_color="#1D1D1D")

mainImage = ctk.CTkImage(light_image=PIL.Image.open("mainImg.png"), size=(36, 36))
mainImageLabel = ctk.CTkLabel(leftPane, text="", image=mainImage)
mainImageLabel.place(anchor=N, relx=0.5, rely=0.02)

headersPane = ctk.CTkFrame(body, width=850, height=75, fg_color="#0d0f1c", corner_radius=10)
headersPane.place(x=260, y=25)

mainPane = ctk.CTkFrame(body, width=950, height=615, fg_color="#B6BBC4", corner_radius=10)
mainPane.place(x=175, y=75)

button1 = ctk.CTkButton(headersPane, text="Overview", fg_color="#31304D", hover_color="#444554",
                        font=("Helvetica", 13, "bold"),cursor="hand2")
button2 = ctk.CTkButton(headersPane, text="Fuel", fg_color="#31304D", hover_color="#444554",
                        font=("Helvetica", 13, "bold"),cursor="hand2")
button3 = ctk.CTkButton(headersPane, text="Services", fg_color="#31304D", hover_color="#444554",
                        font=("Helvetica", 13, "bold"),cursor="hand2")
button4 = ctk.CTkButton(headersPane, text="Cars", fg_color="#31304D", hover_color="#444554",
                        font=("Helvetica", 13, "bold"),cursor="hand2")
button5 = ctk.CTkButton(headersPane, text="Nearby", fg_color="#31304D", hover_color="#444554",
                        font=("Helvetica", 13, "bold"),cursor="hand2")


button1.grid(row=0, column=0, padx=10)
button2.grid(row=0, column=1, padx=10)
button3.grid(row=0, column=2, padx=10)
button4.grid(row=0, column=3, padx=10)
button5.grid(row=0, column=4, padx=10)


root.mainloop()
