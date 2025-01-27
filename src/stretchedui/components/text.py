from typing import Callable

import pyray as pr
from stretchable import Node, Style, Edge
from stretchable.style.geometry import LengthPoints
from stretchable.style.geometry.size import SizePoints, SizeAvailableSpace

from stretchedui import utils
from stretchedui.stretchable_object import StretchedObject
from stretchedui.stretchable_appearance import StretchedAppearance

import pyray as pr
from stretchedui.stretchable_appearance import StretchedAppearance


class StretchedTextAppearance(StretchedAppearance):
    defaults = {
        "foregroundColor": pr.Color(0, 0, 0, 255),  # Default text color (white)
        "font": pr.get_font_default(),  # Default font
        "fontSize": 128,  # Default font size
        "textShader": None  # Default shader (none)
    }

    def __init__(self, **kwargs):

        # Merge text-specific defaults with any provided kwargs
        combined_options = {**self.defaults, **kwargs}

        # Initialize with combined options
        super().__init__(**combined_options)

    def supports_option(self, option_name):
        if option_name in self.defaults:
            return True
        else:
            return StretchedAppearance.supports_option(self, option_name)


class StretchedText(StretchedObject):

    def __init__(self, *children: Node,
                 text: str = "",
                 appearance: StretchedTextAppearance = None,
                 **kwargs):
        # Use the provided appearance or default appearance
        super().__init__(*children, measure=self.measure_text,
                         appearance=appearance if appearance else StretchedTextAppearance(), **kwargs)

        # Store the text directly, while other properties are set from appearance
        self.text = text
        self.font = self.get_appearance_option("font")
        self.font_size = self.get_appearance_option("fontSize")
        self.color = self.get_appearance_option("foregroundColor")
        self.shader = pr.load_shader("", self.get_appearance_option("shader"))


    def construct(self):
        if self.shader:
            shader_values = {
                "time": 0.0,
                "opacity": 1
            }
            # Set shader values based on the dictionary
            utils.set_shader_values(self.shader, shader_values)
            utils.set_shader_values(self.shader, self.appearance.get_all_options())


    def draw(self):
        # Retrieve bounding boxes
        inner_bounding_box = self.get_box(Edge.CONTENT, relative=False)

        utils.update_shader_value(self.shader, "opacity", self.get_appearance_option("opacity", 1))


        pr.begin_shader_mode(self.shader)
        pr.draw_text_ex(self.font, self.text, pr.Vector2(int(inner_bounding_box.x), int(inner_bounding_box.y)),
                        self.font_size, 0, pr.BLACK)
        
        if self.text == "W":
        # Use the original width for "W"
            rect = pr.Rectangle(int(inner_bounding_box.x),
                            int(inner_bounding_box.y),
                            int(inner_bounding_box.width)-5,  # No additional width for "W"
                            int(inner_bounding_box.height))
        elif self.text == "Q":
            rect = pr.Rectangle(int(inner_bounding_box.x),
                            int(inner_bounding_box.y),
                            int(inner_bounding_box.width)+26,  # No additional width for "W"
                            int(inner_bounding_box.height))
        elif self.text == "E":
            rect = pr.Rectangle(int(inner_bounding_box.x),
                            int(inner_bounding_box.y),
                            int(inner_bounding_box.width)+35,  # No additional width for "W"
                            int(inner_bounding_box.height))
        else:
            rect = pr.Rectangle(int(inner_bounding_box.x),
                                int(inner_bounding_box.y),
                                int(inner_bounding_box.width)+30,
                                int(inner_bounding_box.height))
        pr.end_shader_mode()

        pr.draw_rectangle_lines_ex(rect, 1, pr.GREEN)

    def measure_text(self, node, known_dimensions, available_space):
        # Measure the text using appearance's font size setting
        text_width = pr.measure_text_ex(self.font, self.text, self.font_size, 0)
        return SizePoints(LengthPoints.points(text_width.x), LengthPoints.points(self.font_size))
