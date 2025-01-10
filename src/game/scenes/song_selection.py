from stretchable.style import PCT, PT, Display, JustifyContent, \
    AlignSelf, JustifySelf, FlexDirection, AlignItems, GridPlacement, AlignContent
import pyray as pr

from game.core.data_manager import DataManager
from game.core.game_services import ServiceManager
from game.scenes import scene_map
from stretchedui.components.button import StretchedButton, StretchedButtonAppearance
from stretchedui.components.container import StretchedContainer, StretchedContainerAppearance
from game.core.ui_scene import UIScene
from stretchedui.components.text import StretchedText, StretchedTextAppearance
from timeline.timeline import Timeline


class StretchedSongSelection(UIScene):

    def __init__(self):
        super().__init__()
        dm: DataManager = ServiceManager.get_instance().get_data_manager()
        self.playableSongs = ServiceManager.get_instance().get_data_manager().get_all_songs()

        song = self.playableSongs[0]

        highscore = dm.get_highscore(song['id'])

        song_preview = StretchedContainer(
            display=Display.FLEX,
            # flex_grow=1,
            margin=[0, 48 * PT, 0, 48 * PT],
            align_items=AlignItems.CENTER,
            flex_direction=FlexDirection.COLUMN
        ).add(
            StretchedText(
                key="song_name_display",
                text=f"{song['artist']} - {song['name']}",
                appearance=StretchedTextAppearance(fontSize=4 * 48),
                margin=[0, 0, 48 * PT, 0]
            ),
            StretchedContainer(
                display=Display.FLEX,
                flex_grow=1,
            ).add(
                StretchedText(
                    key="song_difficulty_display",
                    text=f"Difficulty: Easy",
                    appearance=StretchedTextAppearance(fontSize=2 * 48),
                    align_self=AlignSelf.START,
                    margin=[0, 48 * PT, 0, 0]
                ),
                StretchedText(
                    text=f"Highscore: {highscore}",
                    key="song_highscore_display",
                    appearance=StretchedTextAppearance(fontSize=2 * 48),
                    align_self=AlignSelf.END
                ),
            )
        )
        self.selectedSongIndex = 0

        self.add_stretched_object(
            StretchedContainer(
                size=(100 * PCT, 100 * PCT),
                display=Display.FLEX,
                padding=3 * 48 * PT,
                flex_direction=FlexDirection.COLUMN
            ).add(
                StretchedContainer(
                    display=Display.FLEX,
                    flex_grow=1,
                    flex_direction=FlexDirection.ROW,
                    align_self=AlignSelf.STRETCH,
                    justify_self=JustifySelf.STRETCH,
                    justify_content=JustifyContent.CENTER,
                    align_items=AlignItems.CENTER,
                    padding=[5 * PCT, 10 * PCT]
                ).add(
                    StretchedButton(
                        key="previous_song",
                        size=[3 * 48 * PT],
                        min_size=[3 * 48 * PT],
                        appearance=StretchedButtonAppearance(
                            shader=ServiceManager.get_instance().get_resources_manager().get_shaders_path(
                                "triangle_button.fs"),
                            backgroundColor=pr.Color(238, 196, 97, 255),
                            reverse=False
                        ),
                        justify_self=JustifySelf.START
                    ),
                    song_preview,
                    StretchedButton(
                        key="previous_song",
                        size=[3 * 48 * PT],
                        min_size=[3 * 48 * PT],
                        appearance=StretchedButtonAppearance(
                            shader=ServiceManager.get_instance().get_resources_manager().get_shaders_path(
                                "triangle_button.fs"),
                            backgroundColor=pr.Color(238, 196, 97, 255),
                            reverse=True
                        ),
                        justify_self=JustifySelf.END
                    ),
                ),
                StretchedContainer(
                    display=Display.FLEX,
                    flex_direction=FlexDirection.ROW,
                    align_self=AlignSelf.STRETCH,
                    justify_content=JustifyContent.SPACE_BETWEEN
                ).add(
                    StretchedButton(
                        key="back_button",
                        text=f"Back",
                        pressed_func=lambda: ServiceManager.get_instance().get_scene_manager().set_current_scene(
                            scene_map.MAIN_MENU_SCENE_CLASS())
                    ),
                    StretchedButton(
                        text="Play",
                        key="play_button",
                        pressed_func=lambda: self.start_game(),
                        align_self=AlignSelf.END,
                    )
                )
            )
        )

        self.currentScore = 0
        self.timeline = Timeline()

    def start_game(self):
        song = self.get_current_song()
        ServiceManager.get_instance().get_scene_manager().set_current_scene(
            scene_map.GAME_SCENE_CLASS(song['id']))

    def get_current_song(self):
        return self.playableSongs[self.selectedSongIndex]
