import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from details import details_section

class mainPage:
        def __init__(self, root):
                    self.root = root
                    self.root.title("ACCOUNT OPENING SYSTEM")
                    self.root.geometry("650x500")
                    self.root.resizable(False, False)
                    self.root.configure(bg="#e6f2ff")

                    def open_main():
                            bank_name=bank_dropdown.get()

                            if not all ([bank_name]):
                                    messagebox.showerror("Validation Error", "Pleaase choose your bank name")
                                    return
                        
                            details_section()
                    

                    img = ImageTk.PhotoImage(Image.open('images/img.png').resize((360,260 )))
                    Bimage = tk.Label(self.root, image=img,bg="#e6f2ff")
                    Bimage.image = img
                    Bimage.place(x=155, y=30)
                    #Choose bank label
                    ChooseBnkLabel=tk.Label(self.root,text="Choose Bank",
                                            width=15,
                                            height=2,
                                            bg="#caeffa")
                    ChooseBnkLabel.place(x=200,y=310)
                    #choose bank entry
                    BnkOptions=["Bank Of Baroda","Indian Bank","SBI"]
                    bank_dropdown=ttk.Combobox(root,values=BnkOptions,state="readonly",width=15)
                    bank_dropdown.pack()
                    bank_dropdown.place(x=340,y=318)
                    # bank_dropdown.set("Select bank")
                    #Account open btn
                    AcOpen_button = tk.Button(self.root, text='OPEN A/C',
                                font=('Courier New', 10),
                                width=15,
                                height=2,
                                relief="flat",
                                bg="green",
                                fg="white",
                                command=open_main)
                    AcOpen_button.place(x=165, y=380)
                    

                    #Exit btn
                    exit_button = tk.Button(self.root, text='EXIT',
                                font=('Courier New', 10),
                                width=15,
                                height=2,
                                relief="flat",
                                command=self.root.destroy,
                                bg="red",
                                fg="white",
                                activebackground="#caeffa")
                    exit_button.place(x=370, y=380)

if __name__ == "__main__":
    root = tk.Tk()
    app = mainPage(root)
root.mainloop()