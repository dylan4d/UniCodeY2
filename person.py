class Person(object):

    def __init__(self, identity, name, job, salary):
        self._identity = identity 
        self._name = name
        self._job = job
        self._salary = salary

    def __str__(self):
        return ("%i %s %s %i" % (self._identity, self._name, self._job, self._salary))

    def __eq__(self, someOtherPerson):
        
        if self._identity == someOtherPerson.identity:
            return True
        else:
            return False

    def givePayRaise(self, percentage):
        self._salary += self._salary * (percentage / 100)

    def getIdentity(self):
        return self._identity

    identity = property(getIdentity)

    def getSalary(self):
        return self._name

    def setSalary(self, salary):
        
        if type(salary) != int:
            print("Pass a number")
            return

        self._salary = salary

    salary = property(getSalary, setSalary)
  
def main():
    cathal = Person(123, "Cathal", "Software person", 120000)
    laura = Person(124, "Laura", "Software person", 120000)

    cathal.givePayRaise(10)
    print(cathal)

    print(cathal == cathal)
    print(laura == cathal)
    print(cathal == laura)

if __name__ == "__main__":
    main()