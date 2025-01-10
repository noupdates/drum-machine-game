import pyray as pr
from stretchable.style import PCT, PT, Display, JustifyContent, \
    AlignSelf, JustifySelf, FlexDirection, AlignContent, AlignItems

from game.core.game_services import ServiceManager
from game.scenes import scene_map
from stretchedui.components.button import StretchedButton
from stretchedui.components.container import StretchedContainer, StretchedContainerAppearance
from stretchedui.components.text import StretchedText, StretchedTextAppearance
from game.core.ui_scene import UIScene
from timeline.timeline import Timeline, Event


class DMMainMenu(UIScene):

    def __init__(self):
        super().__init__()

        self.add_stretched_object(
            StretchedContainer(
                size=(100 * PCT, 100 * PCT),
                display=Display.FLEX,
                padding=3 * 48 * PT,
            ).add(
                StretchedContainer(
                    # size=(1 * FR, 1 * FR),
                    display=Display.FLEX,
                    flex_grow=1,
                    align_self=AlignSelf.STRETCH,
                    justify_self=JustifySelf.STRETCH,
                    flex_direction=FlexDirection.COLUMN,
                    justify_content=JustifyContent.START,
                    align_items=AlignItems.CENTER,
                    padding=[5 * PCT, 10 * PCT],
                    border=[10 * PT, 10 * PT],
                    # margin=[10 * PCT, 10 * PCT],
                ).add(
                    StretchedText(
                        text="DRUM MACHINE",
                        appearance=StretchedTextAppearance(fontSize=128 + 64),
                        margin=[0, 0, 3 * 48 * PT, 0]
                    ),
                    StretchedButton(
                        text="PLAY",
                        align_self=AlignSelf.CENTER,
                        padding=[1 * 48 * PT, 0, 0, 0],
                        pressed_func=lambda: self.switch_scene(scene_map.SONG_SELECTION_SCENE_CLASS)
                    ),
                    StretchedButton(
                        text="QUIT",
                        align_self=AlignSelf.CENTER,
                        padding=[1 * 48 * PT, 0, 0, 0],
                        pressed_func=lambda: pr.close_window()
                    ),
                )
            )
        )

