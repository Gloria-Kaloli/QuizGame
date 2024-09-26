from flask import Flask, request, jsonify
from models import User, Quiz
from extensions import db
import random

def init_routes(app):
    @app.route("/quiz", methods=["GET"])
    def get_quiz():
        """
        Get a subset of quiz questions, including the correct answers and 2 wrong answers for multiple-choice mode.
        """
        num_questions = 5  # Number of questions to return

        # Get all questions from the database
        all_questions = Quiz.query.all()

        # Randomly select a subset of questions
        selected_questions = random.sample(all_questions, min(num_questions, len(all_questions)))

        # Prepare the quiz data
        quiz_data = []
        for q in selected_questions:
            # Determine choices for multiple-choice questions
            choices = [q.correct_answer]  # Start with the correct answer

            # Add dummy incorrect answers
            incorrect_answers = Quiz.query.filter(Quiz.id != q.id).limit(2).all()
            for wrong in incorrect_answers:
                choices.append(wrong.correct_answer)

            random.shuffle(choices)  # Shuffle the choices

            quiz_data.append({
                "id": q.id,
                "text": q.text,
                "choices": choices,  # Multiple choice answers
                "correct_answer": q.correct_answer  # Include correct answer for validation purposes
            })

        return jsonify(quiz_data)

    @app.route("/submit", methods=["POST"])
    def submit_answers():
        """
        Handle quiz answer submission from the user.
        """
        data = request.json
        if not all(k in data for k in ("username", "answers")):
            return jsonify({"error": "Missing fields"}), 400

        # Check if the user exists, if not, create a new one
        user = User.query.filter_by(username=data["username"]).first()
        if not user:
            user = User(username=data["username"], score=0)
            db.session.add(user)

        # Calculate the user's score based on their submitted answers
        score = 0
        for answer in data["answers"]:
            quiz = Quiz.query.get(answer["question_id"])
            if quiz and quiz.correct_answer.lower() == answer["answer"].lower():
                score += 1

        # Update the user's score
        user.score = score
        db.session.commit()

        return jsonify({"score": user.score})

    @app.route("/answers", methods=["GET"])
    def show_answers():
        """
        Get and display the correct answers for all questions.
        """
        all_questions = Quiz.query.all()
        response = []
        for question in all_questions:
            response.append({
                "id": question.id,
                "text": question.text,
                "correct_answer": question.correct_answer or "No correct answer available"
            })

        return jsonify(response)

# Initialize the Flask app and routes
app = Flask(__name__)
init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)

