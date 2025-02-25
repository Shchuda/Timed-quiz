import time

quiz = {
    "Math Quiz": {
        "What is 5 + 3?": 8,
        "What is 12 - 4?": 8,
        "What is 11 * 4": 44,
        "What is 5 * 3?": 15,
        "What is 6 / 2?": 3,
    },
    "Science Quiz": {
        "What planet is known as the Red Planet?": "Mars",
        "What is H2O commonly known as?": "Water",
        "What is the largest organ in the human body?": "Skin",
        "What is the name of the force that keeps us on the ground?": "Gravity",
        "What is the process by which plants convert sunlight to energy?": "Photosynthesis"
    },
    "Animals Quiz": {
        "What animal has the largest brain relative to body size?": "Dolphin",
        "What animal had the most powerful bite in the world?": "Nile crocodile",
        "What animal has the longest tongue?": "Giraffe",
        "How many hearts does an octopus have?": 3,
        "What is the largest mammal on Earth?": "Blue whale"
    },
    "Food and drinks Quiz": {
        "Which country drinks the most coffee per capita?": "Finland",
        "Where did sushi originate?": "Japan",
        "What is the world’s best-selling stout beer?": "Guinness",
        "Pink Ladies and Granny Smiths are types of what fruit?": "Apples",
        "Which country is credited with inventing ice cream?": "China"
    }
}

score = 0
wrong = 0

print("Choose a quiz:")
for index, category in enumerate(quiz.keys(), start=1):
    print(f"{index}. {category}")

while True:
    choice = input("\nChoose a quiz: ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(quiz):
            selected_category = list(quiz.keys())[choice - 1]
            print(f"\nYou selected: {selected_category.upper()}\n")
            break
    print("Invalid choice. Please select a valid number.")


questions = quiz[selected_category]
index = 1
input("Press enter to start the quiz\n")

start_time = time.time()

for question, answer in questions.items():
    user_ans = input(f"{index}. " + question + " " + "\n")

    if str(user_ans).lower() == str(answer).lower():
        score += 1
        print("Correct! \n")
    else:
        wrong += 1
        print("Incorrect. " + "The correct answer is: " + str(answer) + "\n")

    index += 1

end_time = time.time()

total_time = round(end_time - start_time, 2)
total_wrong_ans = wrong
total_correct_ans = score

print("-----------------------------------")
print("Total time taken: " + str(total_time) + " seconds")
print("Total correct answers: " + str(total_correct_ans))
print("Total wrong answers: " + str(total_wrong_ans))
print("-----------------------------------")
print("Score: " + str(score) + "/" + str(len(questions)))
