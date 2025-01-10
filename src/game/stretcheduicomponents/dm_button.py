import math
from typing import Callable

import pyray as pr
from stretchable import Node, Style, Edge
from stretchable.style.geometry.size import SizePoints, SizeAvailableSpace

from stretchedui.stretchable_object import StretchedObject


class StretchedDMButton(StretchedObject):

    def __init__(self, *children: Node, key: str = None,
                 measure: Callable[["Node", SizePoints, SizeAvailableSpace], SizePoints] = None,
                 style: Style = None,
                 keyboard_key: pr.KeyboardKey = pr.KeyboardKey.KEY_ENTER,
                 db_key: int = 0,
                 pressed_func: Callable[[StretchedObject], None] = None,
                 perfect_time_start=.1,
                 perfect_time_end=.1,
                 good_time_start=.25,
                 good_time_end=.2,
                 **kwargs):
        super().__init__(*children, key=key, measure=measure, style=style, **kwargs)
        self.good_time_end = good_time_end
        self.good_time_start = good_time_start
        self.perfect_time_end = perfect_time_end
        self.perfect_time_start = perfect_time_start
        self.db_key = db_key
        self.keyboard_key = keyboard_key
        self.press_window_size = .1
        self.indicator_time = 2.
        self.pressed_func = pressed_func
        self.button_color = (255, 255, 255, 255)
        self.default_button_color = (255, 255, 255, 255)
        self.miss_button_color = (255, 0, 0, 255)
        self.hit_button_color = (0, 255, 0, 255)
        self.perfect_hit_button_color = (0, 0, 255, 255)
        self.button_timer = 0.0

        self.score = 0

    def draw(self):
        bounding_box = self.get_box(edge=Edge.BORDER, relative=False)

        if pr.is_key_pressed(self.keyboard_key):
            self.pressed_func(self)
            self.button_timer = 0.

        self.button_timer += pr.clamp(pr.get_frame_time(), 0., 1.)
        self.button_color = tuple(int(c2 + (c1 - c2) * self.button_timer) for c1, c2 in
                                  zip(self.default_button_color, self.button_color))

        pr.draw_circle(int(bounding_box.x + bounding_box.width / 2),
                       int(bounding_box.y + bounding_box.height / 2),
                       int(bounding_box.width / 2),
                       self.button_color)

        pr.draw_circle_sector(
            pr.Vector2(int(bounding_box.x + bounding_box.width / 2),
                       int(bounding_box.y + bounding_box.height / 2)),
            int(bounding_box.width / 2),
            math.degrees(-math.pi/2 - self.good_time_start * math.pi),
            math.degrees(-math.pi/2 + self.good_time_end * math.pi),
            10,
            pr.GREEN
        )
        pr.draw_circle_sector(
            pr.Vector2(int(bounding_box.x + bounding_box.width / 2),
                       int(bounding_box.y + bounding_box.height / 2)),
            int(bounding_box.width / 2),
            math.degrees(-math.pi/2 - self.perfect_time_start * math.pi),
            math.degrees(-math.pi/2 + self.perfect_time_end * math.pi),
            10,
            pr.BLUE
        )

        pr.draw_circle(int(bounding_box.x + bounding_box.width / 2),
                       int(bounding_box.y + bounding_box.height / 2),
                       int(bounding_box.width / 2 - 40),
                       self.button_color)
        
        pr.draw_rectangle(int(bounding_box.x), int(bounding_box.y), int(bounding_box.width), int(bounding_box.height), self.button_color)
        
    def hit(self):
        self.button_color = self.hit_button_color

    def perfect_hit(self):
        self.button_color = self.perfect_hit_button_color

    def miss(self):
        self.button_color = self.miss_button_color
