from json import JSONDecodeError
import tempfile
import unittest
from processing_classes import FileProcessor
import json
from data_classes import Employee


class TestFileProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_file=tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name=self.temp_file.name
    def tearDown(self) -> None:
        self.temp_file.close()
    def test_read_data_from_file(self):
        sample_data=[
                {
                    "FirstName": "Andrea", 
                    "LastName": "Hilgendorf", 
                    "ReviewDate": "2024-09-24", 
                    "ReviewRating": 5
                }
             ]
        with open(self.temp_file_name, 'w') as file:
            json.dump(sample_data, file)


        employees: list = []
        employees = FileProcessor.read_employee_data_from_file(file.name,
                                                       employee_data=employees,
                                                       employee_type=Employee)  # Note this is the class name (ignore the warning)

        self.assertEqual(len(sample_data), len(employees))
        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i]['FirstName'], "Andrea")
            self.assertEqual(sample_data[i]['LastName'], "Hilgendorf")
            self.assertEqual(sample_data[i]['ReviewDate'], "2024-09-24")
            self.assertEqual(sample_data[i]['ReviewRating'], 5)

    def test_write_data_to_file(self):
        employee=Employee("Andrea", "Hilgendorf", "2024-09-24", 5)
        employees = []
        employees.append(employee)
        FileProcessor.write_employee_data_to_file(self.temp_file_name,employees)

        with open(self.temp_file_name, 'r') as file:
            sample_data=json.load(file)
   
        self.assertEqual(len(sample_data), len(employees))
        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i]['FirstName'], "Andrea")
            self.assertEqual(sample_data[i]['LastName'], "Hilgendorf")
            self.assertEqual(sample_data[i]['ReviewDate'], "2024-09-24")
            self.assertEqual(sample_data[i]['ReviewRating'], 5)

    def test_read_data_from_file_json_decoder_error(self):
        with open(self.temp_file_name, 'w') as file:
            file.write("hello world")


        employees: list = []
        employees = FileProcessor.read_employee_data_from_file(file.name,
                    employee_data=employees,
                    employee_type=Employee)  # Note this is the class name (ignore the warning)
        
        with open(self.temp_file_name, 'r') as file:
            file_data = file.read()
        self.assertEqual(file_data,'[]')
        self.assertEqual(0, len(employees))

if __name__ == '__main__':
    unittest.main()