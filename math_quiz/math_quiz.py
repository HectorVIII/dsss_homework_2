import random


def integer_generator(min, max):
    """
    Generate a random integer between 'min' and 'max'.
    """
    return random.randint(min, max)


def operator_generator():
    """
    Generate a random operator from '+', '-', '*'.
    """
    return random.choice(['+', '-', '*'])


def question_generator(num1, num2, operator):
    """
    Generate a math question
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-': 
        answer = num1 - num2
    else: 
        answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3 #You can set total questions here

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = integer_generator(1, 10) #You can change value here to increase the difficult
        num2 = integer_generator(1, 5)
        operator = operator_generator()

        problem, answer = question_generator(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        # Error handling for users input
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
