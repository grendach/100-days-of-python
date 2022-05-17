
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self): # inharit from super class Animal
        super().__init__()
    
    def breathe(self):
        super().breathe() # inharit method from super class Animal
        print("Doing that under water") # add own functionality
    
    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
