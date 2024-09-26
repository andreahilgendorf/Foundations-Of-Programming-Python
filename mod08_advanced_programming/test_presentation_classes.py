# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - test presentation classes
# Description: A class for testing IO class
# ChangeLog: (Who, When, What)
# AHilgendorf,09/25/2024,Created Script
# ------------------------------------------------------------------------------------------------- #

from presentation_classes import IO
import unittest
from unittest.mock import patch
from data_classes import Employee


class TestIO(unittest.TestCase):
    
    # Test options 1 through 4 return 1 through 4
    def test_get_input(self):
        for test_case in ["1", "2", "3", "4"]:
            with patch('builtins.input', return_value=test_case):
                choice = IO.input_menu_choice()
                self.assertEqual(test_case, choice)

    def test_input_data_to_table(self):
        with patch('builtins.input', side_effect=['Lucas', 'Hilgendorf', '2024-05-05', 5]):
            employees = []
            employees = IO.input_employee_data(employees, Employee)
            self.assertEqual(1, len(employees))
            self.assertEqual('Lucas', employees[0].first_name)
            self.assertEqual('Hilgendorf', employees[0].last_name)
            self.assertEqual('2024-05-05', employees[0].review_date)
            self.assertEqual(5, employees[0].review_rating)

if __name__ == '__main__':
    unittest.main()





#    def test_input_data_to_table_invalid_score(self):
#        with patch('builtins.input', side_effect=['Lucas', 'Hilgendorf', '2024-05-05', "five"]):
#            employees = []
#
#            with self.assertRaises(ValueError):
#                employees = IO.input_employee_data(employees, Employee)
            #self.assertEqual(0, len(employees))
            #self.assertEqual('Lucas', employees[0].first_name)
            #self.assertEqual('Hilgendorf', employees[0].last_name)
            #self.assertEqual('2024-05-05', employees[0].review_date)
            #self.assertEqual(5, employees[0].review_rating)
