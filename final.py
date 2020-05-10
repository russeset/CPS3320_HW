#imports libraries
import io
import random
from datetime import datetime, timedelta
import pandas as pd
import tkinter as tk
from tkinter import *

#start of GUI
root = tk.Tk()
root.title('Python Final Project')
root.geometry("750x750")
root.configure(bg='lightblue')

#functions for easy readability
#used to round the current time up an hour for driver selection
def rounder(t):
    if t.minute >= 30:
        return t.replace(second=0, microsecond=0, minute=0, hour=t.hour+1)
    else:
        return t.replace(second=0, microsecond=0, minute=0)

#reads how many people the list is for in order to ration selected items
def tot(price, num):
    item = float(price) * float(num)
    return float(item)

#takes order input, appends the items and prices to lists, then opens next page
#based on users grocery list length
def takes_input(finish, price, item, orderPrice, orderItem, num, count):
    orderPrice.append(float(price))
    orderItem.append(item)
    count = count + 1
    if count == 10 or finish == True:
        check(num, price, item, orderPrice, orderItem)
    elif count != 10 or finish == False:
        order(num, count, orderPrice, orderItem)

#GUI funcions
def orderInformation():
    global customerName, customerNumber, customerOrderNumber, lbl, lb, lblT, isClicked
    nxt = tk.Toplevel()
    nxt.title('Python Final Project: Order Information')
    nxt.geometry("750x750")
    nxt.configure(bg='lightblue')
    #input regarding customer's name, total number for order, and order number
    lbl = tk.Label(nxt, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="What name will your order be under?")
    lbl.pack(pady=20)
    customerName = tk.Entry(nxt)
    customerName.pack()
    lb = tk.Label(nxt, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="How many people will be under your order?")
    lb.pack(pady=30)
    customerNumber = tk.Entry(nxt)
    customerNumber.pack()
    customerOrderNumber = random.randint(1, 10000)
    lblT = tk.Label(nxt, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 30 bold", text=" ")
    lblT.pack(pady=20)
    #writing customer info to Customer_Info file
    bt = tk.Button(nxt, text="Submit", bg="white", font=('calibri', 16, 'bold', 'underline'), foreground='darkblue', command=lambda:submit(str(customerName.get()), int(customerNumber.get()), customerOrderNumber, nxt))
    bt.pack(padx=10, pady=15)

def order(num, count, orderPrice, orderItem):
    tp = tk.Toplevel()
    tp.title('Python Final Project: Order')
    tp.geometry("750x750")
    tp.configure(bg='lightblue')
    lab = tk.Label(tp, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="")
    lab.pack(pady=20)
    if count >= 10:
        lab['text']="Max Order Limit Reached!"
        button.config(state=DISABLED)
        button2 = tk.Button(tp, text="Submit Order", bg="white", font=('calibri', 16, 'bold', 'underline'), foreground='darkblue', command=lambda:check(num, orderPrice))
        button2.pack(pady=40)
    else:
        #taking order information
        iN = tk.Label(tp, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="Item Name #" + str(count + 1) + ": ")
        iN.pack(pady=20)
        itemName = tk.Entry(tp)
        itemName.pack()
        iP = tk.Label(tp, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="Item Price #" + str(count + 1) + ": ")
        iP.pack(pady=20)
        itemPrice = tk.Entry(tp)
        itemPrice.pack()
        button = tk.Button(tp, text="Next Item", bg="white", font=('calibri', 16, 'bold', 'underline'), foreground='darkblue', command=lambda:[takes_input(False, itemPrice.get(), str(itemName.get()), orderPrice, orderItem, num, count), tp.destroy()])
        button.pack(pady=35)
        button2 = tk.Button(tp, text="Submit Order", bg="white", font=('calibri', 16, 'bold', 'underline'), foreground='darkblue', command=lambda:[takes_input(True, itemPrice.get(), str(itemName.get()), orderPrice, orderItem, num, count), tp.destroy()])
        button2.pack(pady=40)

def check(num, price, name, orderPrice, orderItem):
    #calculation of rationed items based on order size
    count = 0
    total = 0
    for item in orderPrice:
        orderPrice[count] = tot(item, num)
        count += 1

    #writing output to order file for driver
    c = 0
    orderInfo = open('Order_Info.txt', 'w+', encoding='UTF-8')
    for item in orderItem:
        orderInfo.write("%-20s" %(item.upper()) + "%-5s" %("x" + str(num)) + '${:,.2f}'.format(orderPrice[c]) + "\n")
        total = float(total) + orderPrice[c]
        c += 1
    orderInfo.write("%25s" %("Total:") + '${:,.2f}'.format(total))
    orderInfo.close()
    complete(total, orderItem, orderPrice)

def submit(name, number, orderNumber, nxt):
    global customerInfo
    orderPrice = []
    orderItem = []
    count = 0
    if len(name) == 0 and len(str(number)) == 0:
        lblT['text']="No information was updated. Please input a name and number."
    elif len(str(number)) == 0:
        lblT['text']="Name was input, but no number. Please input a number."
    elif len(name) == 0:
        lblT['text']="Name was not input, but number was. Please input a name."
    else:
        #opening customer info page
        customerInfo = open('Customer_Info.txt', 'w+', encoding='utf-8')
        customerInfo.write('Customer Order Name:\t' + str(name) + '\n')
        customerInfo.write('Customer Total Number:\t' + str(number) + '\n')
        customerInfo.write('Customer Order Number:\t#' + str(orderNumber))
        customerInfo.close()
        #continue to order, cant continue until information is update
        btn = tk.Button(nxt, command=lambda:[order(int(number), int(count), orderPrice, orderItem), nxt.destroy()])
        btn.config(text="Continue to Order", bg="white", font=('calibri', 16, 'bold', 'underline'), foreground='darkblue')
        btn.pack(padx=10, pady=10)
        lblT['text']="Order Information Updated!"

def complete(total, orderItem, orderPrice):
    top = tk.Toplevel()
    top.title('Python Final Project: Order Complete')
    top.geometry("750x750")
    top.configure(bg='lightblue')
    #outputting order information
    result = []
    l2 = tk.Label(top, justify=tk.LEFT, padx=15, bg="lightblue", fg="white", font="Times 18 italic", text="")
    for i in range(len(orderItem)):
        result.append('%-20s' % str(orderItem[i]))
        result.append('%20s' %(str('${:,.2f}'.format(orderPrice[i])))+'\n')
        text = ''.join(result)
        l2.configure(text=text)
    l2.pack(padx=10, pady=10)
    l = tk.Label(top, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="")
    l['text'] = "Your total is: " + '${:,.2f}'.format(total)
    l.pack()
    donationInfo = open('Donation_Info.txt', 'r+', encoding='UTF-8')
    line = int(donationInfo.read())
    t = float(line)
    t -= float(total)
    donationInfo.seek(0)
    donationInfo.write(str(t))
    donationInfo.truncate()
    donationInfo.close()
    
    #checking time for driver selection
    now = rounder(datetime.now())
    new = str(now)[11:16]
    driverInfo = open('Driver_Info.txt', 'r', encoding='UTF-8')
    for line in driverInfo.readlines():
        line = line.strip()

        #checking for odd value numbers in time slot
        if new == ' 1:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == ' 3:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == ' 5:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == ' 7:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == ' 9:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == '11:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == '13:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == '15:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == '17:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == '19:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == '21:00':
            new = str(now + timedelta(hours=1))[11:16]
        elif new == '23:00':
            new = str(now + timedelta(hours=1))[11:16]
        #comparing time with driverInfo file
        if new in line[16:21]:
            lab = tk.Label(top, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="Your delivery driver will be: " + line[:7])
            lab.pack(padx=15, pady=20)
            break
        elif new in line[27:32]:
            lab = tk.Label(top, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="Your delivery driver will be: " + line[:7])
            lab.pack(padx=15, pady=20)
            break
        else:
            continue
    driverInfo.close()
    button = tk.Button(top, text="Return to Main Menu", bg="white", font=('calibri', 16, 'bold', 'underline'), foreground='darkblue', command=lambda:top.destroy())
    button.pack(padx=10, pady=20)

#Donations
def donation():
    nt = tk.Toplevel()
    nt.title('Python Final Project: Donations')
    nt.geometry("750x750")
    nt.configure(bg='lightblue')
    d = tk.Label(nt, text="Donation of: $")
    d.config(justify=tk.CENTER, padx=15, pady=50, bg="lightblue", fg="white", font="Times 28 bold")
    d.pack()
    dona = tk.Entry(nt)
    dona.pack(pady=0)
    don = tk.Button(nt, text="Donate", command=lambda: [donate(dona.get()), nt.destroy()])
    don.config(bg="white", font=('calibri', 16, 'bold', 'underline'), justify=tk.CENTER, foreground='darkblue')
    don.pack(padx=20, pady=100)

def donate(do):
    nop = tk.Toplevel()
    nop.title('Python Final Project: Thank You for Donating!')
    nop.geometry("750x750")
    nop.configure(bg='lightblue')
    donationInfo = open('Donation_Info.txt', 'r+', encoding='UTF-8')
    try:
        val = int(do)
        if val <= 0.0:
            ln = tk.Label(nop, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="Sorry, invalid input. Please try again.")
            ln.pack(pady=30)
        else:
            line = int(donationInfo.read())
            total = int(line)
            total += int(do)
            donationInfo.seek(0)
            donationInfo.write(str(total))
            donationInfo.truncate()
            l = tk.Label(nop, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text=("Thank you for donating $" + str(do) + ".00 to our cause!"))
            l.pack(padx=10, pady=20)
    except ValueError:
        lab = tk.Label(nop, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 22 bold", text="Invalid Input: No Donation Input. Please Try Again.")
        lab.pack(padx=10, pady=20)
        back = tk.Button(nop, text="Back", bg="white", font=('calibri', 16, 'bold', 'underline'), foreground='darkblue', command=lambda:[donation(), nop.destroy()])
        back.pack(padx=10, pady=50)
    donationInfo.close()
    button = tk.Button(nop, text="Return to Main Menu", bg="white", font=('calibri', 16, 'bold', 'underline'), foreground='darkblue', command=lambda:nop.destroy())
    button.pack(padx=10, pady=30)

#homepage begins
homepage = tk.Label(root, justify=tk.CENTER, padx=10, pady=20, bg="lightblue", fg="white", text="Welcome to our Grocery Delivery Service!", font = "Helvetica 24 bold italic")
homepage.pack(padx=10, pady=10)
description = tk.Label(root, text="", justify=tk.CENTER, padx=5, pady=10, bg="lightblue", fg="white", font="Times 12 italic")
description.config(text="GDS is a non-profit organization that runs it's program based on donations big and small from the community.\nAll proceeds go towards the delivery of grocery's from stores within reach of our drivers,\nat the best price as to save money.\nPlease, donate if you wish for our program to continue and succeed\nfor our elderly folks as well as poorer families in times of hardship.")
description.pack( pady=5)
home = tk.Label(root, justify=tk.CENTER, padx=15, pady=35, bg="lightblue", fg="white", text="Please select an option:", font="Helvetica 16 bold italic")
home.pack()
o = tk.Label(root, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", font="Times 14 bold", text="To place an order:")
o.pack()
btn = tk.Button(root, text="Order Information", bg="white", font=('calibri', 10, 'bold', 'underline'), foreground='darkblue', command=orderInformation)
btn.config(padx=20, pady=10, overrelief="groove")
btn.pack(padx=20, pady=20)
padding = tk.Label(root, text="", bg="lightblue", pady=20).pack()
d = tk.Label(root, justify=tk.CENTER, padx=15, bg="lightblue", fg="white", text="For donations:", font="Times 14 bold")
d.pack()
button = tk.Button(root, text="Donations", bg="white", font=('calibri', 10, 'bold', 'underline'), foreground='darkblue', command=donation)
button.config(padx=20, pady=10, overrelief="groove")
button.pack(padx=10, pady=10)


root.mainloop()
