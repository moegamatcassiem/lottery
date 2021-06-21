from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox
# from PIL import ImageTk,Image.


root = Tk()
root.geometry("500x550")
root.title("Results")
root.config(bg="yellow")

results = StringVar()
values1 = StringVar()
values2 = StringVar()

class winnings:
    def __init__(self, master):
        # Lables
        self.currency_lab1 = Label(master, text="Account Name: ", bg="yellow")
        self.currency_lab1.place(x=10, y=10)
        self.banking_lab = Label(master, text="Account Number: ", bg="yellow")
        self.banking_lab.place(x=10, y=50)
        self.winnings = Label(master, text="Your winnings: ", bg="yellow")
        self.winnings.place(x=10, y=90)
        self.bank_local = Label(master, text="Please pick your bank: ", bg="yellow")
        self.bank_local.place(x=10, y=170)
        self.select_currency_lab = Label(master, bg="yellow", text="Select your currency")
        self.select_currency_lab.place(x=10, y=130)
        self.converted = Label(master, text=self.amount)
        self.converted.place(x=10, y=210)

        # Entries
        self.bank_name = Entry(master)
        self.bank_name.place(x=150, y=10)
        self.bank_account = Entry(master)
        self.bank_account.place(x=150, y=50)
        self.prize = Entry(master)
        self.prize.place(x=150, y=90)

        # with open("text_file.txt") as x:
        #     for y in x:
        #         if "Total" in y:
        #             amount = int(y[7:-1])


        self.information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
        self.information_json = self.information.json()

        self.conversion = self.information_json['conversion_rates']

        self.currency = []
        for i in self.conversion.keys():
            self.currency.append(i)

        self.select_currency = ttk.Combobox(root)
        self.select_currency['values'] = self.currency
        self.select_currency['state'] = 'readonly'
        self.select_currency.set('Select Currency')
        self.select_currency.place(x=150, y=130)

        self.bank_list = ["FNB", "Standard Bank", "Nedbank", "ABSA"]
        self.banks = ttk.Combobox(master)
        self.banks['values'] = self.bank_list
        self.banks['state'] = 'readonly'
        self.banks.set("Select your bank")
        self.banks.place(x=170, y=170)

        self.convert_btn = Button(root, text="CONVERT", borderwidth=3, bg='white', command=self.perform)
        self.convert_btn.place(x=180, y=430)
        self.exit_btn = Button(root, text="EXIT", borderwidth=3, bg='white', command=self.kill)
        self.exit_btn.place(x=281, y=480)

    def convert(self,to_currency):
        self.amount = round(self.amount * self.conversion[to_currency], 4)
        return self.amount

    def perform(self):
        try:
            self.amount = float(self.prize.get())
            to_curr = self.select_currency.get()

            converted_amount = self.convert(self.amount)

            results.set(converted_amount)
        except ValueError:
            if self.prize != int and self.prize != float:
                messagebox.showerror('Entry not valid', 'Enter numbers only')

        except requests.exceptions.ConnectionError:
            messagebox.showerror('Internet error', 'Internet Bad')
        except KeyError:
            messagebox.showerror("ERROR!", "Select Currency")

        # kill program
    def kill(self):
        return root.destroy()






winnings(root)
root.mainloop()