# CS 216 Exam #3 Review Topics and Problems

Review:
- Chapter 10 (Dictionaries)
- Chapters 12–13 (Files)
- Sample code on GitHub
- Program assignments

You may use a **1-page front/back help guide** (8.5" x 11" or A4 paper).

The exam will be taken online using **Respondus Browser**. Requires web camera.

---

# Review Topics

## Dictionaries

Be able to:

- Create and initialize a dictionary:
  - `dict = {}`
- Add items:
  - `dict[key] = value`
- Check whether a key exists:
  - `dict.get(key)`
  - `dict.get(key, -1)`
  - `key in dict`
- Remove items:
  - `dict.pop(key)`
- Retrieve values:
  - `dict[key]`
  - `dict.get(key)`
- Loop through keys and values:
  - `for key in dict:`
  - `for key, value in dict.items():`

---

## Files

Be able to:

- Read from a text file with one item per line
- Read from a `.csv` file and process each line
- Skip the first line (header) in a `.csv` file
- Use:
  - `readline()`
  - `split(",")`
  - `strip()`
- Open files for reading and writing:
  - `file = open("file", "r")`
  - `file = open("file", "w")`
- Write text files (one item per line)
- Write `.csv` files (multiple values separated by commas)

**Note:** You may use (but are not required to use) the `csv.reader` and `csv.writer` modules.

---

# Dictionary Review Questions

## Part 1 – Creating and Adding Data

1. Create an empty dictionary called `student_scores`.

2. Add the following students and scores:
   - Alice → 95
   - Bob → 88
   - Carlos → 91

3. Display the full dictionary.

---

## Part 2 – Accessing Values

4. Print Alice’s score using dictionary indexing.

5. Print Bob’s score using `get()`.

6. Try printing Diana’s score using:
   - `student_scores["Diana"]`
   - `student_scores.get("Diana")`

   Explain what happens in each case.

7. Use `student_scores.get("Diana", -1)` and print the result.

---

## Part 3 – Checking for Keys

8. Write an `if` statement to check whether `"Carlos"` is in the dictionary.
   - If found, print: `"Carlos is in the dictionary"`.

9. Write an `if` statement to check whether `"Eli"` is in the dictionary.
   - If not found, print: `"Eli is not in the dictionary"`.

---

## Part 4 – Updating and Removing Data

10. Change Bob’s score to 92.

11. Add Diana with a score of 85.

12. Remove Alice from the dictionary using `pop()`.

13. Display the updated dictionary.

---

## Part 5 – Looping Through a Dictionary

14. Use a loop to print only the student names.

15. Use a loop to print only the scores.

16. Use `.items()` to print results like:
   - `Alice scored 95`

17. Write a loop to find and display the highest score.

---

## Part 6 – Challenge

18. Create a dictionary called `inventory` with at least 5 items and quantities.
   - Example: `"apples": 10`

19. Write code to:
   - Add a new item
   - Update an existing item
   - Remove an item
   - Print all items and quantities

---

# File Review Questions

## Part 1 – Reading a Text File

20. Write code to open a file called `names.txt` for reading.

21. Write code to read and display the first line from `names.txt`.

22. Write code to use a loop to read and display all names in the file.
   - Assume one name per line.

23. Explain why `strip()` is useful when reading lines from a file.

---

## Part 2 – Reading a CSV File

24. Suppose a file called `grades.csv` contains:

```csv
name,score
Alice,95
Bob,88
Carlos,91
````

25. Write code to:

* Open the file
* Skip the first line (header)
* Read each remaining line
* Split each line by commas
* Display each student’s name and score

26. What does `split(",")` do?

27. Why is it often helpful to skip the first line in a CSV file?

---

## Part 3 – Processing CSV Data

28. Write code to count how many student records are in `grades.csv` (not counting the header).

29. Write code to calculate the total of all scores.

30. Write code to find the highest score.

31. Write code to count how many students scored 90 or higher.

---

## Part 4 – Writing to a Text File

32. Write code to create a file called `output.txt` and write these lines:

* Hello
* Welcome to Python
* File practice is useful

33. Why should you add `"\n"` when writing lines to a text file?

---

## Part 5 – Writing to a CSV File

34. Write code to create a file called `report.csv` and write:

```csv
name,score
Alice,95
Bob,88
```

35. Write code to write a list of names and scores to a CSV file using a loop.

---

## Part 6 – File Concepts

36. Explain the difference between:

* `"r"` mode
* `"w"` mode

37. What happens if you open a file in `"w"` mode and the file already exists?

-- end --