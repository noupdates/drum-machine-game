from stretchable.style import PCT, PT, Display, JustifyContent, \
    AlignSelf, JustifySelf, FlexDirection, AlignItems, GridPlacement, AlignContent
import pyray as pr

from game.core.data_manager import DataManager, RunDetails
from game.core.game_services import ServiceManager
from game.scenes import scene_map
from stretchedui.components.button import StretchedButton, StretchedButtonAppearance
from stretchedui.components.container import StretchedContainer, StretchedContainerAppearance
from game.core.ui_scene import UIScene
from stretchedui.components.text import StretchedText, StretchedTextAppearance
from timeline.timeline import Timeline


class EndGameScene(UIScene):

    def __init__(self, run_id: int):
        super().__init__()
        dm: DataManager = ServiceManager.get_instance().get_data_manager()

        run_details: RunDetails = dm.get_run_details(run_id)
        song = run_details['song']
        self.current_song_id = song['song_id']

        score_details = StretchedContainer(
            display=Display.FLEX,
            flex_grow=1,
            margin=[0, 48 * PT, 0, 48 * PT],
            align_items=AlignItems.CENTER,
            flex_direction=FlexDirection.COLUMN,
            justify_content=JustifyContent.CENTER,
        ).add(
            StretchedText(
                key="artist_name",
                text=f"{run_details['song']['artist']} - {run_details['song']['name']}",
                appearance=StretchedTextAppearance(fontSize=2 * 48),
                align_self=AlignSelf.CENTER,
                margin=[0, 48 * PT, 0, 0]
            ),
            StretchedText(
                key="score_display",
                text=f"Score: {run_details['score']}",
                appearance=StretchedTextAppearance(fontSize=4 * 48),
                margin=[0, 0, 48 * PT, 0]
            ),
            StretchedContainer(
                display=Display.FLEX,
                flex_direction=FlexDirection.COLUMN,
                align_items=AlignItems.START,
            ).add(
                StretchedText(
                    text=f"Hits: {run_details['hits']}",
                    key="score_hits",
                    appearance=StretchedTextAppearance(fontSize=2 * 48),
                ),
                StretchedText(
                    key="score_misses",
                    text=f"Misses: {run_details['misses']}",
                    appearance=StretchedTextAppearance(fontSize=2 * 48),
                    margin=[0, 48 * PT, 0, 0]
                ),

            )
        )

        self.add_stretched_object(
            StretchedContainer(
                size=(100 * PCT, 100 * PCT),
                display=Display.FLEX,
                padding=3 * 48 * PT,
                flex_direction=FlexDirection.COLUMN
            ).add(
                score_details,
                StretchedContainer(
                    display=Display.FLEX,
                    flex_direction=FlexDirection.ROW,
                    align_self=AlignSelf.STRETCH,
                    justify_content=JustifyContent.SPACE_BETWEEN
                ).add(
                    StretchedButton(
                        key="main_menu",
                        text=f"Main Menu",
                        pressed_func=lambda: ServiceManager.get_instance().get_scene_manager().set_current_scene(
                            scene_map.MAIN_MENU_SCENE_CLASS())
                    ),
                    StretchedButton(
                        text="Retry",
                        key="retry_button",
                        pressed_func=lambda: self.retry(),
                        align_self=AlignSelf.END,
                    )
                )
            )
        )

        self.currentScore = 0
        self.timeline = Timeline()

    def retry(self):
        ServiceManager.get_instance().get_scene_manager().set_current_scene(
            scene_map.GAME_SCENE_CLASS(self.current_song_id))


