import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import Toplevel, Label, Button, PhotoImage
from submitted import open_success_window
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bank"
)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS bank_accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        account_type VARCHAR(255),
        name VARCHAR(255),
        dob VARCHAR(255),
        nominee VARCHAR(255),
        mobile VARCHAR(20),
        email VARCHAR(255),
        address TEXT
    )
""")
# print("Table created successfully.")
conn.close()


def details_section():
    root=tk.Toplevel()
    root.geometry("660x550")
    root.title("Bank opening system")
    root.resizable(False, False)
    
    
    # functions
    # button funstionality
    def create_account_action():
        """
        Validates all form fields. If complete, it shows a success message 
        and clears the form. Otherwise, it shows an error.
        """
        # --- 1. Get data from all fields ---
        account_type = combo.get()
        name = entry_2.get()
        dob=entry_dob.get()
        nominee = entry_3.get()
        mobile = entry_4.get()
        email = entry_5.get()
        address = entry_6.get()
        terms_status = check.get() # Gets the value "1" or "2" from the radio button
    
        # --- 2. Validation ---
        # Check if any text field is empty
        if not all([account_type, name, dob, nominee, mobile, email, address]):
            messagebox.showerror("Validation Error", "All fields are required.")
            return

        if terms_status != "1":
            messagebox.showerror("Validation Error", "You must agree to Terms & Conditions.")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="bank"
            )
            cursor = conn.cursor()
            query = """
                INSERT INTO bank_accounts (account_type, name, dob, nominee, mobile, email, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (account_type, name, dob, nominee, mobile, email, address)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
    
            messagebox.showinfo("Success", "Account Created Success fully.")
            open_success_window()
    
            # Clear fields
            combo.set('')
            entry_2.delete(0, tk.END)
            entry_dob.delete(0, tk.END)
            entry_3.delete(0, tk.END)
            entry_4.delete(0, tk.END)
            entry_5.delete(0, tk.END)
            entry_6.delete(0, tk.END)
            check.set(None)

        except mysql.connector.Error as e:
             messagebox.showerror("Database Error", f"Failed to insert data: {e}")
    
    
    def save_info_action():
        """Shows a confirmation message that the info is saved."""
        messagebox.showinfo("Info Saved", "Your information has been saved. Please complete the form and click 'Create Account'.")
    
    # Integer-only validation function
    def only_numbers(char):
        return char.isdigit()
    
    vcmd = root.register(only_numbers)
    
    # mainsection
    
    # for entry
    style = ttk.Style()
    style.configure("TEntry", padding="10 10 10 10")
    style.configure("TCombobox", padding="10 10 10 10", font=("Arial", 12))
    
    # heading
    heading = tk.Label(root, text="Bank Account Opening Form", font=("Helvetica", 20, "bold"))
    heading.pack(pady=10)
    
    # account type
    label_1=tk.Label(root,text="A/C Type",font=("Helvetica",15,"bold"))
    label_1.place(x=20,y=70)
    combo= ttk.Combobox(root, values=["General Account", "Savings Account", "Zero Balance Account"],width=70,height=30, style="TCombobox")
    combo.place(x=180,y=67)
    
    # nameinput
    label_2=tk.Label(root,text="Name",font=("Helvetica",15,"bold"))
    label_2.place(x=20,y=120)
    entry_2=ttk.Entry(root,width=73, style="TEntry")
    entry_2.place(x=180,y=117)
    
    # DOB
    label_dob=tk.Label(root,text="DOB",font=("Helvetica",15,"bold"))
    label_dob.place(x=20,y=170)
    entry_dob=ttk.Entry(root,width=73, style="TEntry")
    entry_dob.place(x=180,y=167)
    
    # nominee
    label_3=tk.Label(root,text="Nominee name",font=("Helvetica",15,"bold"))
    label_3.place(x=20,y=220)
    entry_3=ttk.Entry(root,width=73, style="TEntry")
    entry_3.place(x=180,y=217)
    
    # Mo.no
    label_4=tk.Label(root,text="Mobile no",font=("Helvetica",15,"bold"))
    label_4.place(x=20,y=270)
    entry_4=ttk.Entry(root,width=73, style="TEntry", validate="key", validatecommand=(vcmd, "%S"))
    entry_4.place(x=180,y=267)
    
    # email
    label_5=tk.Label(root,text="E-mail",font=("Helvetica",15,"bold"))
    label_5.place(x=20,y=320)
    entry_5=ttk.Entry(root,width=73, style="TEntry")
    entry_5.place(x=180,y=317)
    
    # address
    label_6=tk.Label(root,text="Address",font=("Helvetica",15,"bold"))
    label_6.place(x=20,y=370)
    entry_6= ttk.Entry(root, style="TEntry", width=73,)
    entry_6.place(x=180,y=367)
    
    # Agree terms & conditions
    check=tk.StringVar()
    radiobutton_1=tk.Radiobutton(root,text="Agree Terms & Conditions",variable=check,value=1,font=("Helvetica",10,"bold"))
    radiobutton_1.place(x=20,y=430)
    radiobutton_2=tk.Radiobutton(root,text="Not Agree",variable=check,value=2,font=("Arial",10,"bold"))
    radiobutton_2.place(x=20,y=455)
    
    button_1=tk.Button(root,text="Create account",width=14,height=2,bg="red",fg="white",command=create_account_action)
    button_1.place(x=220,y=490)
    button_2=tk.Button(root,text="save info",command=save_info_action,width=14,height=2,bg="Green")
    button_2.place(x=340,y=490)

    def go_back():
        if messagebox.askyesno("Confirm", "Are you sure you want to go back? All unsaved data will be lost."):
            root.destroy()  # Close the Toplevel window and return to main window

    button_3 = tk.Button(root, text="Back", width=10, height=1, bg="green", fg="white", command=go_back)
    button_3.place(x=20, y=15)


