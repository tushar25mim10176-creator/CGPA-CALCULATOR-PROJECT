CGPA CALCULATOR – README

What this program does
This program helps you calculate your CGPA (Cumulative Grade Point Average).
You enter how many subjects you have, then for each subject you enter the grade point and the credit.
The program calculates your overall CGPA and an approximate percentage.

Files

cgpa_calculator.py → Python program that calculates CGPA.

Requirements

Python 3 installed on your computer.

Basic details of your subjects:

Grade point for each subject (for example: 10, 9, 8, 7, etc.).

Credit for each subject (for example: 2, 3, 4, etc.).

How to run the program
Step 1: Save the code in a file named cgpa_calculator.py.
Step 2: Open the folder that contains cgpa_calculator.py.

On Windows:

Click in the address bar of the folder, type cmd and press Enter.

In the black window (Command Prompt), type:
python cgpa_calculator.py
and press Enter.

On Mac / Linux:

Open Terminal.

Use cd to go to the folder where cgpa_calculator.py is saved.

Run:
python3 cgpa_calculator.py

What you will be asked
The program will ask you:

“Enter the number of subjects:”
Type a number (for example, 5) and press Enter.

For each subject, you will see:

“Enter grade point (e.g., 10, 9, 8):”
Type the grade point you got in that subject.

“Enter credit for this subject:”
Type the credit of that subject.

You repeat this until all subjects are entered.

How the calculation works (simple explanation)

For each subject, the program multiplies:
grade point × credit.

It adds all these values for all subjects.

It also adds all the credits.

CGPA = (total of grade point × credit) ÷ (total credits).

The program also multiplies the CGPA by 9.5 to show an approximate percentage
(you can change this number in the code if your board uses a different rule).

Example of final output (sample)
RESULT
Total subjects: 5
Total credits: 20.0
Your CGPA: 8.25
Approx. percentage: 78.38%

Customizing the program
You can edit cgpa_calculator.py to:

Change how percentage is calculated.

Remove percentage if you only need CGPA.

Add checks so that grade points stay in a valid range (for example, between 0 and 10).