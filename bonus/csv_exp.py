import csv


with open("../files/weather.csv",'r') as file:
    mylist = list(csv.reader(file))

for item in mylist:
    print(item)


