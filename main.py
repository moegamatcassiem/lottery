from tkinter import *
from tkinter import messagebox
import multiprocessing
from playsound import playsound
# from PIL import ImageTk,Image
import rsaidnumber
from datetime import datetime, timedelta
from email_validator import validate_email, EmailNotValidError



root = Tk()
root.geometry("500x500")
root.title("Log in")
root.config(bg="yellow")

# sound
# p = multiprocessing.Process(target=playsound, args=('mario.mp3',))

canvas = Canvas(root, width=300, height=185, bg="black")
canvas.place(x=100, y=20)
img =PhotoImage(file="Lottery_1_70.png")
canvas.create_image(20, 20, anchor=NW, image=img)

class validate:
    def __init__(self, master):
        self.name_lab = Label(master, text="Enter full name", bg="yellow", font="bold")
        self.name_lab.place(x=10, y=220)
        self.name_ent = Entry(master)
        self.name_ent.place(x=200, y=220)

        self.email_lab = Label(master, text="Enter email", bg="yellow", font="bold")
        self.email_lab.place(x=10, y=270)
        self.email_ent = Entry(master)
        self.email_ent.place(x=200, y=270)

        self.address_lab = Label(master, text="Enter address", bg="yellow", font="bold")
        self.address_lab.place(x=10, y=320)
        self.address_ent = Entry(master)
        self.address_ent.place(x=200, y=320)

        self.id_lab = Label(master, text="Enter identity number", bg="yellow", font="bold")
        self.id_lab.place(x=10, y=370)
        self.id_ent = Entry(master)
        self.id_ent.place(x=200, y=370)

        self.submit_btn = Button(master, text="Submit", bg="yellow", border="5", command=self.submit)
        self.submit_btn.place(x=200, y=410)

    def submit(self):
        self.info = ""
        self.txt_file = open("Text.txt", 'a')
        self.info += self.name_ent.get()
        self.info += '\n'
        self.info += self.email_ent.get()
        self.info += '\n'
        self.info += self.address_ent.get()
        self.info += '\n'
        self.info += self.id_ent.get()
        self.txt_file.write(self.info)

        self.id_number = rsaidnumber.parse(self.id_ent.get())
        self.years_old = ((datetime.today() - self.id_number.date_of_birth) // timedelta(365.25))
        if  self.years_old >= 18:
            messagebox.showinfo("APPROVED", "LETS PLAY!!")

        else:
            gap = 18 - self.years_old
            messagebox.showerror("Return in", str(gap) + "years")
        try:
            valid = validate_email(self.email_ent.get())
            self.email = valid.email
        except EmailNotValidError:
            messagebox.showerror("Invalid Email")
            root.destroy()
            import screen2


app=validate(root)

root.mainloop()