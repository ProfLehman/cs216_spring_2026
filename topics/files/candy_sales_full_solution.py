
# candy_sales_full_solution.py

# prof. lehman
# spring 2026

# CSV Processing Lab Sample Solution
# AI generated with slight modifications (ChatGPT)


# Uses readline() and split() instead of csv.reader

# -----------------------------
# Task 1 - Read and Display Products
# -----------------------------
print("TASK 1 - PRODUCTS")
file = open("products.csv", "r")

line = file.readline()   # skip header

line = file.readline()
while line != "":
    parts = line.strip().split(",")

    product_name = parts[1]
    price = float(parts[2])

    print(product_name, price)

    line = file.readline()

file.close()
print()


# -----------------------------
# Task 2 - Read and Display Sales
# -----------------------------
print("TASK 2 - FIRST 10 SALES")
file = open("sales.csv", "r")

count = 0

line = file.readline()   # skip header

line = file.readline()
while line != "" and count < 10:
    parts = line.strip().split(",")

    sale_id = parts[0]
    student_name = parts[1]
    customer_name = parts[2]
    phone = parts[3]
    product_name = parts[4]
    qty = int(parts[5])

    print(sale_id, student_name, customer_name, product_name, qty)

    count += 1
    line = file.readline()

file.close()
print()



# -----------------------------
# Task 3 - Count Total Sales
# -----------------------------
print("TASK 3 - TOTAL SALES TRANSACTIONS")
file = open("sales.csv", "r")

sales_count = 0

line = file.readline()   # skip header

line = file.readline()
while line != "":
    sales_count += 1
    line = file.readline()

file.close()

print("Total sales transactions:", sales_count)
print()



# -----------------------------
# Task 4 - Total Quantity Sold
# -----------------------------
print("TASK 4 - TOTAL QUANTITY SOLD")
file = open("sales.csv", "r")

total_qty = 0

line = file.readline()   # skip header

line = file.readline()
while line != "":
    parts = line.strip().split(",")
    
    qty = int(parts[5])
    total_qty += qty
    
    line = file.readline()

file.close()

print("Total quantity sold:", total_qty)
print()


# -------------------------------
# Task 5 - Unique Students (LIST)
# -------------------------------
print("TASK 5 - UNIQUE STUDENTS")

file = open("sales.csv", "r")

line = file.readline() #skip headings

students = []

line = file.readline()
while line != "":
    parts = line.strip().split(",")
    student_name = parts[1]

    if student_name not in students:
        students.append(student_name)

    line = file.readline()

file.close()

for s in students:
    print(s)

print("Total unique students:", len(students))
print()



# -----------------------------
# Task 6 - Sales per Student (Quantity)
# -----------------------------
print("TASK 6 - SALES PER STUDENT")

file = open("sales.csv", "r")

line = file.readline() # skip headings

student_qty = {} #dictionary

line = file.readline()
while line != "":
    parts = line.strip().split(",")
    student_name = parts[1]
    qty = int(parts[5])

    if student_name not in student_qty:
        student_qty[student_name] = 0

    student_qty[student_name] += qty

    line = file.readline()

file.close()

for student in student_qty:
    print(student, ":", student_qty[student])
print()



# -----------------------------
# Task 7 - Sales per Product
# -----------------------------
print("TASK 7 - SALES PER PRODUCT")

file = open("sales.csv", "r")

line = file.readline() # skip headings

product_qty = {}

line = file.readline()
while line != "":
    parts = line.strip().split(",")
    product_name = parts[4]
    qty = int(parts[5])

    if product_name not in product_qty:
        product_qty[product_name] = 0

    product_qty[product_name] += qty

    line = file.readline()

file.close()

for product in product_qty:
    print(product, ":", product_qty[product])
print()



# -----------------------------
# Task 8 - Most Popular Product
# -----------------------------
print("TASK 8 - MOST POPULAR PRODUCT")

best_product = ""
best_qty = 0

for product in product_qty:
    if product_qty[product] > best_qty:
        best_product = product
        best_qty = product_qty[product]

print(best_product, best_qty)
print()


# -----------------------------
# Task 9 - Product Lookup
# -----------------------------
print("TASK 9 - PRODUCT LOOKUP")

# dictionary - product name => price
product_prices = {} 

file = open("products.csv", "r")
line = file.readline()
line = file.readline()

while line != "":
    parts = line.strip().split(",")
    product_name = parts[1]
    price = float(parts[2])

    product_prices[product_name] = price

    line = file.readline()

file.close()

print(product_prices)
print()


# -----------------------------
# Task 10 - Total Revenue
# -----------------------------
print("TASK 10 - TOTAL REVENUE")

file = open("sales.csv", "r")

line = file.readline() # skip headings

total_revenue = 0

line = file.readline()
while line != "":

    parts = line.strip().split(",")
    product = parts[4]
    qty = int(parts[5])

    if product not in product_prices:
        print("Error: missing product", product)
    else:
        total_revenue += qty * product_prices[product]

    line = file.readline()

