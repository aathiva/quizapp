import tkinter as tk
from tkinter import messagebox
import json
import random

def load_users():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}
    return users

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

def validate_login(username, password):
    users = load_users()
    if username in users and users[username] == password:
        return True
    return False

def login_window():
    def login():
        username = entry_username.get()
        password = entry_password.get()
        if validate_login(username, password):
            messagebox.showinfo("Login", "Login Successful")
            root.destroy()
            subject_selection_window(username)
        else:
            messagebox.showerror("Login", "Invalid username or password")

    root = tk.Tk()
    root.title("Login")
    
    tk.Label(root, text="Username").grid(row=0, column=0)
    tk.Label(root, text="Password").grid(row=1, column=0)
    
    entry_username = tk.Entry(root)
    entry_password = tk.Entry(root, show='*')
    
    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)
    
    tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2)
    
    root.mainloop()

def subject_selection_window(username):
    def select_subject(subject):
        root.destroy()
        quiz_window(username, subject)
    
    root = tk.Tk()
    root.title("Select Subject")
    
    subjects = ["Math", "Science", "History"]  # Example subjects
    
    tk.Label(root, text="Choose a subject").pack()
    
    for subject in subjects:
        tk.Button(root, text=subject, command=lambda s=subject: select_subject(s)).pack()
    
    root.mainloop()

def load_questions(subject):
    try:
        with open('questions.json', 'r') as file:
            questions = json.load(file)[subject]
    except FileNotFoundError:
        questions = []
    return questions

def quiz_window(username, subject):
    questions = load_questions(subject)
    if not questions:
        messagebox.showerror("Error", "No questions available for this subject")
        return
    
    random.shuffle(questions)
    current_question = [0]
    score = [0]
    
    def next_question():
        if current_question[0] < len(questions):
            question = questions[current_question[0]]
            lbl_question.config(text=question['question'])
            var_answer.set(None)
            for i, option in enumerate(question['options']):
                radio_buttons[i].config(text=option)
            current_question[0] += 1
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {score[0]}/{len(questions)}")
            root.destroy()

    def submit_answer():
        answer = var_answer.get()
        if answer == questions[current_question[0] - 1]['answer']:
            score[0] += 1
        next_question()
    
    root = tk.Tk()
    root.title("Quiz")

    lbl_question = tk.Label(root, text="")
    lbl_question.pack()

    var_answer = tk.StringVar()
    
    radio_buttons = []
    for i in range(4):
        rb = tk.Radiobutton(root, text="", variable=var_answer, value=i)
        rb.pack()
        radio_buttons.append(rb)

    tk.Button(root, text="Submit", command=submit_answer).pack()
    
    next_question()
    
    root.mainloop()

if __name__ == "__main__":
    login_window()
