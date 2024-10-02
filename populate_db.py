from app import app
from models import db, Quiz

def populate_db():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Clear existing data
        db.session.query(Quiz).delete()
        
        # Insert sample data
        questions = [
            {"text": "What is 5 + 3?", "correct_answer": "8"},
            {"text": "What is the capital of France?", "correct_answer": "Paris"},
            {"text": "What is the largest planet in our solar system?", "correct_answer": "Jupiter"},
            {"text": "What is 2 + 2?", "correct_answer": "4"},
            {"text": "Who wrote 'Hamlet'?", "correct_answer": "William Shakespeare"},
            {"text": "What is the boiling point of water?", "correct_answer": "100°C"},
            {"text": "What is the hardest natural substance on Earth?", "correct_answer": "Diamond"},
            {"text": "What is the main ingredient in guacamole?", "correct_answer": "Avocado"},
            {"text": "Who painted the Mona Lisa?", "correct_answer": "Leonardo da Vinci"},
            {"text": "What is the chemical symbol for gold?", "correct_answer": "Au"},
            {"text": "What is the smallest prime number?", "correct_answer": "2"},
            {"text": "Which gas do plants absorb from the atmosphere?", "correct_answer": "Carbon dioxide"},
            {"text": "Who discovered penicillin?", "correct_answer": "Alexander Fleming"},
            {"text": "What is the capital city of Japan?", "correct_answer": "Tokyo"},
            {"text": "In which year did the Titanic sink?", "correct_answer": "1912"},
            {"text": "What is the largest mammal in the world?", "correct_answer": "Blue whale"},
            {"text": "What is the square root of 64?", "correct_answer": "8"},
            {"text": "Which planet is known as the Red Planet?", "correct_answer": "Mars"},
            {"text": "Who is known as the father of modern physics?", "correct_answer": "Albert Einstein"},
            {"text": "What is the currency of the United States?", "correct_answer": "Dollar"},
            {"text": "What is the main language spoken in Brazil?", "correct_answer": "Portuguese"},
            {"text": "What is the longest river in the world?", "correct_answer": "Nile"},
            {"text": "Which element has the atomic number 1?", "correct_answer": "Hydrogen"},
            {"text": "What is the capital of Australia?", "correct_answer": "Canberra"},
            {"text": "What year did World War II end?", "correct_answer": "1945"},
            {"text": "Who wrote the play 'Romeo and Juliet'?", "correct_answer": "William Shakespeare"},
            {"text": "What is the tallest mountain in the world?", "correct_answer": "Mount Everest"},
            {"text": "Which planet is known for its rings?", "correct_answer": "Saturn"},
            {"text": "What is the chemical formula for table salt?", "correct_answer": "NaCl"},
            {"text": "What is the largest continent?", "correct_answer": "Asia"},
            {"text": "What is the process of converting a liquid to a gas called?", "correct_answer": "Evaporation"},
            {"text": "Who was the first person to walk on the moon?", "correct_answer": "Neil Armstrong"},
            {"text": "What is the capital city of Canada?", "correct_answer": "Ottawa"},
            {"text": "Which instrument is used to measure atmospheric pressure?", "correct_answer": "Barometer"},
            {"text": "What is the most widely spoken language in the world?", "correct_answer": "Mandarin Chinese"},
            {"text": "What is the freezing point of water?", "correct_answer": "0°C"},
            {"text": "What is the capital of France?", "correct_answer": "Paris"},
            {"text": "Who invented the telephone?", "correct_answer": "Alexander Graham Bell"},
            {"text": "What is the largest desert in the world?", "correct_answer": "Sahara"},
            {"text": "In what year did the Berlin Wall fall?", "correct_answer": "1989"},
            {"text": "What is the primary gas found in the Earth's atmosphere?", "correct_answer": "Nitrogen"},
            {"text": "Which planet is known as the Earth's twin?", "correct_answer": "Venus"},
            {"text": "What is the capital city of Italy?", "correct_answer": "Rome"},
            {"text": "Which scientist developed the theory of evolution?", "correct_answer": "Charles Darwin"},
            {"text": "What is the speed of light?", "correct_answer": "299,792 km/s"},
            {"text": "What is the most abundant element in the universe?", "correct_answer": "Hydrogen"},
            {"text": "What is the primary organ of the circulatory system?", "correct_answer": "Heart"},
            {"text": "Who wrote 'The Odyssey'?", "correct_answer": "Homer"},
            {"text": "What is the chemical symbol for water?", "correct_answer": "H2O"},
            {"text": "What is the largest organ in the human body?", "correct_answer": "Skin"},
            {"text": "What is the name of the first artificial satellite launched into space?", "correct_answer": "Sputnik"},
            {"text": "What is the longest river in South America?", "correct_answer": "Amazon"},
            {"text": "What is the main language spoken in Egypt?", "correct_answer": "Arabic"},
            {"text": "What is the capital of Egypt?", "correct_answer": "Cairo"},
            {"text": "Which animal is known as the king of the jungle?", "correct_answer": "Lion"},
            {"text": "What is the square of 7?", "correct_answer": "49"},
            {"text": "What is the main ingredient in a traditional Japanese sushi?", "correct_answer": "Rice"},
            {"text": "What is the capital city of Spain?", "correct_answer": "Madrid"},
            {"text": "What gas do humans exhale?", "correct_answer": "Carbon dioxide"},
            {"text": "What is the value of pi to two decimal places?", "correct_answer": "3.14"},
            {"text": "Which country is known as the Land of the Rising Sun?", "correct_answer": "Japan"},
            {"text": "What is the smallest country in the world?", "correct_answer": "Vatican City"},
            {"text": "What is the most populous country in the world?", "correct_answer": "China"},
            {"text": "What is the currency of the United Kingdom?", "correct_answer": "Pound Sterling"},
            {"text": "What is the capital city of Germany?", "correct_answer": "Berlin"},
            {"text": "What is the primary purpose of the internet?", "correct_answer": "Communication"},
            {"text": "What is the most widely used operating system in the world?", "correct_answer": "Windows"},
            {"text": "What is the capital of Russia?", "correct_answer": "Moscow"},
            {"text": "Who painted the ceiling of the Sistine Chapel?", "correct_answer": "Michelangelo"},
            {"text": "What is the largest ocean on Earth?", "correct_answer": "Pacific Ocean"},
            {"text": "What is the name of the first manned mission to land on the moon?", "correct_answer": "Apollo 11"},
            {"text": "What is the capital city of India?", "correct_answer": "New Delhi"},
            {"text": "Which planet has the most moons?", "correct_answer": "Jupiter"},
            {"text": "What is the name of the fairy in Peter Pan?", "correct_answer": "Tinkerbell"},
            {"text": "What is the official language of the United Nations?", "correct_answer": "English"},
            {"text": "What is the capital of Greece?", "correct_answer": "Athens"},
            {"text": "Who is known as the 'Father of Geometry'?", "correct_answer": "Euclid"},
            {"text": "What is the most consumed fruit in the world?", "correct_answer": "Banana"},
            {"text": "Which animal is known for its ability to change colors?", "correct_answer": "Chameleon"},
            {"text": "What is the chemical formula for oxygen?", "correct_answer": "O2"},
            {"text": "What is the longest running Broadway show?", "correct_answer": "The Phantom of the Opera"},
            {"text": "What is the primary function of red blood cells?", "correct_answer": "Transport oxygen"},
            {"text": "What is the capital city of Sweden?", "correct_answer": "Stockholm"},
            {"text": "What is the process by which plants make their food called?", "correct_answer": "Photosynthesis"},
            {"text": "What is the first element on the periodic table?", "correct_answer": "Hydrogen"},
            {"text": "What is the highest mountain in North America?", "correct_answer": "Denali"},
            {"text": "Which city is known as the Big Apple?", "correct_answer": "New York City"},
            {"text": "What is the most famous clock tower in London?", "correct_answer": "Big Ben"},
            {"text": "What is the currency of Japan?", "correct_answer": "Yen"},
            {"text": "What is the capital of South Africa?", "correct_answer": "Pretoria"},
            {"text": "What is the name of our galaxy?", "correct_answer": "Milky Way"}
        ]
        
        for q in questions:
            quiz = Quiz(text=q["text"], correct_answer=q["correct_answer"])
            db.session.add(quiz)
        
        db.session.commit()
        print("Database populated successfully.")

if __name__ == "__main__":
    populate_db()
