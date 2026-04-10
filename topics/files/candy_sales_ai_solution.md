
## Candy Fundraiser Sales Analysis

This sample solution uses:

* `readline()`
* `strip()`
* `split(",")`

It does **not** use the `csv` module.

## Assumed File Formats

### `products.csv`

```text
product_name,price
Chocolate Bar,1.50
Gummy Bears,2.00
Lollipop,0.75
```

### `sales.csv`

```text
sale_id,student_name,customer_name,phone,product_name,qty
1,Ava Johnson,Liam Smith,260-555-1001,Chocolate Bar,3
2,Noah Miller,Emma Brown,260-555-1002,Gummy Bears,2
3,Ava Johnson,Olivia Davis,260-555-1003,Lollipop,5
```

---

## Full Sample Solution Code

```python
# CS 111 - CSV Processing Lab Sample Solution
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

    product_name = parts[0]
    price = float(parts[1])

    print(product_name, price)

    line = file.readline()

file.close()
print()


# -----------------------------
# Task 2 - Read and Display Sales
# -----------------------------
print("TASK 2 - FIRST 10 SALES")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

count = 0
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

line = file.readline()   # skip header
line = file.readline()

sales_count = 0
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

line = file.readline()   # skip header
line = file.readline()

total_qty = 0
while line != "":
    parts = line.strip().split(",")
    qty = int(parts[5])
    total_qty += qty
    line = file.readline()

file.close()

print("Total quantity sold:", total_qty)
print()


# -----------------------------
# Task 5 - Unique Students
# -----------------------------
print("TASK 5 - UNIQUE STUDENTS")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

students = set()

while line != "":
    parts = line.strip().split(",")
    student_name = parts[1]
    students.add(student_name)
    line = file.readline()

file.close()

for student in students:
    print(student)

print("Total unique students:", len(students))
print()


# -----------------------------
# Task 6 - Sales per Student (Quantity)
# -----------------------------
print("TASK 6 - QUANTITY SOLD PER STUDENT")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

student_qty = {}

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
    print(student + ":", student_qty[student], "items")
print()


# -----------------------------
# Task 7 - Sales per Product (Quantity)
# -----------------------------
print("TASK 7 - QUANTITY SOLD PER PRODUCT")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

product_qty = {}

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
    print(product + ":", product_qty[product], "items")
print()


# -----------------------------
# Task 8 - Most Popular Product
# -----------------------------
print("TASK 8 - MOST POPULAR PRODUCT")

best_product = ""
best_qty = 0

for product in product_qty:
    if product_qty[product] > best_qty:
        best_qty = product_qty[product]
        best_product = product

print("Most popular product:", best_product)
print("Quantity sold:", best_qty)
print()


# -----------------------------
# Task 9 - Build a Product Lookup
# -----------------------------
print("TASK 9 - PRODUCT LOOKUP")

product_prices = {}

file = open("products.csv", "r")

line = file.readline()   # skip header
line = file.readline()

while line != "":
    parts = line.strip().split(",")
    product_name = parts[0]
    price = float(parts[1])

    product_prices[product_name] = price

    line = file.readline()

file.close()

for product in product_prices:
    print(product, "->", product_prices[product])
print()


# -----------------------------
# Task 10 - Calculate Total Revenue
# -----------------------------
print("TASK 10 - TOTAL REVENUE")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

total_revenue = 0.0

while line != "":
    parts = line.strip().split(",")
    product_name = parts[4]
    qty = int(parts[5])

    price = product_prices[product_name]
    total_revenue += qty * price

    line = file.readline()

file.close()

print("Total revenue: $" + format(total_revenue, ".2f"))
print()


# -----------------------------
# Task 11 - Revenue per Product
# -----------------------------
print("TASK 11 - REVENUE PER PRODUCT")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

product_revenue = {}

while line != "":
    parts = line.strip().split(",")
    product_name = parts[4]
    qty = int(parts[5])

    price = product_prices[product_name]
    sale_total = qty * price

    if product_name not in product_revenue:
        product_revenue[product_name] = 0.0

    product_revenue[product_name] += sale_total

    line = file.readline()

file.close()

for product in product_revenue:
    print(product + ": $" + format(product_revenue[product], ".2f"))
print()


# -----------------------------
# Task 12 - Revenue per Student
# -----------------------------
print("TASK 12 - REVENUE PER STUDENT")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

student_revenue = {}

while line != "":
    parts = line.strip().split(",")
    student_name = parts[1]
    product_name = parts[4]
    qty = int(parts[5])

    price = product_prices[product_name]
    sale_total = qty * price

    if student_name not in student_revenue:
        student_revenue[student_name] = 0.0

    student_revenue[student_name] += sale_total

    line = file.readline()

file.close()

for student in student_revenue:
    print(student + ": $" + format(student_revenue[student], ".2f"))
print()


# -----------------------------
# Task 13 - Top Student Seller
# -----------------------------
print("TASK 13 - TOP STUDENT SELLER")

top_student = ""
top_revenue = 0.0

for student in student_revenue:
    if student_revenue[student] > top_revenue:
        top_revenue = student_revenue[student]
        top_student = student

print("Top student seller:", top_student)
print("Revenue: $" + format(top_revenue, ".2f"))
print()


# -----------------------------
# Task 14 - Highest Single Sale
# -----------------------------
print("TASK 14 - HIGHEST SINGLE SALE")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

best_sale_value = 0.0
best_sale_text = ""

while line != "":
    parts = line.strip().split(",")
    sale_id = parts[0]
    student_name = parts[1]
    customer_name = parts[2]
    product_name = parts[4]
    qty = int(parts[5])

    price = product_prices[product_name]
    sale_total = qty * price

    if sale_total > best_sale_value:
        best_sale_value = sale_total
        best_sale_text = sale_id + " | " + student_name + " | " + customer_name + " | " + product_name + " | " + str(qty)

    line = file.readline()

file.close()

print("Highest single sale:", best_sale_text)
print("Value: $" + format(best_sale_value, ".2f"))
print()


# -----------------------------
# Task 15 - Average Sale Value
# -----------------------------
print("TASK 15 - AVERAGE SALE VALUE")

average_sale = total_revenue / sales_count
print("Average sale value: $" + format(average_sale, ".2f"))
print()


# -----------------------------
# Task 16 - Unique Customers
# -----------------------------
print("TASK 16 - UNIQUE CUSTOMERS")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

customers = set()

while line != "":
    parts = line.strip().split(",")
    customer_name = parts[2]
    customers.add(customer_name)
    line = file.readline()

file.close()

print("Unique customers:", len(customers))
print()


# -----------------------------
# Task 17 - Top Customer
# -----------------------------
print("TASK 17 - TOP CUSTOMER")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

customer_qty = {}

while line != "":
    parts = line.strip().split(",")
    customer_name = parts[2]
    qty = int(parts[5])

    if customer_name not in customer_qty:
        customer_qty[customer_name] = 0

    customer_qty[customer_name] += qty

    line = file.readline()

file.close()

top_customer = ""
top_customer_qty = 0

for customer in customer_qty:
    if customer_qty[customer] > top_customer_qty:
        top_customer_qty = customer_qty[customer]
        top_customer = customer

print("Top customer:", top_customer)
print("Items purchased:", top_customer_qty)
print()


# -----------------------------
# Task 18 - Student Leaderboard
# -----------------------------
print("TASK 18 - STUDENT LEADERBOARD")

leaderboard = []

for student in student_revenue:
    leaderboard.append((student_revenue[student], student))

leaderboard.sort(reverse=True)

rank = 1
for revenue, student in leaderboard:
    print(str(rank) + ".", student, "- $" + format(revenue, ".2f"))
    rank += 1

print()


# -----------------------------
# Task 19 - Data Validation
# -----------------------------
print("TASK 19 - DATA VALIDATION")
file = open("sales.csv", "r")

line = file.readline()   # skip header
line = file.readline()

issues_found = 0

while line != "":
    parts = line.strip().split(",")

    sale_id = parts[0]
    product_name = parts[4]
    qty = int(parts[5])

    if product_name not in product_prices:
        print("Invalid product on sale", sale_id + ":", product_name)
        issues_found += 1

    if qty <= 0:
        print("Invalid quantity on sale", sale_id + ":", qty)
        issues_found += 1

    line = file.readline()

file.close()

if issues_found == 0:
    print("No issues found.")
print()


# -----------------------------
# Task 20 - Write Summary File
# -----------------------------
print("TASK 20 - WRITE SUMMARY FILE")

out_file = open("student_totals.csv", "w")
out_file.write("student_name,total_items,total_revenue\n")

for student in student_qty:
    total_items = student_qty[student]
    total_revenue_value = student_revenue[student]

    out_file.write(student + "," + str(total_items) + "," + format(total_revenue_value, ".2f") + "\n")

out_file.close()

print("student_totals.csv written successfully.")
```

