import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from db import *
from charts import pie_chart, bar_chart
from auth import login

# ================= UI =================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("💰 Expense Tracker ULTRA PRO")
app.geometry("800x700")

CATEGORY = ["Food","Travel","Shopping","Bills","Education","Health","Other"]

# ================= LOGIN =================
def login_screen():
    win = ctk.CTkToplevel(app)
    win.title("Login")
    win.geometry("300x300")

    user = ctk.CTkEntry(win, placeholder_text="Username")
    user.pack(pady=10)

    pwd = ctk.CTkEntry(win, placeholder_text="Password", show="*")
    pwd.pack(pady=10)

    def do_login():
        if login(user.get(), pwd.get()):
            messagebox.showinfo("Success", "Logged in")
            win.destroy()
        else:
            messagebox.showerror("Error", "Invalid")

    ctk.CTkButton(win, text="Login", command=do_login).pack(pady=10)

# ================= FUNCTIONS =================
def add():
    date = datetime.now().strftime("%Y-%m-%d")

    add_expense((
        date,
        type_var.get(),
        cat_var.get(),
        float(amount.get()),
        desc.get()
    ))

    messagebox.showinfo("Done", "Added!")

def show_all():
    win = ctk.CTkToplevel(app)
    win.geometry("700x400")

    text = ctk.CTkTextbox(win)
    text.pack(fill="both", expand=True)

    for row in fetch_all():
        text.insert("end", str(row) + "\n")

def report():
    data = summary()

    income = 0
    expense = 0

    for t, amt in data:
        if t == "Income":
            income = amt
        else:
            expense = amt

    messagebox.showinfo(
        "Report",
        f"Income: ₹{income}\nExpense: ₹{expense}\nBalance: ₹{income-expense}"
    )

def search_data():
    win = ctk.CTkToplevel(app)
    win.geometry("500x400")

    text = ctk.CTkTextbox(win)
    text.pack(fill="both", expand=True)

    for row in search(search_entry.get()):
        text.insert("end", str(row)+"\n")

# ================= UI =================
ctk.CTkLabel(app, text="💰 ULTRA PRO EXPENSE TRACKER", font=("Arial", 22)).pack(pady=20)

type_var = ctk.StringVar(value="Expense")
cat_var = ctk.StringVar(value="Food")

ctk.CTkOptionMenu(app, values=["Income","Expense"], variable=type_var).pack(pady=5)
ctk.CTkOptionMenu(app, values=CATEGORY, variable=cat_var).pack(pady=5)

amount = ctk.CTkEntry(app, placeholder_text="Amount")
amount.pack(pady=5)

desc = ctk.CTkEntry(app, placeholder_text="Description")
desc.pack(pady=5)

ctk.CTkButton(app, text="➕ Add", command=add).pack(pady=5)
ctk.CTkButton(app, text="📄 View All", command=show_all).pack(pady=5)
ctk.CTkButton(app, text="📊 Report", command=report).pack(pady=5)
ctk.CTkButton(app, text="🥧 Pie Chart", command=pie_chart).pack(pady=5)
ctk.CTkButton(app, text="📊 Bar Chart", command=bar_chart).pack(pady=5)
ctk.CTkButton(app, text="🔐 Login", command=login_screen).pack(pady=5)

# SEARCH
search_entry = ctk.CTkEntry(app, placeholder_text="Search Category")
search_entry.pack(pady=5)

ctk.CTkButton(app, text="🔍 Search", command=search_data).pack(pady=5)

ctk.CTkButton(app, text="❌ Exit", command=app.destroy).pack(pady=10)

app.mainloop()