file.close()

print("Total revenue:", total_revenue)
print()



# -----------------------------
# Task 11 - Revenue per Product
# -----------------------------
print("TASK 11 - REVENUE PER PRODUCT")

file = open("sales.csv", "r")
line = file.readline() # skip headings

product_revenue = {}

line = file.readline()
while line != "":
    parts = line.strip().split(",")
    product = parts[4]
    qty = int(parts[5])

    if product in product_prices:
        revenue = qty * product_prices[product]

        if product not in product_revenue:
            product_revenue[product] = 0

        product_revenue[product] += revenue
    else:
        print("Error: missing product", product)
        
    line = file.readline()

file.close()

for product in product_revenue:
    print(product, product_revenue[product])
print()



# -----------------------------
# Task 12 - Revenue per Student
# -----------------------------
print("TASK 12 - REVENUE PER STUDENT")

file = open("sales.csv", "r")

line = file.readline() # skip headings

student_revenue = {}

line = file.readline()
while line != "":
    parts = line.strip().split(",")
    student = parts[1]
    product = parts[4]
    qty = int(parts[5])

    if product in product_prices:
        revenue = qty * product_prices[product]

        if student not in student_revenue:
            student_revenue[student] = 0

        student_revenue[student] += revenue
    else:
        print("Error: missing product", product)
        
    line = file.readline()

file.close()

for student in student_revenue:
    print(student, student_revenue[student])
print()



# -----------------------------
# Task 13 - Top Student Seller
# -----------------------------
print("TASK 13 - TOP STUDENT")

top_student = ""
top_value = 0

for student in student_revenue:
    if student_revenue[student] > top_value:
        top_student = student
        top_value = student_revenue[student]

print(top_student, top_value)
print()


# -----------------------------
# Task 14 - Highest Single Sale
# -----------------------------
print("TASK 14 - HIGHEST SALE")

file = open("sales.csv", "r")
line = file.readline() # skip headings
line = file.readline()

best_value = 0
best_sale = ""

while line != "":
    parts = line.strip().split(",")

    student = parts[1]
    customer = parts[2]
    product = parts[4]
    qty = int(parts[5])

    if product in product_prices:
        value = qty * product_prices[product]

        if value > best_value:
            best_value = value
            best_sale = student + " " + product + " " + str(qty)
    else:
        print("Error: missing product", product)
        
    line = file.readline()

file.close()

print(best_sale, best_value)
print()


# -----------------------------
# Task 15 - Average Sale
# -----------------------------
print("TASK 15 - AVERAGE SALE")

avg = total_revenue / sales_count
print(avg)
print()


# -----------------------------
# Task 16 - Unique Customers (LIST)
# -----------------------------
print("TASK 16 - UNIQUE CUSTOMERS")

file = open("sales.csv", "r")
line = file.readline() # skip headings

customers = []

line = file.readline()
while line != "":
    parts = line.strip().split(",")
    customer = parts[2]

    if customer not in customers:
        customers.append(customer)

    line = file.readline()

file.close()

print("Unique customers:", len(customers))
print()


# -----------------------------
# Task 17 - Top Customer
# -----------------------------
print("TASK 17 - TOP CUSTOMER")

file = open("sales.csv", "r")
line = file.readline() # skip headings
line = file.readline()

customer_qty = {}

while line != "":
    parts = line.strip().split(",")
    customer = parts[2]
    qty = int(parts[5])

    if customer not in customer_qty:
        customer_qty[customer] = 0

    customer_qty[customer] += qty

    line = file.readline()

file.close()

top_customer = ""
top_qty = 0

for c in customer_qty:
    if customer_qty[c] > top_qty:
        top_customer = c
        top_qty = customer_qty[c]

print(top_customer, top_qty)
print()


# -----------------------------
# Task 18 - Leaderboard
# -----------------------------
print("TASK 18 - LEADERBOARD")

leaderboard = []

for student in student_revenue:
    leaderboard.append((student_revenue[student], student))

leaderboard.sort(reverse=True)

for item in leaderboard:
    print(item[1], item[0])
print()



# -----------------------------
# Task 19 - Validation
# -----------------------------
print("TASK 19 - VALIDATION")

file = open("sales.csv", "r")
line = file.readline() # skip headings
line = file.readline()

while line != "":
    parts = line.strip().split(",")

    product = parts[4]
    qty = int(parts[5])

    if product not in product_prices:
        print("Error: Missing Product:", product)

    if qty <= 0:
        print("Error: Missing qty:", qty)

    line = file.readline()

file.close()
print()



# -----------------------------
# Task 20 - Write File
# -----------------------------
print("TASK 20 - WRITE FILE")

out = open("student_totals.csv", "w")
out.write("student,total_items,total_revenue\n")

for student in student_qty:
    out.write(student + "," + str(student_qty[student]) + "," + str(student_revenue[student]) + "\n")

out.close()

print("File written.")

