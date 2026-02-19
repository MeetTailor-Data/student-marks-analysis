# Student Marks Analysis Using Pandas (Python)

## Project Description

The Student Marks Analysis project is a Python application that uses the Pandas library to analyze students' academic performance across multiple subjects.
The program performs structured DataFrame operations to calculate total marks, percentage scores, identify high-performing students, detect failed students, and sort results based on overall performance.

This project demonstrates practical tabular data analysis using Pandas and is suitable for beginners learning data analysis and academic performance evaluation in Python.

The application executes once and displays all computed results in the terminal.

---

## Features

* Store student data using a Pandas DataFrame
* Calculate total marks per student
* Calculate percentage per student
* Filter students scoring above a defined threshold
* Sort students by percentage
* Identify students who failed in any subject
* Display final processed DataFrame

---

## Concepts Used

### Python Fundamentals

* Variables
* Data structures (dictionary, list)
* Basic arithmetic operations
* Output display

### Pandas Concepts

* DataFrame creation
* Column-wise operations
* Row-wise aggregation using sum()
* Conditional filtering
* Logical operators (OR condition)
* Sorting using sort_values()
* Data selection and indexing

### Programming Concepts

* Academic performance analysis
* Tabular data processing
* Statistical calculation (total and percentage)
* Performance classification
* Data filtering and ranking

---

## Project Structure

```
student-marks-analysis/
│
├── student_analysis.py
└── README.md
```

---

## How to Run the Program

### Requirements

* Python 3.x installed on the system
* Pandas library installed

### Steps

1. Open terminal or command prompt
2. Navigate to the project directory
3. Run the following command:

```
python student_analysis.py
```

---

## Operations Performed

```
1. Display original student DataFrame
2. Calculate total marks per student
3. Calculate percentage per student
4. Filter students with percentage > 75
5. Sort students by percentage (descending)
6. Identify students who failed in any subject (marks < 40)
7. Display final DataFrame with added columns
```

---

## Sample Output

```
Students with Percentage > 75:
A, C

Failed Students:
D

Top Performer:
C
```

---

## Edge Cases Handled

* Accurate row-wise total calculation
* Correct percentage computation
* Proper filtering using multiple subject conditions
* Identification of failure based on any subject below threshold
* Consistent sorting without modifying original data unintentionally

---

## Author

Meet Tailor

Python Programming Learner

---

## License

This project is created for learning and educational purposes only.

---

## Project Status

Completed

Last Updated: 2026
