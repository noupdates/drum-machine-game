import math
from stretchable import Edge
from game.stretcheduicomponents.dm_button import StretchedDMButton
from timeline.timeline import Event
import pyray as pr



class IndicatorEvent(Event):
    OFFSET_VALUE = 250

    def __init__(self, start_time, end_time, perfect_time, button: StretchedDMButton, color: pr.Color, button_type: str):
        super().__init__(start_time, end_time, None, self.get_update_method(button_type))

        self.perfect_time = perfect_time
        self.color = color
        self.button = button
        self.duration = perfect_time - start_time 
        
        
    def get_update_method(self, button_type):
        if button_type == 'Q':
            return self.update_indicator_top_left
        elif button_type == 'W':
            return self.update_indicator_top
        elif button_type == 'E':
            return self.update_indicator_top_right
        elif button_type == 'A':
            return self.update_indicator_left
        elif button_type == 'S':
            return self.update_indicator_top
        elif button_type == 'D':
            return self.update_indicator_right
        elif button_type == 'Z':
            return self.update_indicator_bottom_left
        elif button_type == 'X':
            return self.update_indicator_bottom
        elif button_type == 'C':
            return self.update_indicator_bottom_right
        else:
            raise ValueError("Invalid button type specified")

    def update_indicator_left(self, current_time, time_since_start):
        t = self.duration - time_since_start + 0.2
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        offset = -t * IndicatorEvent.OFFSET_VALUE # Coming from the left
        x_position = bounding_box.x + offset
        pr.draw_rectangle(int(x_position), int(bounding_box.y), 20, int(bounding_box.height), self.color)

    def update_indicator_top(self, current_time, time_since_start):
        t = self.duration - time_since_start + 0.15
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        offset = -t * IndicatorEvent.OFFSET_VALUE  # Coming from the top
        x_position = bounding_box.x  # Keep x position constant
        y_position = bounding_box.y + offset  # Move downwards
        pr.draw_rectangle(int(x_position), int(y_position), int(bounding_box.height), 20, self.color)

    def update_indicator_right(self, current_time, time_since_start):
        t = self.duration - time_since_start + 0.5
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        offset = t * 300  # Coming from the right
        x_position = bounding_box.x + offset  # Move leftwards
        pr.draw_rectangle(int(x_position), int(bounding_box.y), 20, int(bounding_box.height), self.color)

    def update_indicator_bottom(self, current_time, time_since_start):
        t = self.duration - time_since_start + 0.1
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        offset = t * IndicatorEvent.OFFSET_VALUE  # Coming from the bottom
        x_position = bounding_box.x  # Keep x position constant
        y_position = bounding_box.y + bounding_box.height + offset  # Move upwards from the bottom
        pr.draw_rectangle(int(x_position), int(y_position), int(bounding_box.height), 20, self.color)

    def update_indicator_top_left(self, current_time, time_since_start):
        t = self.duration - time_since_start + 0.2  # Adjust the timing offset as needed
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        
        # Calculate the offset for both x and y positions
        offset_x = -t * IndicatorEvent.OFFSET_VALUE  # Move leftwards
        offset_y = -t * IndicatorEvent.OFFSET_VALUE  # Move downwards

        # Calculate the x and y positions for the indicator
        x_position = bounding_box.x + bounding_box.width + offset_x  - 100 # Start from the right side of the button
        y_position = bounding_box.y + offset_y  # Start from the top side of the button

        # Draw the indicator rectangle
        pr.draw_rectangle(int(x_position), int(y_position), int(bounding_box.height), 20, self.color)  # Adjust width and height as needed
        pr.draw_rectangle(int(x_position), int(y_position), 20, int(bounding_box.height), self.color)

    def update_indicator_top_right(self, current_time, time_since_start):
        t = self.duration - time_since_start + 0.18  # Adjust the timing offset as needed
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        
        # Calculate the offset for both x and y positions
        offset_x = -t * IndicatorEvent.OFFSET_VALUE  # Move leftwards
        offset_y = -t * IndicatorEvent.OFFSET_VALUE  # Move downwards

        # Calculate the x and y positions for the indicator
        x_position = bounding_box.x + bounding_box.width - offset_x  - 100 # Start from the right side of the button
        y_position = bounding_box.y + offset_y  # Start from the top side of the button

        # Draw the indicator rectangle
        pr.draw_rectangle(int(x_position), int(y_position), int(bounding_box.height), 20, self.color)  # Adjust width and height as needed
        pr.draw_rectangle(int(x_position)+int(bounding_box.width)-20, int(y_position), 20, int(bounding_box.height), self.color)

    def update_indicator_bottom_left(self, current_time, time_since_start):
        t = self.duration - time_since_start + 0.2  # Adjust the timing offset as needed
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        
        # Calculate the offset for both x and y positions
        offset_x = -t * IndicatorEvent.OFFSET_VALUE  # Move leftwards
        offset_y = t * IndicatorEvent.OFFSET_VALUE  # Move upwards

        # Calculate the x and y positions for the indicator
        x_position = bounding_box.x + bounding_box.width + offset_x  - 100 # Start from the right side of the button
        y_position = bounding_box.y + offset_y  # Start from the top side of the button

        # Draw the indicator rectangle
        pr.draw_rectangle(int(x_position), int(y_position)+int(bounding_box.height)-20, int(bounding_box.width), 20, self.color)  # Adjust width and height as needed
        pr.draw_rectangle(int(x_position), int(y_position), 20, int(bounding_box.height), self.color)

    def update_indicator_bottom_right(self, current_time, time_since_start):
        t = self.duration - time_since_start + 0.18  # Adjust the timing offset as needed
        bounding_box = self.button.get_box(edge=Edge.CONTENT, relative=False)
        
        # Calculate the offset for both x and y positions
        offset_x = -t * IndicatorEvent.OFFSET_VALUE  # Move rightwards
        offset_y = t * IndicatorEvent.OFFSET_VALUE  # Move upwards

        # Calculate the x and y positions for the indicator
        x_position = bounding_box.x + bounding_box.width - offset_x  - 100 # Start from the right side of the button
        y_position = bounding_box.y + offset_y  # Start from the top side of the button

        # Draw the indicator rectangle
        pr.draw_rectangle(int(x_position), int(y_position)+int(bounding_box.height)-20, int(bounding_box.width), 20, self.color)  # Adjust width and height as needed
        pr.draw_rectangle(int(x_position)+int(bounding_box.width)-20, int(y_position), 20, int(bounding_box.height), self.color)
