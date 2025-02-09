# 2025-ITELEC2-LAB005
Week 02 - Python Variables, Operators and I/O Statements

Laboratory # 05 - Arithmetic Operators and Operator Precedence in Python

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 05 - Arithmetic Operators and Operator Precedence in Python**

   **Objective:**
   - Familiarize you with Python's arithmetic operators (+, -, *, /, %, //, **).
   - Demonstrate how Python handles operator precedence (the order in which operations are performed).
   - Show how to use parentheses to control the order of operations.

   **Desired Output:**
   
```bash
Result of a + b * c: 25
Result of (a + b) * c: 45
Result of a - b: 5
Result of a / b: 2.0
Result of a // b (floor division): 2
Result of a % b (modulus): 0
Result of a ** c (exponentiation): 1000
Result of (a + b - c) * (a / b): 24.0
```
      
   **Notable Observations (to be discussed after completing the exercise):**
   - Python follows standard operator precedence rules (like in mathematics):
      - Parentheses () have the highest precedence.
      - Exponentiation ** is performed next.
      - Multiplication *, division /, floor division //, and modulus % are performed next, from left to right.
      - Addition + and subtraction - are performed last, from left to right.
   - Parentheses can be used to group operations and force a specific order of evaluation.
   - The modulus operator % gives the remainder of a division.
   - The exponentiation operator ** raises a number to a power.
   - / performs standard division resulting in a float.
   - // performs floor division resulting in an integer (discarding the decimal part).

   **Python Best Practices**
   - Names Matter: Give your variables good names so you (and others) can understand your code.
   - Plan It Out: Break down big problems into smaller, easier steps.
   - Order Matters: Python follows rules for which operations happen first (precedence). Parentheses help you control that order.
   - Test Your Work: Check if your code does what you expect!
   - Different Divisions: / gives you decimals, // gives you whole numbers. Know the difference!
   - Practice Makes Perfect: The more you code, the better you'll get.
   
   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `exercise_03.py`
      
   2.  Define numeric variables:
       - Declare three variables named `a`, `b`, and `c`. Assign them integer values (e.g., `a = 10`, `b = 5`, `c = 3`).
         ```python
         a = 10
         b = 5
         c = 3
         ```
      
   3.  Calculate expressions without parentheses (demonstrating precedence):
      - Calculate the expression `a + b * c` and store the result in a variable named `result1`. (Multiplication before addition)
      - Print the value of `result1` with a descriptive label.
         ```python
         result1 = a + b * c
         print("Result of a + b * c:", result1)
         ```

   4. Calculate expressions with parentheses (overriding precedence):
      - Calculate the expression `(a + b) * c` and store the result in a variable named `result2`. (Addition within parentheses first)
      - Print the value of result2 with a descriptive label.
         ```python
         result2 = (a + b) * c
         print("Result of (a + b) * c:", result2)
         ```

   5. Use subtraction:
      - Calculate a - b and store the result in result3.
      - Print the value of result3 with a descriptive label.
         ```python
         result3 = a - b
         print("Result of a - b:", result3)
         ```

   6. Use standard and floor division:
      - Calculate a / b (standard division) and store the result in result4.
      - Calculate a // b (floor division) and store the result in result5.
      - Print the values of result4 and result5 with descriptive labels.
         ```python
         result4 = a / b
         result5 = a // b
         print("Result of a / b:", result4)
         print("Result of a // b (floor division):", result5)
         ```
         
   7. Use modulus and exponentiation:
      - Calculate a % b (modulus) and store the result in result6.
      - Calculate a ** c (exponentiation) and store the result in result7.
      - Print the values of result6 and result7 with descriptive labels.
         ```python
         result6 = a % b
         result7 = a ** c
         print("Result of a % b (modulus):", result6)
         print("Result of a ** c (exponentiation):", result7)
         ```
         
   8. Combine operators in a more complex expression:
      - Calculate (a + b - c) * (a / b) and store the result in result8. This combines multiple operators and parentheses.
      - Print the value of result8 with a descriptive label.
         ```python
         result8 = (a + b - c) * (a / b)
         print("Result of (a + b - c) * (a / b):", result8)
         ```

   9. Run the code: Execute your Python code.
   10. Observe the output: Compare your output with the "Desired Output" shown above.
   11. Discussion (Notable Observations): Discuss all the points in the "Notable Observations" section.  Be sure to explain the full order of operations and how each operator behaves.  Give concrete examples of when you might use each of these operators.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 02 - Session 01 - Exercise 03"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
