from timeline.timeline import Event

import pyray as pr


class ButtonPressEvent(Event):

    def __init__(self, start_time, end_time, key: pr.KeyboardKey, perfect_time: float):
        super().__init__(start_time, end_time, None)

        self.perfect_time = perfect_time
        self.key = key
        self.has_pressed = False

    def button_pressed(self, pressed_key: pr.KeyboardKey, current_time: float) -> float:
        if pressed_key == self.key:
            self.has_pressed = True
            return abs(current_time - self.perfect_time)
        return -1.0
