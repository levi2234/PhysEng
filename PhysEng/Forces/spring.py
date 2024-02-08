class Spring():
    
    def __init__(self, environment, softening_length=0, name="Spring", active=True) -> None:
        self.name = name
        self.environment = environment
        self.softening_length = softening_length
        self.active = active
        pass
    
    def update(self):
        if self.active == False:
            return
        
        for spring_links in self.environment.spring_links:
            spring_links.update(softening_length=self.softening_length)
        pass