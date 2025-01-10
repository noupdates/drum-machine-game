import pyray as pr
from stretchable import Node
from stretchable.style import PCT

from game.core.game_services import ServiceManager
from game.core.scene import Scene
from game.scenes import scene_map
from stretchedui.stretchable_object import StretchedObject
from timeline.timeline import Timeline, Event


class UIScene(Scene):

    def __init__(self):
        super().__init__()
        self.root = StretchedObject(
            size=(100 * PCT, 100 * PCT)
        )
        self.currentScore = 0
        self.switchSceneTimeline = Timeline()
        self.fadeInTimeline = Timeline()

        self.fadeInTimeline.add_event(
            Event.from_functions(0,
                                 .25,
                                 None,
                                 lambda ct, pt: self.root.set_appearance_option("opacity", pt * 4),
                                 lambda: self.root.set_appearance_option("opacity", 1))
        )


    def construct(self):
        self.root.compute_layout(available_space=(pr.get_screen_width(), pr.get_screen_height()))
        self.construct_recursively(self.root)

        self.fadeInTimeline.start()

    def construct_recursively(self, node):
        for child in node.find("./"):
            child.construct()
            self.construct_recursively(child)

    def update(self):
        if self.switchSceneTimeline.is_running:
            self.switchSceneTimeline.update(pr.get_frame_time())
        if self.fadeInTimeline.is_running:
            self.fadeInTimeline.update(pr.get_frame_time())

    def switch_scene(self, scene_class):
        self.switchSceneTimeline.add_event(
            Event.from_functions(0,
                                 .25,
                                 None,
                                 lambda ct, pt: self.root.set_appearance_option("opacity", 1 - pt * 4),
                                 lambda: ServiceManager.get_instance().get_scene_manager().set_current_scene(
                                     scene_class())
                                 )
        )
        self.switchSceneTimeline.start()

    def add_stretched_object(self, stretched_object):
        self.root.add(stretched_object)

    def draw_ui(self):
        if pr.is_window_resized():
            self.root.mark_dirty()
            self.root.compute_layout(available_space=(int(pr.get_screen_width()), int(pr.get_screen_height())))

        self.draw_ui_components_recursively(self.root)

    def draw_ui_components_recursively(self, node):
        for child in node.find("./"):
            child.draw()
            self.draw_ui_components_recursively(child)
