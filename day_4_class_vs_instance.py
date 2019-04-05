class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge # Do we need to do this? Aly just refers to it as initialAge
        if self.initialAge < 1:
            print("Age is not valid, setting age to 0.")
            self.age = 0 # This instance variable need not be declared?
        else:
            self.age = self.initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age >= 18:
            print("You are old.")
        elif (self.age >= 13):
            print("You are a teenager.")
        else:
            print("You are young.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1