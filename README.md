🧠 Python Quiz Application

A command-line based Quiz Application developed using Python. This application allows users to participate in a multiple-choice quiz, answer randomly selected questions, track their scores, and review incorrect answers at the end of the quiz.

The application uses Python's built-in "random" module to shuffle and select questions, making each quiz attempt more interesting.

---

🚀 Project Overview

The Python Quiz Application is designed to test users' knowledge through multiple-choice questions.

Users can enter their names, answer five randomly selected questions, and receive their final score and percentage. The application also displays incorrectly answered questions along with the correct answers.

Additionally, users' scores are stored in a text file for future reference.

✨ Features

- User Name Input: Allows users to enter their name before starting the quiz.
- Random Question Selection: Randomly selects five questions from the question bank.
- Question Shuffling: Shuffles the questions to provide a different order.
- Multiple Choice Questions: Provides four options (A, B, C, D) for each question.
- Answer Validation: Checks whether the entered option is valid.
- Score Calculation: Calculates the number of correct and incorrect answers.
- Percentage Calculation: Displays the final score as a percentage.
- Wrong Answer Review: Displays incorrectly answered questions and their correct answers.
- Score Storage: Saves users' scores in a text file.

🛠️ Technologies Used

Technology| Purpose
Python| Core programming language
Random Module| Shuffle and select random questions
File Handling| Read questions and save scores
OOP| Organize quiz functionality using a class
Lists| Store questions and wrong answers
Tuples| Store incorrectly answered question details
Loops| Display questions and validate answers
Conditional Statements| Check answers and calculate results

📂 Project Structure

Python-Quiz-Application/
│
├── quiz.py
│
├── questions.txt
│
├── scores.txt
│
└── README.md

File Description

- "quiz.py" – Main Python program containing the quiz logic.
- "questions.txt" – Contains the multiple-choice questions and correct answers.
- "scores.txt" – Stores the names and scores of quiz participants.
- "README.md" – Project documentation.

⚙️ Installation and Setup

Step 1: Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Navigate to the Project Folder

cd Python-Quiz-Application

Step 3: Run the Application

python quiz.py

Requirements

- Python 3.8 or above.
- VS Code or any Python-supported IDE.
- No external libraries are required.

📝 Question File Format

Questions are stored in "questions.txt".

Each question follows this format:

Question,Option A,Option B,Option C,Option D,Correct Answer

Example:

What is the capital of India?,Mumbai,Delhi,Chennai,Kolkata,B
Which language is used for data science?,HTML,Python,CSS,PHP,B

Note: Each question must contain exactly six comma-separated fields, and the correct answer must be A, B, C, or D.

💻 Application Workflow

1. The user enters their name.
2. The application reads questions from "questions.txt".
3. Questions are shuffled randomly.
4. Five questions are selected for the quiz.
5. The user answers each question by selecting A, B, C, or D.
6. The application validates the answer.
7. The score is updated based on correct answers.
8. Incorrect answers are stored for review.
9. The final score and percentage are displayed.
10. The score is saved in "scores.txt".

📸 Sample Output

1. Starting the Quiz

Enter your name: Sona

1. What is the capital of India?
A. Mumbai
B. Delhi
C. Chennai
D. Kolkata

Enter your answer (A/B/C/D): B

Correct Answer!!!
Question 1 of 5
Current score: 1

2. Final Result

Name: Sona
Correct Answers: 4 / 5
Wrong answers: 1 / 5
Percentage: 80.0 %

3. Wrong Answer Review

Questions answered incorrectly:

Question: Which language is used for data science?
Your answer: A
Correct answer: B

4. Score Storage

Scores are stored in "scores.txt" in the following format:

Sona - 4/5

🧠 Python Concepts Implemented

This project demonstrates the practical use of:

1. Object-Oriented Programming: Creating a class and objects.
2. Constructor: Initializing variables using "__init__()".
3. Functions and Methods: Organizing different quiz operations.
4. Lists: Storing questions and incorrect answers.
5. Tuples: Grouping question and user answer details.
6. File Handling: Reading questions and writing scores.
7. Random Module: Shuffling and selecting questions randomly.
8. Loops: Iterating through questions and validating inputs.
9. Conditional Statements: Checking correct and incorrect answers.
10. String Methods: Using "strip()", "split()" and "upper()".
11. Exception-free Input Validation: Preventing invalid answer options from being accepted.

📊 Scoring System

The quiz contains five questions.

Result| Calculation
Total Questions| 5
Correct Answers| Based on user responses
Wrong Answers| Total questions − correct answers
Percentage| (Score / Total Questions) × 100

🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Developing an interactive Python application.
- Understanding Object-Oriented Programming.
- Working with external text files.
- Implementing random question selection.
- Managing user inputs and answers.
- Calculating scores and percentages.
- Tracking and reviewing incorrect answers.
- Storing results using file handling.

🔮 Future Enhancements

Possible improvements for future versions:

- Add a graphical user interface using Tkinter.
- Add different quiz categories.
- Include difficulty levels.
- Add a timer for each question.
- Create a leaderboard.
- Store scores using SQLite or MySQL.
- Allow users to choose the number of questions.

👩‍💻 Developed By

Sona V O

Python Developer Intern

🙏 Acknowledgement

This project was developed as part of my Python Developer Internship at Cognorise Info Tech.

I am thankful for this opportunity to strengthen my Python programming skills and gain practical experience through project development.

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback!
