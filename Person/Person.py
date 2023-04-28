class Person:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        
    def display (self):
        print(f" Login: {self.login}, Password: {self.password}")