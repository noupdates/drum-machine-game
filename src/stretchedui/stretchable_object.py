from typing import Callable
from stretchable import Node, Style
from stretchable.style.geometry.size import SizePoints, SizeAvailableSpace

from stretchedui.stretchable_appearance import StretchedAppearance


class StretchedObject(Node):

    def __init__(self, *children: Node,
                 appearance: StretchedAppearance = None,
                 **kwargs):
        super().__init__(*children, **kwargs)

        if appearance is None:
            RuntimeError("Appearance not instantiated")
            self.appearance = StretchedAppearance()
        else:
            self.appearance = appearance

    def construct(self):
        Warning("StretchedObject should not be instantiated directly. Instead, create a specialized child.")

    def draw(self):
        Warning("StretchedObject should not be instantiated directly. Instead, create a specialized child.")

    def update(self):
        Warning("StretchedObject should not be instantiated directly. Instead, create a specialized child.")

    def get_appearance_option(self, key, default_value=None):
        """Fetch an option from the local appearance if available; else, fallback to the default appearance."""
        # Check if the key is available in the local appearance
        if self.appearance.has_option(key):
            return self.appearance.get_option(key)
        elif self.parent:
            return self.parent.get_appearance_option(key, default_value)
        else:
            return default_value

    def set_appearance_option(self, key, value):
        self.appearance.set_option(key, value)