---

## Example Output Format

Your exact numbers will depend on your files, but the output might look something like this:

```text
>>> %Run candy_sales_full_solution.py
TASK 1 - PRODUCTS
Chocolate Bar 1.5
Gummy Bears 1.25
Sour Worms 1.25
Lollipops 0.75
Caramel Chews 1.0
Peanut Butter Cups 1.5
Jelly Beans 1.25
Sugar Blasts 1.5
Licorice Twists 1.0
Toffee Bites 1.75
Candy Corn 1.25

TASK 2 - FIRST 10 SALES
1 Ava Johnson Liam Carter Chocolate Bar 3
2 Noah Smith Emma Davis Gummy Bears 2
3 Olivia Miller Mason Hall Sour Worms 5
4 Ethan Brown Sophia Green Lollipops 4
5 Isabella Davis James Young Caramel Chews 2
6 Lucas Wilson Mia Baker Peanut Butter Cups 3
7 Mia Taylor Mia Baker Jelly Beans 1
8 Mason Anderson Charlotte Nelson Licorice Twists 2
9 Charlotte Thomas Elijah Hill Toffee Bites 4
10 Amelia Moore Amelia Scott Candy Corn 3

TASK 3 - TOTAL SALES TRANSACTIONS
Total sales transactions: 100

TASK 4 - TOTAL QUANTITY SOLD
Total quantity sold: 306

TASK 5 - UNIQUE STUDENTS
Ava Johnson
Noah Smith
Olivia Miller
Ethan Brown
Isabella Davis
Lucas Wilson
Mia Taylor
Mason Anderson
Charlotte Thomas
Amelia Moore
Harper Jackson
James Martin
Total unique students: 12

TASK 6 - SALES PER STUDENT
Ava Johnson : 30
Noah Smith : 28
Olivia Miller : 29
Ethan Brown : 26
Isabella Davis : 20
Lucas Wilson : 22
Mia Taylor : 26
Mason Anderson : 24
Charlotte Thomas : 30
Amelia Moore : 24
Harper Jackson : 31
James Martin : 16

TASK 7 - SALES PER PRODUCT
Chocolate Bar : 33
Gummy Bears : 32
Sour Worms : 30
Lollipops : 34
Caramel Chews : 30
Peanut Butter Cups : 29
Jelly Beans : 28
Licorice Twists : 28
Toffee Bites : 29
Candy Corn : 31
Sour Bears : 1
Lemon Drops : 1

TASK 8 - MOST POPULAR PRODUCT
Lollipops 34

TASK 9 - PRODUCT LOOKUP
{'Chocolate Bar': 1.5, 'Gummy Bears': 1.25, 'Sour Worms': 1.25, 'Lollipops': 0.75, 'Caramel Chews': 1.0, 'Peanut Butter Cups': 1.5, 'Jelly Beans': 1.25, 'Sugar Blasts': 1.5, 'Licorice Twists': 1.0, 'Toffee Bites': 1.75, 'Candy Corn': 1.25}

TASK 10 - TOTAL REVENUE
Error: missing product Sour Bears
Error: missing product Lemon Drops
Total revenue: 378.5

TASK 11 - REVENUE PER PRODUCT
Error: missing product Sour Bears
Error: missing product Lemon Drops
Chocolate Bar 49.5
Gummy Bears 40.0
Sour Worms 37.5
Lollipops 25.5
Caramel Chews 30.0
Peanut Butter Cups 43.5
Jelly Beans 35.0
Licorice Twists 28.0
Toffee Bites 50.75
Candy Corn 38.75

TASK 12 - REVENUE PER STUDENT
Error: missing product Sour Bears
Error: missing product Lemon Drops
Ava Johnson 38.75
Noah Smith 30.25
Olivia Miller 39.0
Ethan Brown 30.75
Isabella Davis 26.5
Lucas Wilson 25.25
Mia Taylor 36.0
Mason Anderson 28.5
Charlotte Thomas 42.0
Amelia Moore 26.75
Harper Jackson 34.25
James Martin 20.5

TASK 13 - TOP STUDENT
Charlotte Thomas 42.0

TASK 14 - HIGHEST SALE
Error: missing product Sour Bears
Error: missing product Lemon Drops
Charlotte Thomas Chocolate Bar 6 9.0

TASK 15 - AVERAGE SALE
3.785

TASK 16 - UNIQUE CUSTOMERS
Unique customers: 98

TASK 17 - TOP CUSTOMER
Charlotte Nelson 7

TASK 18 - LEADERBOARD
Charlotte Thomas 42.0
Olivia Miller 39.0
Ava Johnson 38.75
Mia Taylor 36.0
Harper Jackson 34.25
Ethan Brown 30.75
Noah Smith 30.25
Mason Anderson 28.5
Amelia Moore 26.75
Isabella Davis 26.5
Lucas Wilson 25.25
James Martin 20.5

TASK 19 - VALIDATION
Error: Missing Product: Sour Bears
Error: Missing Product: Lemon Drops

TASK 20 - WRITE FILE
File written.
>>> 
```

---

## Example `student_totals.csv`

```text
student_name,total_items,total_revenue
Ava Johnson,42,71.25
Noah Miller,31,56.50
Mia Wilson,27,48.75
Liam Taylor,25,43.00
Emma Thomas,22,38.50
```

---

## Notes for Students

* `readline()` reads one line at a time.
* `strip()` removes the newline character.
* `split(",")` separates the line into pieces.
* Dictionaries are useful for totals and lookups.
* Sets are useful for counting unique names.

---

