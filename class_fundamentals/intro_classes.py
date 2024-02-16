class Person:
    # constructor with three attributes: first name, last name and age.
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
    
    # create a method to get the full name.
    def full_name(self):
        return self.f_name + ' ' + self.l_name
    
    # create a method to get the email address.
    def email_address(self):
        return self.f_name + '.' + self.l_name + "@email.com"



# creating a Person object.
p1 = Person("Ram", "Sharma", 10)

p1.email_address()