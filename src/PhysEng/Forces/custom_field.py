class CustomField():
    def __init__(self, function, name="Custom Field", active=True):
        """
        Initializes a CustomField object.

        Args:
            function (function): The function to be applied to each particle in the environment.
            name (str, optional): The name of the custom field. Defaults to "Custom Field".
            active (bool, optional): Indicates whether the custom field is active. Defaults to True.
        """
        self.environment = name
        self.function = function
        self.active = active
        self.name = name

    def update(self):
        """
        Updates the custom field by applying the function to each particle in the environment.
        """
        if not self.active:
            return
        
        for i in self.environment.particles:
            self.function(i)
        pass