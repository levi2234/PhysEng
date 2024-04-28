
import pygame as pg


class Renderer:
    def __init__(self, fps=30, output="output.gif", codec="libx264", framelimit=300):
        from collections import deque
        
        try:
            import imageio as io
        except ImportError:
            print("imageio not installed. Please install imageio to use the renderer.")
            return
        
        try:
            import numpy as np
        except ImportError:
            print("numpy not installed. Please install numpy to use the renderer.")
            return
        self.fps = fps
        self.output = output
        self.frames = deque([])
        self.codec = codec
        self.framelimit = framelimit

    def add_frame(self, frame):
        if len(self.frames) >= self.framelimit:
            self.frames.popleft()
        self.frames.append(frame)
        
    def clear_frames(self):
        self.frames = deque([])
        print("Buffer cleared.")
        
    

    def render(self):
        if not self.frames:
            print("No frames to render.")
            return
        
        self.frames = np.array(self.frames, dtype=np.uint8)
        #rotate all frames 90 degrees
        self.frames = np.rot90(self.frames, 3, axes=(1, 2))
        #flip all frames horizontally
        self.frames = np.flip(self.frames, axis=2)

        
        

        #use pillow to convert frames to video
        with io.get_writer(self.output, fps=self.fps, codec=self.codec) as writer:
            for frame in self.frames:
                writer.append_data(frame)
        
        
        print(f"Video rendered successfully to {self.output}")
