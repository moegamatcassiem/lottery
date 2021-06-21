from tkinter import *
import random
from tkinter import messagebox
import multiprocessing
from playsound import playsound
# from PIL import ImageTk,Image.


root = Tk()
root.geometry("500x900")
root.title("Lottery")
root.config(bg="yellow")
n = StringVar()
n2 = StringVar()
n3 = StringVar()
n4 = StringVar()


canvas = Canvas(root, width=345, height=168, bg="black")
canvas.place(x=80, y=10)
img =PhotoImage(file="Lottery_1_70.png")
canvas.create_image(40, 20, anchor=NW, image=img)

# # sound feature
p = multiprocessing.Process(target=playsound, args=('mario.mp3',))

#sound function
def music():
    p.start()

def stop_music():
    p.terminate()
    root.destroy()

class gen:
    def __init__(self, master):
        self.text = Label(master, text="Choose any six numbers between 1 and 49", bg="yellow", font=5)
        self.text.place(x=80, y=180)

        self.space = Label(master, width=20, bg="white", textvariable=n)
        self.space.place(x=170, y=205)
        self.space2 = Label(master, width=20, bg="white", textvariable=n2)
        self.space2.place(x=170, y=230)
        self.space3 = Label(master, width=20, bg="white", textvariable=n3)
        self.space3.place(x=170, y=255)

        self.num_1 = Button(master, width=2, border="0", bg="black", fg="yellow", text="1", command=lambda: self.select(1))
        self.num_1.place(x=80, y=290)
        self.num_2 = Button(master, width=2, border="0", bg="black", fg="yellow", text="2", command=lambda: self.select(2))
        self.num_2.place(x=130, y=290)
        self.num_3 = Button(master, width=2, border="0", bg="black", fg="yellow", text="3", command=lambda: self.select(3))
        self.num_3.place(x=180, y=290)
        self.num_4 = Button(master, width=2, border="0", bg="black", fg="yellow", text="4", command=lambda: self.select(4))
        self.num_4.place(x=230, y=290)
        self.num_5 = Button(master, width=2, border="0", bg="black", fg="yellow", text="5", command=lambda: self.select(5))
        self.num_5.place(x=280, y=290)
        self.num_6 = Button(master, width=2, border="0", bg="black", fg="yellow", text="6", command=lambda: self.select(6))
        self.num_6.place(x=330, y=290)
        self.num_7 = Button(master, width=2, border="0", bg="black", fg="yellow", text="7", command=lambda: self.select(7))
        self.num_7.place(x=380, y=290)
        self.num_8 = Button(master, width=2, border="0", bg="black", fg="yellow", text="8", command=lambda: self.select(8))
        self.num_8.place(x=80, y=325)
        self.num_9 = Button(master, width=2, border="0", bg="black", fg="yellow", text="9", command=lambda: self.select(9))
        self.num_9.place(x=130, y=325)
        self.num_10 = Button(master, width=2, border="0", bg="black", fg="yellow", text="10", command=lambda: self.select(10))
        self.num_10.place(x=180, y=325)
        self.num_11 = Button(master, width=2, border="0", bg="black", fg="yellow", text="11", command=lambda: self.select(11))
        self.num_11.place(x=230, y=325)
        self.num_12 = Button(master, width=2, border="0", bg="black", fg="yellow", text="12", command=lambda: self.select(12))
        self.num_12.place(x=280, y=325)
        self.num_13 = Button(master, width=2, border="0", bg="black", fg="yellow", text="13", command=lambda: self.select(13))
        self.num_13.place(x=330, y=325)
        self.num_14 = Button(master, width=2, border="0", bg="black", fg="yellow", text="14", command=lambda: self.select(14))
        self.num_14.place(x=380, y=325)
        self.num_15 = Button(master, width=2, border="0", bg="black", fg="yellow", text="15", command=lambda: self.select(15))
        self.num_15.place(x=80, y=360)
        self.num_16 = Button(master, width=2, border="0", bg="black", fg="yellow", text="16", command=lambda: self.select(16))
        self.num_16.place(x=130, y=360)
        self.num_17 = Button(master, width=2, border="0", bg="black", fg="yellow", text="17", command=lambda: self.select(17))
        self.num_17.place(x=180, y=360)
        self.num_18 = Button(master, width=2, border="0", bg="black", fg="yellow", text="18", command=lambda: self.select(18))
        self.num_18.place(x=230, y=360)
        self.num_19 = Button(master, width=2, border="0", bg="black", fg="yellow", text="19", command=lambda: self.select(19))
        self.num_19.place(x=280, y=360)
        self.num_20 = Button(master, width=2, border="0", bg="black", fg="yellow", text="20", command=lambda: self.select(20))
        self.num_20.place(x=330, y=360)
        self.num_21 = Button(master, width=2, border="0", bg="black", fg="yellow", text="21", command=lambda: self.select(21))
        self.num_21.place(x=380, y=360)
        self.num_22 = Button(master, width=2, border="0", bg="black", fg="yellow", text="22", command=lambda: self.select(22))
        self.num_22.place(x=80, y=395)
        self.num_23 = Button(master, width=2, border="0", bg="black", fg="yellow", text="23", command=lambda: self.select(23))
        self.num_23.place(x=130, y=395)
        self.num_24 = Button(master, width=2, border="0", bg="black", fg="yellow", text="24", command=lambda: self.select(24))
        self.num_24.place(x=180, y=395)
        self.num_25 = Button(master, width=2, border="0", bg="black", fg="yellow", text="25", command=lambda: self.select(25))
        self.num_25.place(x=230, y=395)
        self.num_26 = Button(master, width=2, border="0", bg="black", fg="yellow", text="26", command=lambda: self.select(26))
        self.num_26.place(x=280, y=395)
        self.num_27 = Button(master, width=2, border="0", bg="black", fg="yellow", text="27", command=lambda: self.select(27))
        self.num_27.place(x=330, y=395)
        self.num_28 = Button(master, width=2, border="0", bg="black", fg="yellow", text="28", command=lambda: self.select(28))
        self.num_28.place(x=380, y=395)
        self.num_29 = Button(master, width=2, border="0", bg="black", fg="yellow", text="29", command=lambda: self.select(29))
        self.num_29.place(x=80, y=430)
        self.num_30 = Button(master, width=2, border="0", bg="black", fg="yellow", text="30", command=lambda: self.select(30))
        self.num_30.place(x=130, y=430)
        self.num_31 = Button(master, width=2, border="0", bg="black", fg="yellow", text="31", command=lambda: self.select(31))
        self.num_31.place(x=180, y=430)
        self.num_32 = Button(master, width=2, border="0", bg="black", fg="yellow", text="32", command=lambda: self.select(32))
        self.num_32.place(x=230, y=430)
        self.num_33 = Button(master, width=2, border="0", bg="black", fg="yellow", text="33", command=lambda: self.select(33))
        self.num_33.place(x=280, y=430)
        self.num_34 = Button(master, width=2, border="0", bg="black", fg="yellow", text="34", command=lambda: self.select(34))
        self.num_34.place(x=330, y=430)
        self.num_35 = Button(master, width=2, border="0", bg="black", fg="yellow", text="35", command=lambda: self.select(35))
        self.num_35.place(x=380, y=430)
        self.num_36 = Button(master, width=2, border="0", bg="black",  fg="yellow", text="36", command=lambda: self.select(36))
        self.num_36.place(x=80, y=465)
        self.num_37 = Button(master, width=2, border="0", bg="black",  fg="yellow", text="37", command=lambda: self.select(37))
        self.num_37.place(x=130, y=465)
        self.num_38 = Button(master, width=2, border="0", bg="black", fg="yellow", text="38", command=lambda: self.select(38))
        self.num_38.place(x=180, y=465)
        self.num_39 = Button(master, width=2, border="0", bg="black", fg="yellow", text="39", command=lambda: self.select(39))
        self.num_39.place(x=230, y=465)
        self.num_40 = Button(master, width=2, border="0", bg="black", fg="yellow", text="40", command=lambda: self.select(40))
        self.num_40.place(x=280, y=465)
        self.num_41 = Button(master, width=2, border="0", bg="black", fg="yellow", text="41", command=lambda: self.select(41))
        self.num_41.place(x=330, y=465)
        self.num_42 = Button(master, width=2, border="0", bg="black", fg="yellow", text="42", command=lambda: self.select(42))
        self.num_42.place(x=380, y=465)
        self.num_43 = Button(master, width=2, border="0", bg="black", fg="yellow", text="43", command=lambda: self.select(43))
        self.num_43.place(x=80, y=500)
        self.num_44 = Button(master, width=2, border="0", bg="black", fg="yellow", text="44", command=lambda: self.select(44))
        self.num_44.place(x=130, y=500)
        self.num_45 = Button(master, width=2, border="0", bg="black", fg="yellow", text="45", command=lambda: self.select(45))
        self.num_45.place(x=180, y=500)
        self.num_46 = Button(master, width=2, border="0", bg="black", fg="yellow", text="46", command=lambda: self.select(46))
        self.num_46.place(x=230, y=500)
        self.num_47 = Button(master, width=2, border="0", bg="black", fg="yellow", text="47", command=lambda: self.select(47))
        self.num_47.place(x=280, y=500)
        self.num_48 = Button(master, width=2, border="0", bg="black", fg="yellow", text="48", command=lambda: self.select(48))
        self.num_48.place(x=330, y=500)
        self.num_49 = Button(master, width=2, border="0", bg="black", fg="yellow", text="49", command=lambda: self.select(49))
        self.num_49.place(x=380, y=500)

        self.numbers_lab = Label(master, width=20, height=2, font=2, bg="white")
        self.numbers_lab.place(x=160, y=540)

        self.list1 = []
        self.list2 = []
        self.list3 = []

        self.play_btn = Button(master, bg="black",fg="yellow",border="0", width=4, height=2, font=20, text="Play", command=self.play)
        self.play_btn.place(x=355, y=220)

        self.winnings_btn = Button(master, bg="black",fg="yellow",border="0", height=2, font=20, text="Winnings", command=self.winnings)
        self.winnings_btn.place(x=325, y=780)

        self.play_agn_btn = Button(master, bg="black",fg="yellow",border="0", height=2, font=20, text="Play Again", command=self.clear)
        self.play_agn_btn.place(x=80, y=845)

        self.play_agn_btn = Button(master, bg="black", fg="yellow", border="0", height=2, font=20, text="Exit",command=self.exit)
        self.play_agn_btn.place(x=220, y=845)

        self.claim_prize_btn = Button(master, bg="black", fg="yellow", border="0", height=2, font=20, text="Claim Prize",command=self.claim)
        self.claim_prize_btn.place(x=310, y=845)

        self.win_lab = Label(master, width=25, bg="yellow", font=1)
        self.win_lab.place(x=50, y=780)

        self.win_lab2 = Label(master, width=25, bg="yellow", font=1)
        self.win_lab2.place(x=50, y=800)

        self.win_lab3 = Label(master, width=25, bg="yellow", font=1)
        self.win_lab3.place(x=50, y=820)

        self.match_txt = Label(master, text="Matches in 1st set", bg="yellow")
        self.match_txt.place(x=100, y=585)
        self.match_lab = Label(master, border="0", width=15, height=1, font=1)
        self.match_lab.place(x=80, y=610)

        self.match_txt2 = Label(master, text="Matches in 2nd set", bg="yellow")
        self.match_txt2.place(x=100, y=650)
        self.match_lab2 = Label(master, border="0", width=15, height=1, font=1)
        self.match_lab2.place(x=80, y=670)

        self.match_txt3 = Label(master, text="Matches in 3rd set", bg="yellow")
        self.match_txt3.place(x=100, y=710)
        self.match_lab3 = Label(master, border="0", width=15, height=1, font=1)
        self.match_lab3.place(x=80, y=730)

        self.set1_txt = Label(master, text="Your 1st set", bg="yellow")
        self.set1_txt.place(x=300, y=585)
        self.set1 = Label(master, width=15, height=1, font=1)
        self.set1.place(x=270, y=610)

        self.set2_txt = Label(master, text="Your 2nd set", bg="yellow")
        self.set2_txt.place(x=300, y=650)
        self.set2 = Label(master, width=15, height=1, font=1)
        self.set2.place(x=270, y=670)

        self.set3_txt = Label(master, text="Your 3rd set", bg="yellow")
        self.set3_txt.place(x=300, y=710)
        self.set3 = Label(master, width=15, height=1, font=1)
        self.set3.place(x=270, y=730)

    def select(self, value):
        if len(self.list1) < 6 and value not in self.list1:
            self.list1.append(value)
            n.set(self.list1)
        elif len(self.list2) < 6 and value not in self.list2:
            self.list2.append(value)
            n2.set(self.list2)
        elif len(self.list3) < 6 and value not in self.list3:
            self.list3.append(value)
            n3.set(self.list3)

    def play(self):
        global prize
        y = 0
        self.n4 = self.numbers = random.sample(range(1, 49), 6)
        self.numbers.sort()
        self.list1.sort()
        self.matchings = set(self.list1).intersection(self.numbers)
        for x in range(len(self.matchings)):
            y += 1
        if y == 6 and y == len(self.matchings):
            prize = 10000000
        elif y == 5 and y == len(self.matchings):
            prize = 8584
        elif y == 4 and y == len(self.matchings):
            prize = 2384
        elif y == 3 and y == len(self.matchings):
            prize = 100.50
        elif y == 2 and y == len(self.matchings):
            prize = 20
        elif y < 2 and y == len(self.matchings):
            prize = 0
        self.set1.config(text=self.list1)
        self.numbers_lab.config(text=self.numbers)
        self.win_lab.config(text="You have won R" + str(prize) + " from 1st set")
        self.match_lab.config(text=str(y))

        global prize2
        y = 0
        self.n4 = self.numbers = random.sample(range(1, 49), 6)
        self.numbers.sort()
        self.list2.sort()
        self.matchings = set(self.list2).intersection(self.numbers)
        for x in range(len(self.matchings)):
            y += 1
        if y == 6 and y == len(self.matchings):
            prize2 = 10000000
        elif y == 5 and y == len(self.matchings):
            prize2 = 8584
        elif y == 4 and y == len(self.matchings):
            prize2 = 2384
        elif y == 3 and y == len(self.matchings):
            prize2 = 100.50
        elif y == 2 and y == len(self.matchings):
            prize2 = 20
        elif y < 2 and y == len(self.matchings):
            prize2 = 0
        self.set2.config(text=self.list2)
        self.numbers_lab.config(text=self.numbers)
        self.win_lab2.config(text="You have won R" + str(prize2) + " from 2nd set")
        self.match_lab2.config(text=str(y))

        global prize3
        y = 0
        self.n4 = self.numbers = random.sample(range(1, 49), 6)
        self.numbers.sort()
        self.list3.sort()
        self.matchings = set(self.list3).intersection(self.numbers)
        for x in range(len(self.matchings)):
            y += 1
        if y == 6 and y == len(self.matchings):
            prize3 = 10000000
        elif y == 5 and y == len(self.matchings):
            prize3 = 8584
        elif y == 4 and y == len(self.matchings):
            prize3 = 2384
        elif y == 3 and y == len(self.matchings):
            prize3 = 100.50
        elif y == 2 and y == len(self.matchings):
            prize3 = 20
        elif y < 2 and y == len(self.matchings):
            prize3 = 0
        self.set3.config(text=self.list3)
        self.numbers_lab.config(text=self.numbers)
        self.win_lab3.config(text="You have won R" + str(prize3) + " from 3rd set")
        self.match_lab3.config(text=str(y))

    def winnings(self):
        something_else = open('text_file.txt', 'a')
        self.total = (prize + prize2 + prize3)
        something_else.write("Total: " + str(self.total))
        messagebox.showinfo("STATUS", "Your total winnings is R" + str(self.total))

    def exit(self):
        root.destroy()

    def clear(self):
        n.set(self.list1.clear())
        n2.set(self.list2.clear())
        n3.set(self.list3.clear())
        self.set1.config(text="")
        self.set2.config(text="")
        self.set3.config(text="")
        self.match_lab.config(text="")
        self.match_lab2.config(text="")
        self.match_lab3.config(text="")
        self.win_lab.config(text="")
        self.win_lab2.config(text="")
        self.win_lab3.config(text="")
        self.numbers_lab.config(text="")

    def claim(self):
        root.destroy()
        import screen3






gen(root)
root.mainloop()