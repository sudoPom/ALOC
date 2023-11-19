import tkinter as tk


class ZoomPanCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Button-4>", self.zoom_in)  # Zoom in with mouse wheel
        self.bind("<Button-5>", self.zoom_out)  # Zoom out with mouse wheel
        self.bind("<B2-Motion>", self.pan)  # Pan with middle mouse button drag
        # Start pan with middle mouse button click
        self.bind("<Button-2>", self.pan_start)
        # End pan with middle mouse button release
        self.bind("<ButtonRelease-2>", self.pan_end)
        self.scale_factor = 1.2  # Zoom factor
        self.start_x = None
        self.start_y = None
        self.start_scan_x = None
        self.start_scan_y = None

    def zoom(self, x, y, factor):
        bbox = self.bbox(tk.ALL)

        x_center = self.canvasx(self.winfo_width() / 2)
        y_center = self.canvasy(self.winfo_height() / 2)

        new_width = self.winfo_width() * factor
        new_height = self.winfo_height() * factor

        new_x0 = x_center - new_width / 2
        new_y0 = y_center - new_height / 2
        new_x1 = x_center + new_width / 2
        new_y1 = y_center + new_height / 2

        self.scan_dragto(0, 0, gain=1)
        self.scale(tk.ALL, x_center, y_center, factor, factor)

    def zoom_in(self, event):
        self.zoom(event.x, event.y, self.scale_factor)

    def zoom_out(self, event):
        self.zoom(event.x, event.y, 1 / self.scale_factor)

    def pan_start(self, event):
        if self.start_scan_x is None and self.start_scan_y is None:
            self.start_x = event.x
            self.start_y = event.y
            self.start_scan_x = int(self.canvasx(0))
            self.start_scan_y = int(self.canvasy(0))

    def pan(self, event):
        if self.start_x is not None and self.start_y is not None:
            delta_x = self.start_x - event.x
            delta_y = self.start_y - event.y
            self.scan_dragto(self.start_scan_x + int(delta_x),
                             self.start_scan_y + int(delta_y), gain=1)

    def pan_end(self, event):
        self.start_x = None
        self.start_y = None
