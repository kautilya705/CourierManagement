from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Dashboard:
    def __init__(self, root):

        self.root = root
        # Title to indicate the three buttons.
        self.root.title("Dashboard Page")
        self.root.withdraw()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 3
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 5
        self.root.geometry("590x424+%d+%d" % (x, y))
        self.root.resizable(False, False)

        # Frame
        self.txt_frame = Frame(
            self.root, bd=4, relief=RIDGE)
        self.txt_frame.place(x=0, y=0, width=790, height=425)

        # Frame for Buttons
        self.btn_frame = Frame(
            self.txt_frame, bd=2, relief=RIDGE)
        self.btn_frame.place(x=60, y=43, width=466, height=330)

        # Input
        self.input_btn = Button(self.btn_frame, text='Courier Inputs', width=40, height=3, bd=2, relief=FLAT, bg="#fc5c01", fg="black",
                                font=("roboto sans-serif", 13, "bold"), command=self.input_view)
        self.input_btn.grid(row=1, column=5, pady=28, padx=23)

        # View
        self.view_btn = Button(self.btn_frame, text='Courier details changes', width=40, height=3, bd=2, relief=FLAT, bg="#fc5c01", fg="black",
                               font=("roboto sans-serif", 13, "bold"), command=self.view_page)
        self.view_btn.grid(row=2, column=5)

        # Close
        self.close_btn = Button(self.btn_frame, text='Exit from the software', width=40, height=3, bd=2, relief=FLAT, bg="#fc5c01", fg="black",
                                font=("roboto sans-serif", 13, "bold"), command=self.close_page)
        self.close_btn.grid(row=3, column=5, pady=28, padx=23)

    def input_view(self):

        top = Toplevel()
        top.title("Courier Management System")

        x = (top.winfo_screenwidth() - top.winfo_reqwidth()) / 4
        y = (top.winfo_screenheight() - top.winfo_reqheight()) / 5
        top.geometry("790x424+%d+%d" % (x, y))
        top.resizable(False, False)

        def add_item():

            if Name.get() == '' or Number.get() == '' or FlatNum.get() == '' or Date.get() == '':
                messagebox.showerror(
                    'Required Fields', 'Please include all fields')
                return
            else:
                con = pymysql.connect(
                    host="localhost", database1="root", password="hello1234", database="register")
                cur = con.cursor()

                cur.execute(
                    "insert into database2 (Name ,Number, FlatNum, Date) values(%s,%s,%s,%s)",
                    (Name.get(),
                     Number.get(),
                     FlatNum.get(),
                     Date.get()
                     ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Adding Items Successfuly")
                clear_text()

        def clear_text():
            top.Name_entry.delete(0, END)
            top.Number_entry.delete(0, END)
            top.FlatNum_entry.delete(0, END)
            top.Date_entry.delete(0, END)

        # Head Label
        top.lbl_title = Label(
            top, text="Courier Management System", bd=4, fg="white", relief=RIDGE,  bg="black", font=("roboto sans-serif", 23), pady=7)
        top.lbl_title.pack(side=TOP, fill=X)

        # Frame
        top.txt_frame = Frame(
            top, bd=4, relief=RIDGE, bg="black")
        top.txt_frame.place(x=0, y=55, width=790, height=370)
        # Space
        top.Name_label = Label(top.txt_frame, text='',
                               font=('', 14), pady=10, padx=10, bg="black", fg="white").grid(row=0, column=0, sticky=W)
        # Name
        Name = StringVar()
        top.Name_label = Label(top.txt_frame, text='Recipient name :',
                               font=('bold', 14), pady=10, padx=14, bg="black", fg="white").grid(row=1, column=0, sticky=W)
        top.Name_entry = Entry(
            top.txt_frame, textvariable=Name, width=25, bd=3, font=("bold", 11))
        top.Name_entry.grid(row=1, column=1)
        # Number
        Number = StringVar()
        top.Number_label = Label(top.txt_frame, text='Phone Number :', font=(
            'bold', 14), padx=10, bg="black", fg="white").grid(row=1, column=2, sticky=W)
        top.Number_entry = Entry(top.txt_frame, textvariable=Number,
                                   width=25, bd=3, font=("bold", 11))
        top.Number_entry.grid(row=1, column=3)
        # FlatNum
        FlatNum = StringVar()
        top.FlatNum_label = Label(top.txt_frame, text='Flat Number:', font=(
            'bold', 14), padx=12, bg="black", fg="white").grid(row=2, column=0, sticky=W)
        top.FlatNum_entry = Entry(top.txt_frame, textvariable=FlatNum,
                                   width=25, bd=3, font=("bold", 11))
        top.FlatNum_entry.grid(row=2, column=1)

        # Date
        Date = IntVar()
        top.Date_label = Label(top.txt_frame, text='Date of  checkout :', font=('bold', 14),
                                padx=10, bg="black", fg="white").grid(row=2, column=2, sticky=W)
        top.Date_entry = Entry(top.txt_frame, textvariable=Date,
                                width=25, bd=3, font=("bold", 11))
        top.Date_entry.grid(row=2, column=3)

        # Frame for Buttons
        top.btn_frame = Frame(
            top.txt_frame, bd=2, relief=RIDGE, bg="black")
        top.btn_frame.place(x=0, y=252, width=781, height=110)

        top.add_btn = Button(top.btn_frame, text='Add', width=20, height=2, bd=2, relief=FLAT, bg="black", fg="black",
                             font=("roboto sans-serif", 12, "bold"), command=add_item)
        top.add_btn.grid(row=1, column=2, pady=26)

        top.delete_btn = Button(top.btn_frame, text='Clear', width=20, height=2, bg="#fc5c01", fg="black", bd=2, relief=FLAT,
                                font=("roboto sans-serif", 12, "bold"), command=clear_text)
        top.delete_btn.grid(row=1, column=6, padx=26)

        top.deiconify()
        top.mainloop()

    def view_page(self):
        top = Toplevel()
        top.title("Courier Management System")
        x = (top.winfo_screenwidth() -
             top.winfo_reqwidth()) / 10
        y = (top.winfo_screenheight() - top.winfo_reqheight()) / 30
        top.geometry("1130x665+%d+%d" % (x, y))
        top.resizable(False, False)

        def populate_data():

            con = pymysql.connect(
                host="localhost", database1="root", password="", database="register")
            cur = con.cursor()

            cur.execute("select * from database2")
            rows = cur.fetchall()

            if len(rows) != 0:
                top.data_list.delete(*top.data_list.get_children())
                for row in rows:
                    top.data_list.insert('', END, values=row)
                con.commit()
            con.close()

        def clear_text():
            top.id_entry.delete(0, END)
            top.Name_entry.delete(0, END)
            top.Number_entry.delete(0, END)
            top.FlatNum_entry.delete(0, END)
            top.Date_entry.delete(0, END)

        def update_item():
            con = pymysql.connect(
                host="localhost", database1="root", password="", database="register")
            cur = con.cursor()
            cur.execute(
                "update database2 set id=%s, Name=%s, Number=%s, FlatNum=%s, Date=%s",
                (id_text.get(),
                 Name_text.get(),
                 Number_text.get(),
                 FlatNum_text.get(),
                 Date_text.get(),
                 id_text.get()
                 ))
            con.commit()
            messagebox.showinfo("Success", "Update Successfuly")
            populate_data()
            clear_text()
            con.close()

        def delete_item():
            con = pymysql.connect(
                host="localhost", database1="root", password="hello1234", database2="register")
            cur = con.cursor()
            cur.execute("delete from database2 where id=%s", id_text.get()) #id to find the data packet

            dlt = messagebox.askyesno(
                'Gadgets', 'Do you want to delete this file ')

            clear_text() #functions being called. Colour indicates that
            con.commit()

            if dlt > 0:
                clear_text()
                populate_data()

            con.close()

        def select_item(ev):

            cursor_row = top.data_list.focus()
            contents = top.data_list.item(cursor_row)
            row = contents['values']
            id_text.set(row[0])
            Name_text.set(row[1])
            Number_text.set(row[2])
            FlatNum_text.set(row[3])
            Date_text.set(row[4])


        def clear():
            top.id_entry.delete(0, END)
            top.Name_entry.delete(0, END)
            top.Number_entry.delete(0, END)
            top.FlatNum_entry.delete(0, END)
            top.Date_entry.delete(0, END)

        def close():
            ext = messagebox.askyesno(
                'Database', 'Do you want to this window? ')

            if ext > 0:
                top.destroy()

        # Head Label
        top.lbl_title = Label(
            top, text="Courier Checkout", bd=4, fg="white", relief=RIDGE,  bg="black", font=("roboto sans-serif", 23), pady=7)
        top.lbl_title.pack(side=TOP, fill=X)

        # Frame Table
        top.detail_frame = Frame(
            top, bd=4, relief=RIDGE, bg="black")
        top.detail_frame.place(x=0, y=390, width=1130, height=276)

        # Frame Input
        top.txt_frame = Frame(
            top, bd=4, relief=RIDGE, bg="black")
        top.txt_frame.place(x=0, y=55, width=1130, height=340)

        # Buttons Frame
        top.btn_frame = Frame(
            top.detail_frame, bd=3, relief=RIDGE, bg="black")
        top.btn_frame.place(x=0, y=170, width=1122, height=98)

        # Button Here
        # Space for Buttons
        top.space_label = Label(top.btn_frame, text='',
                                font=('', 10), bg="black", fg="white").grid(row=1, column=2, pady=20, padx=5)
        # Edit
        top.edit_btn = Button(top.btn_frame, text='Change', width=24, height=2, bd=2, relief=FLAT, bg="#fc5c01", fg="black",
                              font=("roboto sans-serif", 13, "bold"), command=update_item)
        top.edit_btn.grid(row=1, column=3, pady=20, padx=10)

        # Delete
        top.delete_btn = Button(top.btn_frame, text='Delete', width=24, height=2, bd=2, relief=FLAT, bg="#fc5c01", fg="black",
                                font=("roboto sans-serif", 13, "bold"), command=delete_item)
        top.delete_btn.grid(row=1, column=4, pady=20, padx=10)

        # Back
        top.bck_btn = Button(top.btn_frame, text='Clear', width=24, height=2, bg="#fc5c01", fg="black", bd=2, relief=FLAT,
                             font=("roboto sans-serif", 13, "bold"), command=clear)
        top.bck_btn.grid(row=1, column=5, padx=12)

        # Exit
        top.exit_btn = Button(top.btn_frame, text='Exit', width=24, height=2, bg="#fc5c01", fg="black", bd=2, relief=FLAT,
                              font=("roboto sans-serif", 13, "bold"), command=close)
        top.exit_btn.grid(row=1, column=6, padx=12)

        # Space
        top.space_label = Label(top.txt_frame, text='',
                                font=('', 10), bg="black", fg="white").grid(row=0, column=2, pady=10, sticky=W, padx=43)
        # ID
        id_text = StringVar()
        top.id_label = Label(top.txt_frame, text='List Number :',
                             font=('bold', 14), bg="black", fg="white").grid(row=1, column=0, sticky=W, padx=55)
        top.id_entry = Entry(
            top.txt_frame, textvariable=id_text, width=25, bd=3, font=("bold", 15))
        top.id_entry.grid(row=1, column=1)

        # Name
        Name_text = StringVar()
        top.Name_label = Label(top.txt_frame, text='Recipient name :',
                               font=('bold', 14), bg="black", fg="white").grid(row=2, column=0, sticky=W, padx=52)
        top.Name_entry = Entry(
            top.txt_frame, textvariable=Name_text, width=25, bd=3, font=("bold", 15))
        top.Name_entry.grid(row=2, column=1)

        # Number
        Number_text = StringVar()
        top.Number_label = Label(top.txt_frame, text='Phone Number :', font=(
            'bold', 14), bg="black", fg="white").grid(row=1, column=2, sticky=W, padx=50)
        top.Number_entry = Entry(top.txt_frame, textvariable=Number_text,
                                   width=25, bd=3, font=("bold", 15))
        top.Number_entry.grid(row=1, column=3)

        # FlatNum
        FlatNum_text = StringVar()
        top.FlatNum_label = Label(top.txt_frame, text='Flat Number:', font=(
            'bold', 14), bg="black", fg="white").grid(row=3, column=0, sticky=W, padx=50)
        top.FlatNum_entry = Entry(top.txt_frame, textvariable=FlatNum_text,
                                   width=25, bd=3, font=("bold", 15))
        top.FlatNum_entry.grid(row=3, column=1)

        # Date
        Date_text = StringVar()
        top.Date_label = Label(top.txt_frame, text='Date of  checkout :', font=('bold', 14),
                                bg="black", fg="white").grid(row=2, column=2, sticky=W, padx=50, pady=20)
        top.Date_entry = Entry(top.txt_frame, textvariable=Date_text,
                                width=25, bd=3, font=("bold", 15))
        top.Date_entry.grid(row=2, column=3)

        # Listbox Frame
        top.list_frame = Frame(
            top.detail_frame, bd=2, relief=RIDGE, bg="black")
        top.list_frame.place(x=0, y=0, width=1122, height=170)

        # Treeview Scrollbar
        scroll_x = Scrollbar(top.list_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(top.list_frame, orient=VERTICAL)

        # Treeview
        top.data_list = ttk.Treeview(top.list_frame, height=12, columns=(
            "list", "Name", "Number", "FlatNum", "Date"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        top.data_list.configure(yscrollcommand=scroll_x.set)
        scroll_x.configure(command=top.data_list.xview)

        top.data_list.configure(yscrollcommand=scroll_y.set)
        scroll_y.configure(command=top.data_list.yview)

        top.data_list.heading("list", text="List No.")
        top.data_list.heading("Name", text="Recipient name")
        top.data_list.heading("Number", text="Phone Number")
        top.data_list.heading("FlatNum", text="Flat Number")
        top.data_list.heading("Date", text="Date")

        top.data_list['show'] = 'headings'

        top.data_list.column("list", width=30)
        top.data_list.column("Name", width=160)
        top.data_list.column("Number", width=146)
        top.data_list.column("FlatNum", width=140)
        top.data_list.column("Date", width=66)

        top.data_list.pack(fill=BOTH, expand=1)

        top.data_list.bind('<ButtonRelease-1>', select_item)

        # To show all Data in Treeview
        populate_data()

    def close_page(self):
        ext = messagebox.askyesno(
            'Dashboard', 'Do you want to this window ')

        if ext > 0:
            self.root.destroy()


root = Tk()
obj = Dashboard(root) #Memory realeasing and closing the program. 
root.deiconify()
root.mainloop()
