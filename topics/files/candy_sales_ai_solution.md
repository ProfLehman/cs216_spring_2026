
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

See [`candy_sales_full_solutuion.py`](.candy_sales_full_solution.py)

---

## Sample Output

Your exact numbers will depend on your files:

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
* Sets (although not used in the sample solution) could be useful for counting unique names.

---

