import math

from stretchable import Edge

from game.stretcheduicomponents.dm_button import StretchedDMButton
from timeline.timeline import Event

import pyray as pr


class IndicatorEvent(Event):

    def __init__(self, start_time, end_time, perfect_time, button: StretchedDMButton, color: pr.Color):
        super().__init__(start_time, end_time, None, self.update_indicator)

        self.perfect_time = perfect_time
        self.color = color
        self.button = button
        self.duration = perfect_time - start_time

    def update_indicator(self, current_time, time_since_start):
        t = self.duration - time_since_start
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        offset = - t * 250
        
        pr.draw_rectangle(int((bounding_box.x)+offset), int(bounding_box.y), 20, int(bounding_box.height), self.color)

