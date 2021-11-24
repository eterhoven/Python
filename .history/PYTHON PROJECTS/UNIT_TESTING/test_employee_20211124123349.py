import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp1 = Employee('Emil', 'Terhoven', 5000)
        emp2 = Employee('Andrea', 'Terhoven', 100000)
        
        self.assertEqual(self.emp_1.email, 'Emil.Terhoven@email.com')
        self.assertEqual(self.emp_2.email, 'Andrea.Terhoven@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Terhoven@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Terhoven@email.com')

    def test_fullname(self):
        emp1 = Employee('Emil', 'Terhoven', 5000)
        emp2 = Employee('Andrea', 'Terhoven', 100000)
        
        self.assertEqual(self.emp_1.fullname, 'Emil Terhoven')
        self.assertEqual(self.emp_2.fullname, 'Andrea Terhoven')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Terhoven')
        self.assertEqual(self.emp_2.fullname, 'Jane Terhoven')

    def test_apply_raise(self):
        emp1 = Employee('Emil', 'Terhoven', 5000)
        emp2 = Employee('Andrea', 'Terhoven', 100000)
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 105000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()