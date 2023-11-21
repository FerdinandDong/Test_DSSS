import unittest
from math_quiz import generate_random_number, choose_random_operator, create_problem_and_answer

class TestMathQuiz(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
    
    def test_choose_random_operator(self):
        # Test whether one of "+", "-" or "*" is always selected
        operators = ['+', '-', '*']
        for _ in range(1000):
            op = choose_random_operator()
            self.assertIn(op, operators)

    def test_create_problem_and_answer(self):
        # Test that questions and answers are generated correctly
        
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 1, '-', '3 - 1', 2),
            (4, 3, '*', '4 * 3', 12),
        ]
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()