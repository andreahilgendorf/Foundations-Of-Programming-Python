import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    def test_person_init(self):
        person=Person("Andrea", "Hilgendorf")
        self.assertEqual(person.first_name, "Andrea")
        self.assertEqual(person.last_name, "Hilgendorf")
    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            person=Person("Andrea123", "Hilgendorf")
        with self.assertRaises(ValueError):
            person=Person("Andrea", "Hilgendorf123")
    def test_person_str(self):
        person=Person("Andrea", "Hilgendorf")
        self.assertEqual('Andrea,Hilgendorf', str(person))


class TestEmployee(unittest.TestCase):
    def test_employee_init(self):
        employee=Employee("Andrea", "Hilgendorf", "2024-09-24", 5)
        self.assertEqual(employee.first_name, "Andrea")
        self.assertEqual(employee.last_name, "Hilgendorf")

    def test_employee_invalid_name(self):
        with self.assertRaises(ValueError):
            employee=Employee("Andrea123", "Hilgendorf", "2024-09-24", 5)
        with self.assertRaises(ValueError):
            employee=Employee("Andrea", "Hilgendorf123", "2024-09-24", 5)

    def test_employee_str(self):
        employee=Employee("Andrea", "Hilgendorf", "2024-09-24", 5)
        self.assertEqual('Andrea,Hilgendorf,2024-09-24,5', str(employee))

    def test_employee_invalid_rating_type(self):
        with self.assertRaises(ValueError):
            employee=Employee("Andrea", "Hilgendorf", "2024-09-24", "Five")

    # TODO this should raise an error
    def test_employee_rating_out_of_range(self):
        with self.assertRaises(ValueError):
            employee=Employee("Andrea", "Hilgendorf", "2024-09-24", 200)



if __name__ == '__main__':
    unittest.main()