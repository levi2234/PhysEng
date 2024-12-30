
import pygame as pg
from collections import deque


class Renderer:
    """
    A class that renders frames into a video using imageio.

    Args:
        fps (int): Frames per second of the output video. Default is 30.
        output (str): Output file name for the rendered video. Default is "output.gif".
        codec (str): Codec used for encoding the video. Default is "libx264".
        framelimit (int): Maximum number of frames to keep in the buffer. Default is 300.
    """

    def __init__(self, fps=30, output="output.gif", codec="libx264", framelimit=300):
        self.fps = fps
        self.output = output
        self.frames = deque([])
        self.codec = codec
        self.framelimit = framelimit

    def add_frame(self, frame):
        """
        Adds a frame to the renderer's frame buffer.

        Args:
            frame: The frame to be added.
        """
        if len(self.frames) >= self.framelimit:
            self.frames.popleft()
        self.frames.append(frame)
        
    def clear_frames(self):
        """
        Clears all frames from the renderer's frame buffer.
        """
        self.frames = deque([])
        print("Buffer cleared.")
        
    def render(self):
        """
        Renders the frames in the frame buffer into a video file.
        """
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
