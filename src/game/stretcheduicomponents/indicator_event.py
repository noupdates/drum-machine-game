import math
from stretchable import Edge
from game.stretcheduicomponents.dm_button import StretchedDMButton
from timeline.timeline import Event
import pyray as pr

class IndicatorEvent(Event):

    def __init__(self, start_time, end_time, perfect_time, button: StretchedDMButton, color: pr.Color, button_type: str):
        super().__init__(start_time, end_time, None, self.get_update_method(button_type))

        self.perfect_time = perfect_time
        self.color = color
        self.button = button
        self.duration = perfect_time - start_time

    def get_update_method(self, button_type):
        if button_type == 'Q':
            return self.update_indicator_left
        elif button_type == 'W':
            return self.update_indicator_top
        elif button_type == 'E':
            return self.update_indicator_right
        else:
            raise ValueError("Invalid button type specified")

    def update_indicator_left(self, current_time, time_since_start):
        t = self.duration - time_since_start
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        offset = -t * 250  # Coming from the left
        x_position = bounding_box.x + offset
        pr.draw_rectangle(int(x_position), int(bounding_box.y), 20, int(bounding_box.height), self.color)

    def update_indicator_top(self, current_time, time_since_start):
        t = self.duration - time_since_start
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        offset = -t * 250  # Coming from the top
        x_position = bounding_box.x  # Keep x position constant
        y_position = bounding_box.y + offset  # Move downwards
        pr.draw_rectangle(int(x_position), int(y_position), int(bounding_box.height), 20, self.color)

    def update_indicator_right(self, current_time, time_since_start):
        t = self.duration - time_since_start
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        offset = t * 250  # Coming from the right
        x_position = bounding_box.x + offset  # Move leftwards
        pr.draw_rectangle(int(x_position), int(bounding_box.y), 20, int(bounding_box.height), self.color)