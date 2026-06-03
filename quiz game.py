print("QUIZ TIME!")

questions = ("how many notes in the key of  C major are sharp?: ",
             "what is the 4th planet in the solar system?: ",
             "humans have the same number of chromosomes as: ",
             "which number is not valid in python?: ",
             "who created the first working lamp?: ")

options = (("A. 1", "B. 3", "C. 2", "D. 0"),
           ("A. venus", "B. uranus", "C. mars", "D. jupiter"),
           ("A. olive trees", "B. carrots", "C. chimpanees", "D. lions"),
           ("A. 1023", "B. 16,987", "C. 156.0", "D. 785.003"),
           ("A. joseph swan", "B. alessandro volta", "C. humphry davy", "D. thomas edison"))

answers = ("D", "C", "A", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(question)
    
    for option in options[question_num]:
        print(option)
        
    guess = input("enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!!")
    else:
        print("incorrect :(((")
        print(f"{answers[question_num]} is the answer")
    question_num += 1
    
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("RESULTS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("your guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")