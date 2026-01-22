# Cgpa-Calculator
A simple CGPA calculator for my SEN Assignment.

README: CGPA CALCULATOR SOFTWARE DOCUMENTATION

Name: Oluwarotimi Agunloye David Funso
MATRIC NO: 25/17788

PROJECT DESCRIPTION
This project is a terminal-based application designed to 
help students calculate their Grade 
Point Average (CGPA). Automating the process of 
converting numerical scores into grade points and 
determining the final academic classification.


2. SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)

PHASE 1: REQUIREMENTS ANALYSIS
The primary objective was to create a tool that:
- Captures course details (Code, Units, Scores).
- Validates user input to prevent runtime errors.
- Applies standard 5.0 grading scale logic.
- Displays a formatted summary table.

PHASE 2: SYSTEM DESIGN
The system was designed with a function to handle grading thresholds (70+=A, 60-69=B, etc.), Logic to compute weighted points 
  using the formula: (Units * Points) and a clean CLI design 
  using string padding for tabular alignment.

PHASE 3: IMPLEMENTATION
Key coding techniques used include 'try-except' blocks to catch ValueErrors when users input non-numeric data. I also made use of Lists to store and iterate through multiple course entries and by using f-strings to limit decimal places to 2 for the final CGPA.

PHASE 4: TESTING
I validated the program by entering a sample result from a past year, entering known scores to verify the 
  CGPA matches manual calculations and entering 'abc' as a score to ensure the handles errors properly.

PHASE 5: DEPLOYMENT
The script is packaged as a portable .py file. It requires 
no external libraries, making it compatible with any 
standard Python environment.


How To Use
1. Open a terminal or command prompt.
2. Navigate to the folder containing the file.
3. Run: python Calculator.py
4. Follow the prompts to enter your data.

GRADING REFERENCE
70 - 100   A    5
60 - 69    B    4
50 - 59    C    3
45 - 49    D    2
40 - 44    E    1
0  - 39    F    0
