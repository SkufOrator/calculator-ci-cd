import unittest
from unittest.mock import patch, call
import io
import sys

# Импортируем функцию для тестирования
from calculator import calculator


class TestCalculatorOperations(unittest.TestCase):
    """Тестирование математических операций калькулятора"""

    @patch('builtins.input', side_effect=['5', '+', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_addition(self, mock_stdout, mock_input):
        """Тестирование операции сложения"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Результат: 8.0", output)

    @patch('builtins.input', side_effect=['10', '-', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_subtraction(self, mock_stdout, mock_input):
        """Тестирование операции вычитания"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Результат: 6.0", output)

    @patch('builtins.input', side_effect=['7', '*', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_multiplication(self, mock_stdout, mock_input):
        """Тестирование операции умножения"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Результат: 42.0", output)

    @patch('builtins.input', side_effect=['15', '/', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_division(self, mock_stdout, mock_input):
        """Тестирование операции деления"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Результат: 5.0", output)

    @patch('builtins.input', side_effect=['5.5', '+', '2.3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_float_numbers_addition(self, mock_stdout, mock_input):
        """Тестирование сложения дробных чисел"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Результат: 7.8", output)

    @patch('builtins.input', side_effect=['-10', '-', '-3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_numbers_subtraction(self, mock_stdout, mock_input):
        """Тестирование вычитания отрицательных чисел"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Результат: -7.0", output)


class TestCalculatorErrorHandling(unittest.TestCase):
    """Тестирование обработки ошибок в калькуляторе"""

    @patch('builtins.input', side_effect=['10', '/', '0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_division_by_zero_error(self, mock_stdout, mock_input):
        """Тестирование обработки деления на ноль"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Ошибка: Деление на ноль!", output)
        self.assertNotIn("Результат:", output)

    @patch('builtins.input', side_effect=['5', '%', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_operator_error(self, mock_stdout, mock_input):
        """Тестирование обработки неверного оператора"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Ошибка: Неверный оператор!", output)
        self.assertNotIn("Результат:", output)

    @patch('builtins.input', side_effect=['abc', '+', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_first_number_error(self, mock_stdout, mock_input):
        """Тестирование обработки неверного первого числа"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Ошибка: Введите корректные числа!", output)
        self.assertNotIn("Результат:", output)

    @patch('builtins.input', side_effect=['5', '+', 'xyz'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_second_number_error(self, mock_stdout, mock_input):
        """Тестирование обработки неверного второго числа"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Ошибка: Введите корректные числа!", output)
        self.assertNotIn("Результат:", output)


class TestCalculatorInterface(unittest.TestCase):
    """Тестирование пользовательского интерфейса калькулятора"""

    @patch('builtins.input', side_effect=['8', '*', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_display(self, mock_stdout, mock_input):
        """Тестирование отображения меню операций"""
        calculator()
        output = mock_stdout.getvalue()
        self.assertIn("Доступные операции:", output)
        self.assertIn("+ Сложение", output)
        self.assertIn("- Вычитание", output)
        self.assertIn("* Умножение", output)
        self.assertIn("/ Деление", output)
        self.assertIn("Результат: 16.0", output)


class TestCalculatorPerformance(unittest.TestCase):
    """Тесты производительности для CI/CD"""

    def test_all_operations_quickly(self):
        """Быстрый тест всех операций"""
        test_cases = [
            (['2', '+', '2'], "Результат: 4.0"),
            (['5', '-', '3'], "Результат: 2.0"),
            (['3', '*', '4'], "Результат: 12.0"),
            (['10', '/', '2'], "Результат: 5.0"),
        ]

        for inputs, expected in test_cases:
            with self.subTest(inputs=inputs):
                with patch('builtins.input', side_effect=inputs):
                    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                        calculator()
                        output = mock_stdout.getvalue()
                        self.assertIn(expected, output)


def run_tests():
    """Функция для запуска всех тестов и возврата результата"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorErrorHandling))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorInterface))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorPerformance))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


if __name__ == '__main__':
    # Для CI/CD важно выходить с правильным кодом
    success = run_tests()
    sys.exit(0 if success else 1)