from typing import Callable
import pyray as pr
from stretchable import Node, Style, Edge
from stretchable.style.geometry import LengthPoints
from stretchable.style.geometry.size import SizePoints, SizeAvailableSpace

from stretchedui import utils
from stretchedui.stretchable_object import StretchedObject

from stretchedui.stretchable_appearance import StretchedAppearance


class StretchedButtonAppearance(StretchedAppearance):
    defaults = {
        "foregroundColor": pr.Color(255, 255, 255, 255),
        "hoverColor": pr.Color(150, 150, 150, 255),
        "actionColor": pr.Color(100, 100, 100, 255),
        "font": pr.get_font_default(),  # Default font
        "fontSize": 20,  # Default font size
        "shader": "res/shaders/default_button.fs",
        "backgroundTexture": "res/imgs/default_ui.png"
    }

    def __init__(self, **kwargs):
        # Merge button-specific defaults with any provided kwargs
        combined_options = {**self.defaults, **kwargs}

        # Initialize with combined options
        super().__init__(**combined_options)

    def supports_option(self, option_name):
        if option_name in self.defaults:
            return True
        else:
            return StretchedAppearance.supports_option(self, option_name)


class StretchedButton(StretchedObject):

    def __init__(self, *children: Node,
                 text: str = "",
                 pressed_func: Callable[[], None] = None,
                 appearance: StretchedButtonAppearance = None,
                 **kwargs):
        # Use StretchedButtonAppearance as the default appearance if none is provided
        super().__init__(*children, measure=self.measure_text if text else None,
                         appearance=appearance if appearance else StretchedButtonAppearance(), **kwargs)

        # Set text directly, other attributes are set from appearance or provided kwargs
        self.text = text
        self.font_size = self.get_appearance_option("fontSize")
        self.color = self.get_appearance_option("foregroundColor")
        self.font = self.get_appearance_option("font")
        self.hover_color = self.get_appearance_option("hoverColor")
        self.action_color = self.get_appearance_option("actionColor")
        self.background_texture = pr.load_texture(
            self.get_appearance_option("backgroundTexture")) if self.get_appearance_option(
            "backgroundTexture") else None
        self.shader = pr.load_shader("", self.get_appearance_option("shader"))
        self.pressed_func = pressed_func

    def construct(self):
        if self.shader:
            bounding_box = self.get_box(edge=Edge.BORDER, relative=False)
            shader_values = {
                "boundingBox": (bounding_box.width, bounding_box.height),
                "backgroundColor": utils.pr_to_glsl_color(self.color),
                "hoverColor": utils.pr_to_glsl_color(self.hover_color),
                "actionColor": utils.pr_to_glsl_color(self.action_color),
                "isHovering": False,
                "isActing": False,
                "time": 0.0,
                "opacity": 1
            }
            # Set shader values based on the dictionary
            utils.set_shader_values(self.shader, shader_values)
            utils.set_shader_values(self.shader, self.appearance.get_all_options())

    def draw(self):
        # Determine if the button is being hovered or pressed
        bounding_box = self.get_box(Edge.BORDER, relative=False)
        inner_bounding_box = self.get_box(Edge.CONTENT, relative=False)
        inner_bounding_box_rect = utils.stretchable_box_to_rect(inner_bounding_box)
        is_hovering = pr.check_collision_point_rec(
            pr.get_mouse_position(),
            inner_bounding_box_rect,
        )
        is_acting = is_hovering and pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT)

        # Set the initial color based on the appearance or provided value

        if is_hovering and pr.is_mouse_button_released(pr.MouseButton.MOUSE_BUTTON_LEFT) and self.pressed_func:
            self.pressed_func()

        utils.update_shader_value(self.shader, "opacity", self.get_appearance_option("opacity", 1))

        # Draw the button text
        if self.shader and self.background_texture:
            pr.begin_shader_mode(self.shader)
            utils.update_shader_value(self.shader, "time", pr.get_time())
            utils.update_shader_value(self.shader, "isHovering", is_hovering)
            utils.update_shader_value(self.shader, "isActing", is_acting)

            pr.draw_texture_pro(self.background_texture,
                                pr.Rectangle(1, 1, 1, 1),
                                utils.stretchable_box_to_rect(bounding_box),
                                pr.Vector2(0, 0),
                                0,
                                pr.Color(0, 0, 0, 1))
            if self.text != "":
                pr.draw_text_ex(self.font, self.text, pr.Vector2(int(inner_bounding_box.x), int(inner_bounding_box.y)),
                                self.font_size, 0, pr.WHITE)

            pr.end_shader_mode()

        pr.draw_rectangle_lines_ex(inner_bounding_box_rect, 1, pr.GREEN)

    def measure_text(self, node, known_dimensions, available_space):
        # Measure the tex(t width using the appearance's font size
        text_width = pr.measure_text_ex(self.font, self.text, self.font_size, 0)
        return SizePoints(LengthPoints.points(text_width.x), LengthPoints.points(self.font_size))
