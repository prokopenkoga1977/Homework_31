from Person.Person import Person

class Admin(Person):
    def __init__(self, login, password, remove_person = True):
        super().__init__(login, password)
        self.remote_person = remove_person