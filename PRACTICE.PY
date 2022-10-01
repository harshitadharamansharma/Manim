class Vehicle:
    def __init__(self, number_of_wheels, tanktype, number_of_seats, max_velocity ):
       self.number_of_wheels = number_of_wheels
       self.tanktype = tanktype
       self.number_of_seats =  number_of_seats
       self.max_velocity = max_velocity

@property
def number_of_wheels(self):
    return self.number_of_wheels

@number_of_wheels.setter
def set_number_of_wheels(self, number):
    self.number_of_wheels = number

def make_noise (self):
    print:('VRUMMMM')


tesla_model_s =Vehicle(4, 'electric', 5, 250)
print(tesla_model_s.number_of_wheels)  #4
tesla_model_s.number_of_wheels = 2  
print(tesla_model_s.number_of_wheels) #2



class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email # adding understore during defining  matbal non public instance variable

tk = Person('TK', 'tk@mail.com')
print(tk._email) # tk@mail.com