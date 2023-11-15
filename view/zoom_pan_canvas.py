import tkinter as tk


class ZoomPanCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Button-4>", self.zoom_in)
        self.bind("<Button-5>", self.zoom_out)
        self.bind("<B2-Motion>", self.pan) 
        self.bind("<Button-2>", self.pan_start) 
        self.bind("<ButtonRelease-2>", self.pan_end)  
        self.scale_factor = 1.2  

    def zoom_in(self, event):
        self.scale(tk.ALL, event.x, event.y, self.scale_factor)

    def zoom_out(self, event):
        self.scale(tk.ALL, event.x, event.y, 1 / self.scale_factor)

    def pan_start(self, event):
        self.scan_mark(event.x, event.y)

    def pan(self, event):
        self.scan_dragto(event.x, event.y, gain=1)
