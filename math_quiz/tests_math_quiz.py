import unittest
from math_quiz import integer_generator, operator_generator, question_generator


class TestMathGame(unittest.TestCase):

    def test_integer_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = integer_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operator_generator(self):
        # Test if random operators generated are valid
        true_operators = ['+', '-', '*']
        for _ in range(1000):
             operator = operator_generator()
             self.assertIn(operator, true_operators)
             

    def test_question_generator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (7, 8, '*', '7 * 8', 56),
                (1, 1, '-', '1 - 1', 0)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = question_generator(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
