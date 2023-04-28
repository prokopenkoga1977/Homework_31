# Homework

# 1) Create app.py
# 2) Create package Person -> Into Person create file Person.py -> 
# 2.1) Create file Admin.py
# 2) Admin extends Person
# 3) Create instance Admin into app.py 
# 3.1) Into app.py create function or class(method) that will run our program . 
# 4) If app.py == __main__ => run program 

from Person.Person import Person
from Admin import Admin

person = Person("Hennadii", 11111111)
admin = Admin("Alex", 2222222)

def main():
    person.display()
    print(admin.__dict__)
    
if __name__ == "__main__":
   main() 
