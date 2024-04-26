
class ClearBuffer():
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = f"Clear Buffer"
        pass
    
    def show(self):
        if self.active:
            self.visualize.renderer.clear_frames()
            self.active = False
            pass
