from tkinter import *
from tkinter import messagebox

window=Tk()
window.title('Login Screen')
window.geometry('400x150')

l1=Label(window,text='username:',font=(12))
l2=Label(window,text='password:',font=(12))
l1.grid(row=0,column=0,padx=5,pady=5)
l2.grid(row=1,column=0,padx=5,pady=5)

username=StringVar()
password=StringVar()
t1=Entry(window,textvariable=username,font=(12))
t2=Entry(window,textvariable=password,font=(12),show='*') #show'x'password field
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)

def login():
    if username.get()=='admin'and password.get()=='admin':
        messagebox.showinfo(title='loginstatus',message="you have logged in")
    else:
        messagebox.showerror(title='loginerror',message="username/password is incorrect")
b1=Button(window,command=login,text='login',font=(12))


def cancel():
    status=messagebox.askyesno(title='Question',message='Do you want to close the window?')
    if status==True:
            window.destroy()
    else:
        messagebox.showwarning(title='warningmessage',message='please login again!!')

b2=Button(window,command=cancel,text='cancel',font=(12))
b1.grid(row=2,column=1,sticky=W)
b2.grid(row=2,column=1,sticky=E)

window.mainloop()

import tkinter as tk
from tkinter import messagebox



class WelcomeWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome to Quiz App")
        self.master.geometry("400x300")  # Set window size

        self.create_widgets()

    def create_widgets(self):
        self.welcome_label = tk.Label(self.master, text="Welcome to Quiz App", font=("Helvetica", 18, "bold"))
        self.welcome_label.pack(pady=20)

        self.instructions_label = tk.Label(self.master,
                                           text="Instructions:\n1. Select a category.\n2. Answer the questions.\n3. Click 'Start Quiz'.",
                                           font=("Helvetica", 12))
        self.instructions_label.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=20)

    def start_quiz(self):
        # Here you can launch the quiz window
        print("Starting quiz...")


def main():
    root = tk.Tk()
    app = WelcomeWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk

class CategoryWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Category Selection")

        self.categories = ["General Knowledge", "Science", "History", "Geography"]

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Select a quiz category:")
        self.label.pack()

        self.category_var = tk.StringVar()
        self.category_var.set(self.categories[0])

        for category in self.categories:
            rb = tk.Radiobutton(self.master, text=category, variable=self.category_var, value=category)
            rb.pack(anchor="w")

        self.start_button = tk.Button(self.master, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        selected_category = self.category_var.get()
        # Here you can launch the quiz window based on the selected category
        print("Starting quiz in category:", selected_category)

def main():
    root = tk.Tk()
    app = CategoryWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    import tkinter as tk
    from tkinter import messagebox


    class QuizApp:
        def __init__(self, master):
            self.master = master
            self.master.title("Quiz App")

            self.questions = [
                {
                    "question": "The basic operations performed by a computer are?",
                    "options": ["Arithmetic operation", "Logical operation", "Storage and relative", "All the above"],
                    "answer": "All the above"
                },
                {
                    "question": " The two major types of computer chips are?",
                    "options": ["External memory chip", "Primary memory chip", "Microprocessor chip", "Both b and c"],
                    "answer": "Both b and c"
                },
                {
                    "question": "Microprocessors as switching devices are for which generation computers?",
                    "options": [" First Generation", "Second Generation", "Third Generation", "Fourth Generation"],
                    "answer": "Fourth Generation"
                },
                {
                    "question": "The brain of any computer system is?",
                    "options": ["ALU", "Memory", "CPU", "Control unit"],
                    "answer": "CPU"
                },
                {
                    "question": "Storage capacity of magnetic disk depends on?",
                    "options": ["tracks per inch of surface", "bits per inch of tracks", "disk pack in disk surface",
                                "All of above"],
                    "answer": "All of above"
                },
                {
                    "question": "The two kinds of main memory are?",
                    "options": ["Primary and secondary", "Random and sequential", "ROM and RAM", "All of above"],
                    "answer": "ROM and RAM"
                },
                {
                    "question": " Computer is free from tiresome and boardoom.We call it?",
                    "options": ["Accuracy", "Reliability", "Diligence", "Versatility"],
                    "answer": "Diligence"
                },
                {
                    "question": "CD-ROM is a?",
                    "options": ["Semiconductor memory", "Memory register", "Magnetic memory", "None of above"],
                    "answer": "None of above"
                },
                {
                    "question": "Which type of computers uses the 8-bit code called EBCDIC?",
                    "options": ["Minicomputers", "Microcomputers", "Mainframe computers", "Super computer"],
                    "answer": "Mainframe computers"
                },
                {
                    "question": " Chief component of first generation computer was?",
                    "options": ["Transistors", "Vacuum Tubes and Valves", "Integrated Circuits", "None of above"],
                    "answer": "Vacuum Tubes and Valves"
                },
            ]

            self.current_question = 0
            self.score = 0

            self.create_widgets()

        def create_widgets(self):
            self.question_label = tk.Label(self.master, text="")
            self.question_label.pack()

            self.radio_var = tk.StringVar()
            self.radio_var.set(None)

            self.radio_buttons = []
            for option in self.questions[self.current_question]["options"]:
                rb = tk.Radiobutton(self.master, text=option, variable=self.radio_var, value=option)
                rb.pack()
                self.radio_buttons.append(rb)

            self.next_button = tk.Button(self.master, text="Next", command=self.next_question)
            self.next_button.pack()

        def next_question(self):
            selected_answer = self.radio_var.get()
            correct_answer = self.questions[self.current_question]["answer"]

            if selected_answer == correct_answer:
                self.score += 1

            self.current_question += 1
            if self.current_question < len(self.questions):
                self.update_question()
            else:
                messagebox.showinfo("Quiz Completed", f"You scored {self.score}/{len(self.questions)}")
                self.master.destroy()

        def update_question(self):
            self.question_label.config(text=self.questions[self.current_question]["question"])

            for i, option in enumerate(self.questions[self.current_question]["options"]):
                self.radio_buttons[i].config(text=option, value=option)

            self.radio_var.set(None)


    def main():
        root = tk.Tk()
        app = QuizApp(root)
        root.mainloop()


    if __name__ == "__main__":
        main()


import tkinter as tk


class ThankYouWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Thank You!")

        self.create_widgets()

    def create_widgets(self):
        self.thank_you_label = tk.Label(self.master, text="Thank you for using the Quiz App!", font=("Helvetica", 16))
        self.thank_you_label.pack(padx=20, pady=30)

        self.close_button = tk.Button(self.master, text="Close", command=self.close_window)
        self.close_button.pack(pady=10)

    def close_window(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = ThankYouWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()


