from game.core.scene import Scene
from timeline.timeline import Timeline


class SceneManager:

    def __init__(self):
        self.__current_scene__: Scene = None

    def set_current_scene(self, scene: Scene) -> None:
        self.__current_scene__ = scene
        self.__current_scene__.construct()

    def get_current_scene(self) -> Scene:
        return self.__current_scene__
