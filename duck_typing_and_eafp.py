class Person:
    def feature(self):
        print("I am a person with unique features.")


class dog:
    def feature(self):
        print("I am a dog with unique features.")
        
class call_function:
    def call(self,obj):
        obj.feature()


p = Person()
d = dog()

p.feature()  # Output: I am a person with unique features.
d.feature()  # Output: I am a dog with unique features.

c = call_function()

c.call(p)  # Output: I am a person with unique features.
c.call(d)  # Output: I am a dog with unique features.

