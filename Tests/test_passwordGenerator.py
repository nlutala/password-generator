'''
Tests for the passwordGenerator script
'''

import random, string, unittest
from passwordGenerator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_passwordGenerator_raises_valueerror_if_no_num_passwords_are_given(self):
        num_passwords = ""
        with self.assertRaises(ValueError):
            num_passwords = int(num_passwords)

    def test_passwordGenerator_raises_valueerror_if_no_length_is_given(self):
        length = ""
        with self.assertRaises(ValueError):
            length = int(length)

    def test_passwordGenerator_raises_valueerror_if_no_num_numbers_are_given(self):
        num_numbers = ""
        with self.assertRaises(ValueError):
            num_numbers = int(num_numbers)

    def test_passwordGenerator_raises_valueerror_if_no_num_uppercase_are_given(self):
        num_uppercase = ""
        with self.assertRaises(ValueError):
            num_uppercase = int(num_uppercase)

    def test_passwordGenerator_raises_valueerror_if_no_num_symbols_are_given(self):
        num_symbols = ""
        with self.assertRaises(ValueError):
            num_symbols = int(num_symbols)

    def test_num_passwords_generated_is_amount_user_specified(self):
        num_passwords_to_generate = 2
        pg = PasswordGenerator(num_passwords_to_generate)
        assert len(pg.generate_password()) == num_passwords_to_generate

    def test_password_generated_is_of_length(self):
        num_passwords = random.randint(1,5)
        pg = PasswordGenerator(num_passwords)
        length = random.randint(8,15)
        passwords = pg.generate_password(length)

        for password in passwords:
            assert length == len(password)

    def test_password_generated_has_correct_num_numbers(self):
        num_passwords = random.randint(1,5)
        pg = PasswordGenerator(num_passwords)
        length = random.randint(8,15)
        num_numbers = random.randint(0,length)
        passwords = pg.generate_password(length, num_numbers=num_numbers)

        for password in passwords:
            count = [1 for char in list(password) if char.isdigit()]
            assert num_numbers == len(count)

    def test_password_generated_has_correct_num_uppercase(self):
        num_passwords = random.randint(1,5)
        pg = PasswordGenerator(num_passwords)
        length = random.randint(8,15)
        num_uppercase = random.randint(0,length)
        passwords = pg.generate_password(length, num_uppercase=num_uppercase)

        for password in passwords:
            count = [1 for char in list(password) if char.isupper()]
            assert num_uppercase == len(count)

    def test_password_generated_has_correct_num_symbols(self):
        num_passwords = random.randint(1,5)
        pg = PasswordGenerator(num_passwords)
        length = random.randint(8,15)
        num_symbols = random.randint(0,length)
        passwords = pg.generate_password(length, num_symbols=num_symbols)

        for password in passwords:
            count = [1 for char in list(password) if char in string.punctuation]
            assert num_symbols == len(count)

    def test_generate_password_raises_value_error_if_num_constraints_exceed_password_length(self):
        num_passwords = random.randint(1,5)
        pg = PasswordGenerator(num_passwords)

        length = random.randint(8,15)
        num_numbers = random.randint(length,20)
        num_uppercase = random.randint(length,20)
        num_symbols = random.randint(length, 20)

        with self.assertRaises(ValueError):
            pg.generate_password(length, num_numbers=num_numbers, num_uppercase=num_uppercase, num_symbols=num_symbols)

    def test_generate_password_correctly_generates_passwords_with_all_constraints(self):
        num_passwords = random.randint(1,5)
        pg = PasswordGenerator(num_passwords)

        length = random.randint(8,15)
        num_numbers = random.randint(0,length-1)
        num_uppercase = random.randint(0,length-num_numbers)
        num_symbols = random.randint(0,length-(num_numbers + num_uppercase))

        passwords = pg.generate_password(length, num_numbers=num_numbers, num_uppercase=num_uppercase, num_symbols=num_symbols)

        for password in passwords:
            count = [1 for char in list(password) if char.isdigit()]
            assert num_numbers == len(count)

            count = [1 for char in list(password) if char.isupper()]
            assert num_uppercase == len(count)

            count = [1 for char in list(password) if char in string.punctuation]
            assert num_symbols == len(count)
