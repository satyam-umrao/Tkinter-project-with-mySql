import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bank"
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS deposit_money (
        id INT AUTO_INCREMENT PRIMARY KEY,
        account_number VARCHAR(50),
        amount DECIMAL(10, 0),
        deposited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# print("Table 'deposit_money' created.")
conn.close()

def open_success_window():
    def deposit_action():
        account = entry_8.get()
        amount = entry_9.get()
    
        if not all([account, amount]):
            messagebox.showerror("Validation Error", "All fields are required. Please fill out the entire form.")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
            database="bank"
        )
            cursor = conn.cursor()
            query = "INSERT INTO deposit_money (account_number, amount) VALUES (%s, %s)"
            cursor.execute(query, (account, amount))
            conn.commit()
            conn.close()

            messagebox.showinfo("Deposit", "Amount Deposited successfully")

            entry_8.delete(0, tk.END)
            entry_9.delete(0, tk.END)

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to deposit: {e}")
      
    def exit_action():
        root.destroy()
    
    # Create window
    root = tk.Toplevel()
    root.title("Bank UI")
    root.geometry("500x390")
    root.resizable(False, False)

    # Integer-only validation function
    def only_numbers(char):
        return char.isdigit()
    
    vcmd = root.register(only_numbers)

    
    style = ttk.Style()
    style.configure("TEntry", padding="10 10 10 10")
    
    # Load and resize image to 50x50
    img = Image.open("images/tick.png")  # Replace with your image file
    img = img.resize((100, 100))
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=photo)
    img_label.image = photo  # Prevent garbage collection
    img_label.pack(pady=20)
    
    label_7=tk.Label(root,text="Account Opened Successfully",font=("Helvetica",15,"bold"))
    label_7.pack()
    
    label_8=tk.Label(root,text="Enter A/C No.",font=("Helvetica",15,"bold"))
    label_8.place(x=20,y=200)
    entry_8=ttk.Entry(root,width=45, style="TEntry",validate="key", validatecommand=(vcmd, "%S"))
    entry_8.place(x=180,y=197)
    
    
    label_9=tk.Label(root,text="Enter Amount",font=("Helvetica",15,"bold"))
    label_9.place(x=20,y=250)
    entry_9=ttk.Entry(root,width=45, style="TEntry", validate="key", validatecommand=(vcmd, "%S"))
    entry_9.place(x=180,y=247)
    # Buttons
    deposit_btn = tk.Button(root, text="Deposit", width=15, bg="green", fg="white", command=deposit_action)
    deposit_btn.place(x=120,y=330)
    
    exit_btn = tk.Button(root, text="Exit", width=15, bg="red", fg="white", command=exit_action)
    exit_btn.place(x=250,y=330)
    
    root.mainloop()
    