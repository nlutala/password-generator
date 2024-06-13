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
                
                # Check constraints:
                constraints = kwargs.get("num_numbers", 0) + kwargs.get("num_uppercase", 0) + kwargs.get("num_symbols", 0)
                if length < constraints:
                    raise ValueError(f"The password is set to be {length} characters long, but the amount of numbers, uppercase letters and symbols to be added into the password is {constraints}.")
                
                # Check each of the values of the extra arguments added
                if kwargs.get("num_numbers", 0) != 0:
                    for j in range(kwargs.get("num_numbers")):
                        index = secrets.choice([k for k in range(length) if index_used.count(k) == 0])
                        password.pop(index)
                        password.insert(index, secrets.choice(self.numbers))
                        index_used.append(index)
                
                if kwargs.get("num_uppercase", 0) != 0:
                    for j in range(kwargs.get("num_uppercase")):
                        index = secrets.choice([k for k in range(length) if index_used.count(k) == 0])
                        password.pop(index)
                        password.insert(index, secrets.choice(self.letters).upper())
                        index_used.append(index)
                        
                if kwargs.get("num_symbols", 0) != 0:
                    for j in range(kwargs.get("num_symbols")):
                        index = secrets.choice([k for k in range(length) if index_used.count(k) == 0])
                        password.pop(index)
                        password.insert(index, secrets.choice(self.symbols))
                        index_used.append(index)
                        
                passwords.append("".join(password))
                index_used.clear()
        
        return passwords


if __name__ == "__main__":
    while True:
        num_passwords = int(input("How many passwords would you like to generate?: "))
        length = int(input("How many characters would you like your password(s) to have?: "))
        num_numbers = int(input("How many numbers would you like in your password(s)?: "))
        num_uppercase = int(input("How many uppercase letters would you like in your password(s)?: "))
        num_symbols = int(input("How many special characters or symbols would you like in your password(s)?: "))
        
        pg = PasswordGenerator(num_passwords)
        
        print("\nPlease find your generated passwords below: ")
        for password in pg.generate_password(length, num_numbers=num_numbers, num_uppercase=num_uppercase, num_symbols=num_symbols):
            print(password)
                
        isDone = False
        
        while isDone == False:
            userInput = input("\nDo you want to generate a new password? Enter 'yes' (y) or 'no' (n): ")
            if userInput.upper() == "YES" or userInput.upper() == "Y":
                isDone = True
                continue
            elif userInput.upper() == "NO" or userInput.upper() == "N":
                isDone = True
                input("\nPress the Enter key to quit ")
                exit()
            else:
                print("\nThere was a problem with your input.\n")
