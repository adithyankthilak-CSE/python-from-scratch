questions = (
    "Who is the Prime Minister of India?",
    "What is the capital of Karnataka?",
    "Which company developed ChatGPT?",
    "Which sport is Virat Kohli famous for?",
    "Which Indian city is known as the Silicon Valley of India?",
    "Which programming language are you learning now?",
    "Which festival is known as the Festival of Lights?",
    "Which payment app was developed by NPCI?",
    "What does IPL stand for?",
    "Which state is known as God's Own Country?"
)

options = (
    ("a. Narendra Modi", "b. Rahul Gandhi", "c. Amit Shah", "d. Yogi Adityanath"),
    ("a. Mysuru", "b. Bengaluru", "c. Mangaluru", "d. Hubballi"),
    ("a. Google", "b. Microsoft", "c. OpenAI", "d. Apple"),
    ("a. Football", "b. Cricket", "c. Tennis", "d. Hockey"),
    ("a. Hyderabad", "b. Pune", "c. Bengaluru", "d. Chennai"),
    ("a. Java", "b. Python", "c. C++", "d. Swift"),
    ("a. Holi", "b. Diwali", "c. Onam", "d. Pongal"),
    ("a. Paytm", "b. PhonePe", "c. BHIM", "d. Google Pay"),
    ("a. Indian Premier League", "b. International Premier League", "c. Indian Players League", "d. India Premier League"),
    ("a. Kerala", "b. Goa", "c. Tamil Nadu", "d. Karnataka")
)

answers = ("a", "b", "c", "b", "c", "b", "b", "c", "a", "a")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (a, b, c, d): ").lower()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("✅ Correct!")
    else:
        print("❌ Incorrect!")
        print(f"The correct answer is {answers[question_num]}.")

    question_num += 1

print("----------- RESULT -----------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")

print("\nGuesses: ", end="")
for guess in guesses:
    print(guess, end=" ")

print()

score = int((score / len(questions)) * 100)
print(f"\nYour score: {score}%")