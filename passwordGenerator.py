'''
Generates a random password.
'''
import secrets
import string

class PasswordGenerator:
    def __init__(self, num_passwords_to_generate=5) -> None:
        '''
        Params:
        num_passwords_to_generate (int) - how many passwords to generate and display to the user
        '''
        self.num_passwords_to_generate = num_passwords_to_generate
        self.letters = string.ascii_lowercase
        self.numbers = string.digits
        self.symbols = string.punctuation
        
    def get_num_passwords_to_generate(self) -> int:
        return self.num_passwords_to_generate
    
    def generate_password(self, length=8, **kwargs) -> list[str]:
        '''
        Generates self.num_passwords_to_generate passwords
        
        Params (Keyword arguments):
        num_numbers: int, num_uppercase: int, num_symbols: int
        
        num_numbers (int) - the amount of numbers in the password(s)
        num_uppercase (int) - the amount of numbers in the password(s)
        num_symbols (int) - the number of symbols in the password(s)
        length (int) - the amount of total characters in the password(s)
        
        The length of each password is 8 as a default
        
        Returns a list of passwords
        '''
        passwords = []
        index_used = []
        
        for i in range(self.num_passwords_to_generate):
            if len(kwargs.items()) == 0:
                passwords.append("".join([secrets.choice(self.letters) for j in range(length)]))
            else:
                password = [secrets.choice(self.letters) for i in range(length)]
                print(password)
                if kwargs.get("num_numbers") != None:
                    for j in range(kwargs.get("num_numbers")):
                        index = secrets.choice([k for k in range(length)])
                        print(index)
                        password[index] = secrets.choice(self.numbers)
                        index_used.append(index)
                
                if kwargs.get("num_uppercase") != None:
                    for j in range(kwargs.get("num_uppercase")):
                        index = secrets.choice([k for k in range(length) if index_used.count(k) == 0])
                        print(index)
                        password[index] = password[index].upper()
                        
                if kwargs.get("num_symbols") != None:
                    for j in range(kwargs.get("num_symbols")):
                        index = secrets.choice([k for k in range(length) if index_used.count(k) == 0])
                        print(index)
                        password[index] = secrets.choice(self.symbols)
                        
                password = "".join([secrets.choice(self.letters)])
                passwords.append(password)
                index_used.clear()
        
        return passwords
    