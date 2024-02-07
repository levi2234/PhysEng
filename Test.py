class one():
    def __init__(self):
        print("one")
    def call(self):
        print("one call")
    def call2(self):
        print("one call2")
        
class two(one):
    def __init__(self):
        print("two")
    def call(self):
        print("two call")

print(type(two()))