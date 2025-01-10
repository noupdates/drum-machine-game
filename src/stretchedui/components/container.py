from typing import Callable
import pyray as pr
from stretchable import Node, Style, Edge
from stretchable.style.geometry.size import SizePoints, SizeAvailableSpace
from stretchedui import utils
from stretchedui.stretchable_appearance import StretchedAppearance
from stretchedui.stretchable_object import StretchedObject


class StretchedContainerAppearance(StretchedAppearance):
    # Class-level default context
    default_appearance = None

    defaults = {
        "backgroundColor": pr.Color(50, 50, 50, 255),  # Default background color
        "borderColor": pr.Color(200, 200, 200, 255),  # Default border color
        "backgroundShader": "res/shaders/default_ui.fs",
        "backgroundTexture": None
    }
    def __init__(self, **kwargs):

        # Merge container-specific defaults with any provided kwargs
        combined_options = {**StretchedContainerAppearance.defaults, **kwargs}

        # Initialize with combined options
        super().__init__(**combined_options)

    def supports_option(self, option_name):
        if option_name in self.defaults:
            return True
        else:
            return StretchedAppearance.supports_option(self, option_name)


class StretchedContainer(StretchedObject):
    def __init__(self, *children: Node,
                 appearance: StretchedContainerAppearance = None,
                 **kwargs):
        super().__init__(*children, appearance=appearance if appearance else StretchedContainerAppearance(), **kwargs)

        # Set component-specific attributes using the get_ui_context_option method
        self.background_color = self.get_appearance_option("backgroundColor")
        self.border_color = self.get_appearance_option("borderColor")
        self.shader = pr.load_shader("", self.get_appearance_option("backgroundShader"))
        self.background_texture = self.get_appearance_option("backgroundTexture")
        self.background_texture_rect = pr.Rectangle(0, 0, 3, 3)

    def construct(self):
        if self.shader:
            bounding_box = self.get_box(edge=Edge.BORDER, relative=False)
            shader_values = {
                "boundingBox": (bounding_box.width, bounding_box.height),
                "backgroundColor": utils.pr_to_glsl_color(self.background_color),
                "borderColor": utils.pr_to_glsl_color(self.border_color),
                "time": 0.0
            }
            # Set shader values based on the dictionary
            utils.set_shader_values(self.shader, shader_values)

    def draw(self):
        bounding_box = self.get_box(edge=Edge.PADDING, relative=False)
        bounding_box_border = self.get_box(edge=Edge.BORDER, relative=False)
        content_rect = pr.Rectangle(int(bounding_box.x),
                                    int(bounding_box.y),
                                    int(bounding_box.width),
                                    int(bounding_box.height))
        border_rect = pr.Rectangle(int(bounding_box_border.x),
                                   int(bounding_box_border.y),
                                   int(bounding_box_border.width),
                                   int(bounding_box_border.height))
        if self.shader and self.background_texture:
            pr.begin_shader_mode(self.shader)
            utils.update_shader_value(self.shader, "time", pr.get_time())
            pr.draw_texture_pro(self.background_texture,
                                pr.Rectangle(1, 1, 1, 1),
                                border_rect,
                                pr.Vector2(0, 0),
                                0,
                                pr.WHITE)

            pr.draw_texture_pro(self.background_texture,
                                pr.Rectangle(1, 1, 1, 1),
                                content_rect,
                                pr.Vector2(0, 0),
                                0,
                                pr.WHITE)
            pr.end_shader_mode()

        pr.draw_rectangle_lines_ex(content_rect, 1, pr.RED)
        pr.draw_rectangle_lines_ex(border_rect, 1, pr.BLUE)

