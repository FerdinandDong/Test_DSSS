import random

def generate_random_number(min_value, max_value):
    """
    Generate a random integer between min_value and max_value.

    Args:
    min_value (int): Minimum value of the random number.
    max_value (int): Maximum value of the random number.

    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_random_operator():
    """
    Choose a random operator from '+', '-', or '*'.

    Returns:
    str: A randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])


def create_problem_and_answer(number1, number2, operator):
    """
    Create a math problem and its answer based on given numbers and operator.

    Args:
    number1 (int): The first number in the problem.
    number2 (int): The second number in the problem.
    operator (str): The operator of the problem.

    Returns:
    tuple: A tuple containing the problem as a string and its answer.
    """
    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem, answer

def math_quiz():
    """
    Run a math quiz game where users solve randomly generated math problems.
    """
    score = 0
    total_questions = 3  # Total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 10)
        operator = choose_random_operator()

        problem, correct_answer = create_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

def main():
    # 您的游戏逻辑
    math_quiz()
    
if __name__ == "__main__":
    math_quiz()

