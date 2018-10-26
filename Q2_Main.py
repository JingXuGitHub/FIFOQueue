# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:03:35 2018

@author: Jing
"""

import Car
import FIFOQueue as FIFO

# Test 
menulist = ['Enter: ',
		'1  for Enqueue', 
		'2  for Dequeue', 
		'3  for Print']
def menu():
	for i in range(len(menulist)):
		print(menulist[i])
	return int(input())

def Main():
    FIFOQUE = FIFO.FIFOQue()
    try:
        fo = open("Cars.txt", "r")
    except IOError:
        print("No such file!")
    else:
        for line in fo.readlines():
            info = line.split()
            Make = info[0]
            Model = info[1]
            Year = int(info[2])
            Mileage = float(info[3])
            Price = float(info[4])
            newCar = Car.Car(Make, Model, Year, Mileage, Price)
            FIFOQUE.Enqueue(newCar)
        fo.close()
    print("Cars information in the system are as follows:")
    FIFOQUE.Print()    
    s = menu()
    while s in range(1,4):
        if s == 1:
            print("Enter the information of the car you want to Enqueue:")
            Make = input("Make: ")
            Model = input("Model: ")
            Year = int(input("Year: "))
            Mileage = float(input("Mileage: "))
            Price = float(input("Price: "))
            newCar = Car.Car(Make, Model, Year, Mileage, Price)
            FIFOQUE.Enqueue(newCar)
            print("Cars information in the system are as follows: ")
            FIFOQUE.Print()
        if s == 2:
            print("Dequeuing...")
            temp = FIFOQUE.Dequeue()
            print("Cars information dequeued are as follows: Make: %s, Model: %s, Year: %d, Mileage: %.0f, Price: %.0f" % (temp.data.Make, temp.data.Model, temp.data.Year, temp.data.Mileage, temp.data.Price))
        if s == 3:
            FIFOQUE.Print()
        s = menu()
Main()