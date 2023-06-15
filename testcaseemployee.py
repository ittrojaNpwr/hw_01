import employee
from employee import Employee

import unittest


class EmployeeTest(unittest.TestCase):
    """класс с тестами"""

    def setUp(self) -> None:
        self.employee = Employee('andrew', 'mischenko')

    def test_default_raise(self):
        """проверка, что year_raise = 5000"""
        self.assertEqual(self.employee.year_raise, 5000)

    def test_custom_raise(self):
        """проверка кастомного значения year_raise"""
        self.assertEqual(self.employee.year_raise, 5000)
        self.employee.get_raise(3000)
        self.assertEqual(self.employee.year_raise, 8000)
        self.employee.get_raise()
        self.assertEqual(self.employee.year_raise, 13000)
if __name__ == '__main__':
    unittest.main()
