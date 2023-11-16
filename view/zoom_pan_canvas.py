import tkinter as tk


class ZoomPanCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Button-4>", self.zoom_in)
        self.bind("<Button-5>", self.zoom_out)
        self.bind("<B2-Motion>", self.pan) 
        self.bind("<Button-2>", self.pan_start) 
        self.scale_factor = 1.2  
        self.pan_start_x = None
        self.pan_start_y = None

    def zoom_in(self, event):
        self.zoom(event.x, event.y, self.scale_factor)

    def zoom_out(self, event):
        self.zoom(event.x, event.y, 1 / self.scale_factor)

    def zoom(self, x, y, factor):
        bbox = self.bbox(tk.ALL)
        if bbox is not None:
            center_x = (bbox[0] + bbox[2]) / 2
            center_y = (bbox[1] + bbox[3]) / 2

            new_width = (bbox[2] - bbox[0]) * factor
            new_height = (bbox[3] - bbox[1]) * factor

            new_x0 = center_x - new_width / 2
            new_y0 = center_y - new_height / 2
            new_x1 = new_x0 + new_width
            new_y1 = new_y0 + new_height

            self.scale(tk.ALL, center_x, center_y, factor, factor)
            self.scan_dragto(new_x0, new_y0, gain=1)


    def pan_start(self, event):
        self.pan_start_x = event.x
        self.pan_start_y = event.y

    def pan(self, event):
        if self.pan_start_x is not None and self.pan_start_y is not None:
            delta_x = event.x - self.pan_start_x
            delta_y = event.y - self.pan_start_y
            self.scan_dragto(-delta_x, -delta_y, gain=1)
            self.pan_start_x = event.x
            self.pan_start_y = event.y

    def pan_end(self, event):
        self.pan_start_x = None
        self.pan_start_y = None
