class Spring():
    
    def __init__(self, environment, softening_length=0) -> None:
        self.name = "Spring"
        self.environment = environment
        self.softening_length = softening_length
        pass
    
    def update(self):
        for spring_links in self.environment.spring_links:
            spring_links.update(softening_length=self.softening_length)
        pass