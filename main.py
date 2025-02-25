# timed quiz

import time

quiz = {
    "What is the capital of France?": "Paris",
    "What is a traditional serving size of an Italian espresso?": "1 oz",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the primary ingredient in traditional French béchamel sauce?": "Milk",
    "How many bones are there in the adult human body?": 206,
    "What does the Yoga term \'Pranayama\' refer to?": "Breathing exercises",
    "Which spice is known as \"queen of spices\"?": "Cardamom",
    "Which breed of dog is known for its excellent sense of smell and tracking abilities?": "Bloodhound",
}

score = 0
wrong = 0
input("Press enter to start the quiz")
print("-----------------------------------")

start_time = time.time()

for index , (question, answer) in enumerate(quiz.items(), start=1):
    user_ans = input(f"{index}. " + question + " " + "\n")

    if str(user_ans).lower() == str(answer).lower():
        score += 1
        print("Correct! \n")
    else:
        wrong += 1
        print("Incorrect. " + "The correct answer is: " + str(answer) + "\n")


end_time = time.time()

total_time = round(end_time - start_time, 2)
total_wrong_ans = wrong
total_correct_ans = score

print("-----------------------------------")
print("Total time taken: " + str(total_time) + " seconds")
print("Total correct answers: " + str(total_correct_ans))
print("Total wrong answers: " + str(total_wrong_ans))
print("-----------------------------------")
print("Score: " + str(score) + "/" + str(len(quiz)))
