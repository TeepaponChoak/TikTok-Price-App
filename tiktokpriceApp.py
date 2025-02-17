import customtkinter as ctk
import csv
import tkinter as tk
from tkinter import ttk

def calculate():
    tiktok_charge = 0.06
    payment_charge = 0.02
    commission = 0.02

    List = entry_list.get()
    sell_price = float(entry_sell_price.get())
    cost_price = float(entry_cost_price.get())

    result_tc = sell_price - (sell_price * tiktok_charge)
    result_pc = result_tc - (result_tc * payment_charge)
    result_com = sell_price * commission
    result_profit = result_pc - result_com - cost_price
    result_profit_percent = (result_profit / cost_price) * 100

    file_exists = False
    try:
        with open("tiktok_price.csv", "r", encoding="utf-8") as file:
            file_exists = True
    except FileNotFoundError:
        pass

    with open("tiktok_price.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["List", "Sell Price", "Cost Price", "COM Tiktok", "COM Payment", "Commission", "Profit", "Profit%"])
        writer.writerow([List, f'{sell_price:.2f}', f'{cost_price:.2f}', f'{result_tc:.2f}', f'{result_pc:.2f}', f'{result_com:.2f}', f'{result_profit:.2f}', f'{result_profit_percent:.2f}'])

    result_label.configure(text="ค่าธรรมเนียม TikTok : " + str(f'{result_tc:.2f}') + " บาท\n"
                           "ค่าธรรมเนียมชำระเงิน : " + str(f'{result_pc:.2f}') + " บาท\n"
                           "คอมฯจ่าย : " + str(f'{result_com:.2f}') + " บาท\n"
                           "กำไร : " + str(f'{result_profit:.2f}') + " บาท\n"
                           "กำไร% : " + str(f'{result_profit_percent:.2f}') + "%")
    load_csv_data()

def load_csv_data():
    for row in tree.get_children():
        tree.delete(row)
    try:
        with open("tiktok_price.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                tree.insert("", "end", values=row)
    except FileNotFoundError:
        pass

def check_entries(*args):
    if entry_list.get() and entry_sell_price.get() and entry_cost_price.get():
        button_result.configure(state="normal")
    else:
        button_result.configure(state="disabled")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("TikTok Price Cal App")
app.geometry("800x600")

entry_list = ctk.CTkEntry(app, placeholder_text="รายการสินค้า", width=150,height=30)
entry_list.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

entry_sell_price = ctk.CTkEntry(app, placeholder_text="ราคาขาย", width=150,height=30)
entry_sell_price.place(relx=0.5, rely=0.17, anchor=ctk.CENTER)

entry_cost_price = ctk.CTkEntry(app, placeholder_text="ราคาต้นทุน", width=150,height=30)
entry_cost_price.place(relx=0.5, rely=0.24, anchor=ctk.CENTER)

button_result = ctk.CTkButton(app, text="Calculate", width=100, height=50, font=("Arial", 20), command=calculate, fg_color="#E50914", hover_color="#B20710")
button_result.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

result_label = ctk.CTkLabel(app, text="Result will show here", font=("FC SaveSpace Rounded", 26))
result_label.place(relx=0.5, rely=0.43, anchor=ctk.N)

title_label = ctk.CTkLabel(app, text="TikTok Price Calculator", font=("FC SaveSpace Rounded", 40))
title_label.pack(pady = 10)

frame = tk.Frame(app, width=800, height=300)
frame.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

tree = ttk.Treeview(frame, columns=("List", "Sell Price", "Cost Price", "COM Tiktok", "COM Payment", "Commission", "Profit", "Profit%"),  show="headings")
column_widths = {"List": 100, "Sell Price": 100, "Cost Price": 100, "COM Tiktok": 100, "COM Payment": 100, "Commission": 100, "Profit": 100, "Profit%": 100}
for col in ("List", "Sell Price", "Cost Price", "COM Tiktok", "COM Payment", "Commission", "Profit", "Profit%"):
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=column_widths[col])

tree.pack(fill="both", expand=True)

load_csv_data()

entry_list.bind("<KeyRelease>", check_entries)
entry_sell_price.bind("<KeyRelease>", check_entries)
entry_cost_price.bind("<KeyRelease>", check_entries)

app.mainloop()