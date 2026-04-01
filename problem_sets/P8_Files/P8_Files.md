# CS216 – Software Development

**P8 Assignment: Counting Chapel Attendance**  
**30 points**  
**Due: 5:00 pm, April 8, 2026**  

---

## Objective

Write a Python program that:

1. Reads data from two CSV files:  
   - `student.csv`: list of all students (`student_id`, `student_name`)  
   - `attendance.csv`: records of who attended each chapel (`chapel_id`, `student_id`)  

2. Computes how many times each student attended chapel.

3. Writes the result to a file named `report.csv` in following format:

```
student_id, student_name, total_attended
S111, Alice Anderson, 3
S112, Barnaby Brown, 2
...
```

---

- Your code must use the techniques for readings CSV files demonstrated in-class. 
- You can assume each student attendance record is unique ie. no duplicate records
- Your code must work for any valid student.csv and attendance.csv files using the formats shown. 
- You can assume there will be at least one student and one attendance record.

## Steps & Hints

1. Open and read `student.csv`. Store each student’s name in a dictionary with `student_id` as the key.
2. Open and read `attendance.csv`. Count how many times each `student_id` appears using a dictionary.
3. Combine the two dictionaries and write the results to `report.csv`.

---

## Submitting your assignment

Host your code on GitHub and upload links.

1.Your Python program file (e.g., `chapel_report.py`)

2.Your generated report file `report.csv` using `student.csv` and `attendance.csv`

---

-- end --


