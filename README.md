\# Week 2 Python - Student Grade Calculator



\## Project Overview



This project is a Student Grade Calculator developed as part of Week 2 of my Python internship.



The program accepts a student's name and marks, calculates the appropriate grade, and displays an encouraging message based on the grade.



\## Objectives



\* Understand if-elif-else statements

\* Use comparison operators

\* Use functions in Python

\* Use while loops for input validation

\* Handle invalid user input using try-except

\* Practice testing and debugging



\## Grading System



| Marks    | Grade |

| -------- | ----- |

| 90 - 100 | A     |

| 80 - 89  | B     |

| 70 - 79  | C     |

| 60 - 69  | D     |

| 0 - 59   | F     |



\## Technologies Used



\* Python 3

\* Python IDLE

\* GitHub



\## Project Structure



```text

Week-2-Python/

├── README.md

├── grade\_calculator.py

├── test\_cases.txt

└── screenshots/

     ├── 01\_time\_of\_day.png

     ├── 02\_number\_guessing\_game.png

     ├── 03\_for\_loop\_1\_to\_100.png

     ├── 04\_rectangle\_area\_function.png

     ├── 05\_simple\_calculator.png

     ├── 06\_grading\_system.png

     ├── 07\_age\_categories.png

     ├── 08\_grade\_calculator\_B\_grade.png

     ├── 09\_grade\_calculator\_A\_grade.png

     ├── 10\_grade\_calculator\_invalid\_marks.png

     └── 11\_grade\_calculator\_invalid\_input.png

```



\## How to Run



1\. Install Python 3.

2\. Open `grade\_calculator.py` using Python IDLE.

3\. Press `F5` to run the program.

4\. Enter the student's name.

5\. Enter marks between 0 and 100.

6\. The program displays the grade and an encouraging message.



\## Code Structure



\### `calculate\_grade()`



This function checks the student's marks and returns the appropriate grade from A to F.



\### `get\_message()`



This function displays an encouraging message based on the calculated grade.



\### Input Validation



The program uses a `while` loop to repeatedly ask for marks until a valid value between 0 and 100 is entered.



\### Error Handling



A `try-except` block handles non-numeric inputs such as `abc`.



\## Testing



The project was tested using:



\* Valid marks such as 85 and 95

\* Marks outside the valid range such as 150

\* Non-numeric input such as `abc`



All tested cases produced the expected results.



Detailed testing information is available in `test\_cases.txt`.



\## Screenshots



Screenshots of the practice programs and Student Grade Calculator testing are available in the `screenshots` folder.



\## Learning Outcomes



Through this project, I practiced:



\* Conditional statements

\* Comparison operators

\* For loops

\* While loops

\* Functions

\* Exception handling

\* Input validation

\* Testing and debugging



\## Author



Mansi Patankar



