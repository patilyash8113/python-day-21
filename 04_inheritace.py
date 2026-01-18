class animal: #superclass 

    location="australia"
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Generic animal sound")

class dog(animal): #This is how inheritance works in python
    def speak(self):
        super().speak() #so basically super is used to call other parent or superclass  methods...
        print("Woof!")
        
# a=animal("Dog") 
# a.speak()
d= dog("yash")
d.speak()
print(d.location)