from tkinter import *

primary_color = "#053246"


class Qrgernerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry('900x500+200+100')
        self.root.title("Qr Generator|Developed By Gourab karmakar")
        self.root.resizable(False, False)
        text = Label(self.root, text="   Qr code Generator for Skfund Members", font=("times new roman", 30),
                     fg='White', bg='#053246', anchor='w').place(x=0, y=0, relwidth=1)

        # ========= Employee window ============
        emp_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        emp_frame.place(x=40, y=90, width=500, height=390)

        emp_title = Label(emp_frame, text="Member Deatils", font=("goudy old style", 20), bg='#053246', fg='white', )
        emp_title.place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(emp_frame, text="Member Id", font=("times new roman", 15, 'bold'), bg='white')
        lbl_emp_code.place(x=25, y=60)

        lbl_emp_fname = Label(emp_frame, text="First Name", font=("times new roman", 15, 'bold'), bg='white')
        lbl_emp_fname.place(x=25, y=100)

        lbl_emp_lname = Label(emp_frame, text="Last Name", font=("times new roman", 15, 'bold'), bg='white')
        lbl_emp_lname.place(x=25, y=140)

        lbl_emp_mno = Label(emp_frame, text="Mobile No", font=("times new roman", 15, 'bold'), bg='white')
        lbl_emp_mno.place(x=25, y=180)

        lbl_emp_ano = Label(emp_frame, text="Aadhar No", font=("times new roman", 15, 'bold'), bg='white')
        lbl_emp_ano.place(x=25, y=220)

        # =================== Entry ==========================

        self.var_emp_code = StringVar()
        self.var_emp_fname = StringVar()
        self.var_emp_lname = StringVar()
        self.var_emp_mno = StringVar()
        self.var_emp_ano = StringVar()

        ent_emp_code = Entry(emp_frame, font=("times new roman", 15, 'bold'), bg='lightyellow',
                             textvar=self.var_emp_code)
        ent_emp_code.place(x=185, y=60)

        ent_emp_fname = Entry(emp_frame, font=("times new roman", 15, 'bold'), bg='lightyellow',
                              textvar=self.var_emp_fname)
        ent_emp_fname.place(x=185, y=100)

        ent_emp_lname = Entry(emp_frame, font=("times new roman", 15, 'bold'), bg='lightyellow',
                              textvar=self.var_emp_lname)
        ent_emp_lname.place(x=185, y=140)

        ent_emp_mno = Entry(emp_frame, font=("times new roman", 15, 'bold'), bg='lightyellow', textvar=self.var_emp_mno)
        ent_emp_mno.place(x=185, y=180)

        ent_emp_ano = Entry(emp_frame, font=("times new roman", 15, 'bold'), bg='lightyellow', textvar=self.var_emp_ano)
        ent_emp_ano.place(x=185, y=220)

        # ========= Button ===========

        btn_save = Button(emp_frame, text="Save", bg="#497e1e", fg="white", font=("times new roman", 15, 'bold'),
                          command=self.generate)
        btn_save.place(x=25, y=270, width=90, height=40)

        btn_clear = Button(emp_frame, text="Clear", bg="#497e1e", fg="white", font=("times new roman", 15, 'bold'))
        btn_clear.place(x=125, y=270, width=90, height=40)

        btn_edit = Button(emp_frame, text="Edit", bg="#497e1e", fg="white", font=("times new roman", 15, 'bold'))
        btn_edit.place(x=225, y=270, width=90, height=40)

        # =========== show qr =========

        qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_frame.place(x=560, y=90, width=300, height=390)

        qr_title = Label(qr_frame, text="Qr Show", font=("goudy old style", 20), bg=primary_color, fg="white")
        qr_title.place(x=0, y=0, relwidth=1)

        self.qr_frame = Label(qr_frame, text="No qr Available", font=('times new roman', 15), bg='#bd3333', fg="white")
        self.qr_frame.place(x=60, y=100, width=180, height=180)

    def generate(self):
        if self.var_emp_code.get() == '' or self.var_emp_fname.get() == "" or self.var_emp_lname.get() == "" or self.var_emp_ano.get() or self.var_emp_mno.get() == "":
            # self.label_massage.config = ""
            pass
        else:
            print()


root = Tk()
obj = Qrgernerator(root)
root.mainloop()
