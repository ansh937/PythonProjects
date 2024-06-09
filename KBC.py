import os
print("Welcome to Quiz :)")
question = input("Do you want to play the game? ")

if question.lower() != "yes":
    quit()
else:
    os.system(f"say 'Lets the game begain'")
    print(f"say'Let's the game begin")

QandA = {
    "What is the highest mountain in the world? ": "Mount Everest",
    "What country has the highest life expectancy? ": "Hong Kong",
    "How many elements are in the periodic table? ": "118",
    "What’s the capital of Canada? ": "Ottawa",
    "How many time zones are there in Russia? ": "11",
    "Which football team is known as ‘The Red Devils’? ": "Manchester United"
}

score = 0
base_prize = 1000
current_multiplier = 1
total_prize = 0

for question in QandA.keys():
    os.system(f"say '{question}'")
    answer = input(question)
    correct_answer = QandA[question]#*value is iniclalized with the help of keys in Dictionary

    if answer.strip().lower() == correct_answer.strip().lower():
        os.system(f"say 'correct answer '")
        print("Correct answer")
        score += 1
        total_prize += base_prize * current_multiplier
        current_multiplier += 1  # Increase multiplier for next correct answer
    else:
        os.system(f"say 'Incorrect answer. The correct answer is {correct_answer}'")
        print(f"Incorrect answer. The correct answer is {correct_answer}")
        
        current_multiplier = 1  # Reset multiplier on wrong answer

os.system(f"say 'You have got {score} out of {len(QandA)} questions correct.'")
print(f"You have got {score} out of {len(QandA)} questions correct.")
os.system(f"say 'Congratulation!!!The final prize you won is {total_prize}'")
print(f" Congratulations!!!!!!!!The final prize you won is {total_prize}")
last=f"say 'Thank you for playing, wish you have a good day '"
os.system(last)


# # Dictionary example
# my_dict = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
# }

# # Accessing values using keys
# print(my_dict["key1"])  # Output: value1
# print(my_dict["key2"])  # Output: value2
    

