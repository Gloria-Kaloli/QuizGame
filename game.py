import requests
import tkinter as tk
from tkinter import messagebox, simpledialog

# Main Menu Function
def main_menu():
    root = tk.Tk()
    root.title("Quiz Game Menu")
    root.geometry("300x200")

    tk.Label(root, text="Welcome to the Quiz Game!").pack(pady=10)

    # Button for Text Entry Quiz
    tk.Button(root, text="Start Text Entry Quiz", command=lambda: start_quiz('text_entry', root)).pack(pady=10)

    # Button for Multiple Choice Quiz
    tk.Button(root, text="Start Multiple Choice Quiz", command=lambda: start_quiz('multiple_choice', root)).pack(pady=10)

    root.mainloop()

# Start the selected quiz type (Text Entry or Multiple Choice)
def start_quiz(quiz_type, root):
    root.destroy()  # Close the menu window
    questions = fetch_questions()
    
    if not questions:
        messagebox.showerror("Error", "Failed to load questions.")
        return

    if quiz_type == 'text_entry':
        display_text_entry_questions(questions)
    else:
        display_multiple_choice_questions(questions)

# Fetch questions from the server
def fetch_questions():
    try:
        response = requests.get('http://127.0.0.1:5000/quiz')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching questions: {e}")
        return []

# Display the text entry questions
def display_text_entry_questions(questions):
    root = tk.Tk()
    root.title("Text Entry Quiz")
    root.geometry("900x600")

    user_answers = []
    for question in questions:
        answer = simpledialog.askstring("Quiz", question['text'], parent=root)
        if answer is not None:
            user_answers.append({"question_id": question['id'], "answer": answer})

    tk.Button(root, text="Submit", command=lambda: submit_answers(user_answers, root)).pack(pady=20)
    root.mainloop()

# Display multiple choice questions
def display_multiple_choice_questions(questions):
    root = tk.Tk()
    root.title("Multiple Choice Quiz")
    root.geometry("900x600")

    user_answers = []

    for question in questions:
        frame = tk.Frame(root)
        frame.pack(pady=10)

        # Display question text
        tk.Label(frame, text=question.get('text', 'No question text'), wraplength=600).pack()

        # Check if 'choices' key exists and is not empty
        if 'choices' not in question or not question['choices']:
            tk.Label(frame, text="No choices available for this question.", fg="red").pack()
            continue

        # Create radio buttons for the choices
        selected_answer = tk.StringVar()
        for option in question['choices']:
            tk.Radiobutton(frame, text=option, variable=selected_answer, value=option).pack(anchor=tk.W)

        user_answers.append({"question_id": question['id'], "answer_var": selected_answer})

    # Submit button
    tk.Button(root, text="Submit", command=lambda: submit_answers(user_answers, root)).pack(pady=20)

    root.mainloop()

# Submit answers to the server
def submit_answers(user_answers, root):
    final_answers = []
    for answer in user_answers:
        # Handle both text entry and multiple choice
        if 'answer_var' in answer:  # Multiple choice
            selected_answer = answer['answer_var'].get()
            if selected_answer:  # Only add answers that were selected
                final_answers.append({"question_id": answer['question_id'], "answer": selected_answer})
        else:  # Text entry
            final_answers.append(answer)

    try:
        response = requests.post('http://127.0.0.1:5000/submit', json={"username": "user", "answers": final_answers})
        response.raise_for_status()

        result = response.json()
        score = result.get('score', 0)
        
        # Show the score
        messagebox.showinfo("Quiz Result", f"Your score: {score}")

        root.destroy()  # Close the quiz window
        display_correct_answers(final_answers)  # Display the correct answers

    except requests.RequestException as e:
        print(f"Error submitting answers: {e}")
        messagebox.showerror("Error", "Failed to submit answers.")

# Display correct answers and score in a new window
def display_correct_answers(user_answers):
    correct_answers = fetch_correct_answers()

    result_window = tk.Tk()
    result_window.title("Correct Answers")
    result_window.geometry("600x500")

    text_widget = tk.Text(result_window, wrap=tk.WORD)
    text_widget.pack(expand=True, fill=tk.BOTH)

    # Display correct answers
    for answer in correct_answers:
        question_text = answer.get('text', 'No question text available')
        correct_answer = answer.get('correct_answer', 'No correct answer available')
        text_widget.insert(tk.END, f"Question: {question_text}\nCorrect Answer: {correct_answer}\n\n")

    text_widget.config(state=tk.DISABLED)

    # Replay prompt when closing the correct answers window
    result_window.protocol("WM_DELETE_WINDOW", lambda: ask_replay(result_window))

# Fetch correct answers from the server
def fetch_correct_answers():
    try:
        response = requests.get('http://127.0.0.1:5000/answers')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching correct answers: {e}")
        return []

# Ask the user if they want to replay when closing the result window
def ask_replay(window):
    if messagebox.askyesno("Replay", "Do you want to play again?"):
        window.destroy()
        main_menu()  # Start the main menu again
    else:
        window.destroy()

if __name__ == "__main__":
    main_menu()

