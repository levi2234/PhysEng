class CustomField():
    def __init__(self, function, name="Custom Field", active=True):
        self.environment = name
        self.function = function
        self.active = active
        self.name = name

    def update(self):
        if not self.active:
            return
        
        for i in self.environment.particles:
            self.function(i)
        pass