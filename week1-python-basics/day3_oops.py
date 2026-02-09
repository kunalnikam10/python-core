class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    return f"Hi How are you {self.name}"
  

class Class:
  def __init__(self, division, roll_no):
    self.division= division
    self.roll_no = roll_no

# p1= Person("Kunal", 23)

# print(p1.name)
# print(p1.greet())

class Animal:
  def __init__(self, name):
    self.name= name

  def speak(self):
    return "speak"
  
class Dog(Animal):
  def __init__(self, name, breed):
    self.breed = breed
    super().__init__(name)

  def speak(self):
    parent_call = super().speak()
    return f"{self.name} is the breed of a {self.breed} and doesnt {parent_call} but does bark"
  
# d1= Dog("Tommy", "Labrador")

# print(d1.name)
# print(d1.speak())

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person('{self.name}')"

# p = Person("Kunal")

# print(repr(p))

class Employee:
    company = "TechCorp"   # class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def __str__(self):
        return f"{self.name} earns {self.salary}"

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"


# e1 = Employee("Kunal", 50000)

# print(e1)
# print(e1.annual_salary())

class BankAccount:
   
   def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance

   def deposit(self, amount):
      if amount <= 0:
         return "Deposit must be positive"
      self.balance += amount
      return f"{self.owner} deposits {amount}"
   
   def withdraw(self, amount):
      if(self.balance<amount):
         self.balance= self.balance + amount
         return f"Insuffisient balance of {self.balance}"
      
      self.balance -= amount
      return f"Amount withdrawn is {amount}"

   def CurrBalance(self):
      return f"The current balance of {self.owner} is {self.balance}"
   
acc = BankAccount("Kunal", 60000)
print(acc.owner)
print(acc.CurrBalance())
print(acc.deposit(20000))
print(acc.CurrBalance())
print(acc.withdraw(30000))
print(acc.CurrBalance())
print(acc.withdraw(6000))
print(acc.CurrBalance())
      