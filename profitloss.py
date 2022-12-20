import numpy as np
bList = []
sList = []
number1 = input("Enter number and hit enter ")

if int(number1) > 500:
        number1 = 500 

for x in range(int(number1)):
        print("Enter the buy & sell numbers: ")
        x, y = [int(x) for x in input().split()] 

        bList.append(x)
        sList.append(y)

print (bList, sList)

for x in range(int(number1)):
        print("Profit") if bList[x] < sList[x] else print("Neutral") if bList[x] == sList[x] else print("Loss")