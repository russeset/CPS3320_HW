#imports libraries
import io
import random
from datetime import datetime, timedelta
import pandas as pd
import tkinter as tk

#start of GUI
root = Tk()
root.title('Python Final Project')
root.geometry("500x500")
root.configure(bg='lightblue')

#GUI functions for buttons
def order():
    nxt = Toplevel()
    

#functions for easy readability
#used to round the current time up an hour for driver selection
def rounder(t):
    if t.minute >= 30:
        return t.replace(second=0, microsecond=0, minute=0, hour=t.hour+1)
    else:
        return t.replace(second=0, microsecond=0, minute=0)

#reads how many people the list is for in order to ration selected items
def total(price, num):
    item = float(price) * float(num)
    return float(item)

#start of main program

#file input
customerInfo = open("Customer_Info.txt", "w+", encoding='utf-8')
orderInfo = open("Order_Info.txt", "w+", encoding='utf-8')
donationInfo = open("Donation_Info.txt", "r+", encoding='utf-8')
driverInfo = open("Driver_Info.txt", "r", encoding='utf-8')

#checking if files opened or not
if (customerInfo.closed or orderInfo.closed or donationInfo.closed or driverInfo.closed):{
    print("Error: Files could not be opened. Please try again later.")
}

#arrays for order storage is created
orderItem = []
orderPrice = []

#input regarding customer's name, total number for order, and order number
customerName = str(input("What name will your order be under?: "))
customerNumber = int(input("How many people will be under your order?: "))
customerOrderNumber = random.randint(1, 10000)

#writing customer info to Customer_Info file
customerInfo.write("Customer Order Name:\t" + customerName + "\n")
customerInfo.write("Customer Total Number:\t" + str(customerNumber) + "\n")
customerInfo.write("Customer Order Number:\t#" + str(customerOrderNumber))
customerInfo.close()

#taking order information
count = 15
more = ""
while count > 0:
    itemName = str(input("Item Name: "))
    orderItem.append(itemName)
    itemPrice = float(input("Item Price: "))
    orderPrice.append(itemPrice)
    count -= 1
    more = str(input("Keep going? (y/n): "))
    if more == 'n':
        break
    else:
        continue
    
#calculation of rationed items based on order size
count = 0
for item in orderPrice:
    orderPrice[count] = total(item, customerNumber)
    count += 1

#writing output to order file for driver
total = 0
c = 0
for item in orderItem:
    orderInfo.write("%-20s" %(item.upper()) + '${:,.2f}'.format(orderPrice[c]) + "\n")
    total = float(total) + orderPrice[c]
    c += 1
orderInfo.write("%20s" %("Total:") + '${:,.2f}'.format(total))


#checking for time for driver selection
now = rounder(datetime.now())
new = str(now)[11:16]
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
        print("\nYour delivery driver will be: " + line[:7])
        break
    elif new in line[27:32]:
        print("\nYour delivery driver will be: " + line[:7])
        break
    else:
        continue

#Donations
donate = str(input("\nWould you like to donate? (y/n): "))
while donate != 'y' or donate != 'n':
    if donate == 'y':
        while True:
            donation = input("Donation of: $")
            try:
                val = int(donation)
                if val <= 0:
                    print("Sorry, input must be positive. Please try again.")
                    continue
                else:
                    line = int(donationInfo.read())
                    total = int(line)
                    total += int(donation)
                    donationInfo.seek(0)
                    donationInfo.write(str(total))
                    donationInfo.truncate()
                    print("\nThank you for donating $" + str(donation) + ".00 to our cause!")
                break
            except ValueError:
                print("Invalid Input: Please try again.")
        break
    elif donate == 'n':
        print("Thank you for your consideration.")
        break
    else:
        print("Invalid Input: Please try again.")
        donate = str(input("Would you like to donate? (y/n): "))

#closes files for saving information
#customerInfo.close()
orderInfo.close()
donationInfo.close()
driverInfo.close()

#end of program
print("\nThank you, have a great day!")

root.mainloop()
