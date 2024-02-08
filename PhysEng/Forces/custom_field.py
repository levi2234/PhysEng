class CustomField():
    def __init__(self, function, name="Custom Field", active=True):
        self.environment = name
        self.function = function
        self.active = active
        self.name = name

    
    def update(self):
        if self.active == False:
            return
        
        for i in self.environment.particles:
            self.function(i)
        pass