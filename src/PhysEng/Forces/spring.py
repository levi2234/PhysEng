class Spring():
    """
    Represents a spring force in a physics simulation.
    
    Attributes:
        environment (Environment): The environment in which the spring operates.
        softening_length (float): The softening length of the spring.
        name (str): The name of the spring.
        active (bool): Indicates whether the spring is active or not.
    """
    
    def __init__(self, environment, softening_length=0, name="Spring", active=True) -> None:
        self.name = name
        self.environment = environment
        self.softening_length = softening_length
        self.active = active
    
    def update(self):
        """
        Updates the spring by updating all the spring links in the environment.
        """
        if self.active == False:
            return
        
        for spring_links in self.environment.spring_links:
            spring_links.update(softening_length=self.softening_length)
