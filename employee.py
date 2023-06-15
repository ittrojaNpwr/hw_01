class Employee:
    """Описание работника года!"""

    def __init__(self, first_name, last_name):
        """присваиваем все значения"""
        self.first_name = first_name
        self.last_name = last_name
        self.year_raise = 5000

    def get_raise(self, new_raise=None):
        """Работа с кастомным значением year_raise"""
        if new_raise is not None:
            self.year_raise += new_raise
        else:
            self.year_raise += 5000
