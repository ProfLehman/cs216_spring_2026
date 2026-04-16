# Task 1 – Read and Display Products
# Read products.csv
# Print each product with its price

file = open("products.csv", "r")

headings = file.readline()

line = file.readline()
while line != "":
    
    # print( line )
    
    parts = line.strip().split(",")

    number = parts[0]
    candy_name = parts[1]
    price = float( parts[2] )
    
    print(number, candy_name, price)

    line = file.readline()

file.close()

print()
print()

import csv
from itertools import islice

total_items_sold =  0

with open("sales.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # skip header line

    #for row in islice(reader, 10):
    for row in reader:
        
        #print( row )
        who_sold = row[1]
        candy_name = row[4]
        qty = int(row[5])

        total_items_sold += qty

        print(who_sold, candy_name, qty)


print()
print()

file = open("sales.csv", "r")
count = 0

students = {}

file.readline()
line = file.readline()
while line != "":
    count = count + 1
    
    parts = line.strip().split(",")
    name = parts[1]
    qty = int( parts[5] )
    print( name, qty )

    if name not in students:
        students[name] = qty
    else:
        students[name] += qty
        
    line = file.readline()
    
print("Number of sales = ", count)
print("Number of items sold = ", total_items_sold)
    
print( students )
print( len(students) )

for student, total in students.items():
    print(student, total)



