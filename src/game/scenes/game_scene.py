import random

import pyray as pr
from stretchable.style import PCT, PT, Display, AUTO, AlignItems, JustifyContent, GridPlacement, \
    AlignSelf, JustifySelf, Position, AlignContent

from game.core.data_manager import DataManager, SongInfo, Timing
from game.core.game_services import ServiceManager
from game.scenes import scene_map
from game.stretcheduicomponents.dm_button import StretchedDMButton
from game.stretcheduicomponents.indicator_event import IndicatorEvent
from game.stretcheduicomponents.button_press_event import ButtonPressEvent
from stretchedui.components.container import StretchedContainer, StretchedContainerAppearance
from stretchedui.components.text import StretchedText, StretchedTextAppearance
from game.core.ui_scene import UIScene
from timeline.timeline import Timeline, Event


class GameScene(UIScene):

    def __init__(self, song_id: int):
        super().__init__()

        dm: DataManager = ServiceManager.get_instance().get_data_manager()
        song_info_with_timings: SongInfo = dm.get_song_details(song_id)

        self.song_id = song_id
        self.timings: [Timing] = song_info_with_timings['timings']
        self.started = False
        self.last_frame_played_time = 0.0
        self.countdown_ready = False
        self.scoreText = StretchedText(
            text="SCORE: 0",
            align_self=AlignSelf.STRETCH,
            justify_self=JustifySelf.END,
            padding=2 * PCT
        )

        self.music_stream = pr.load_music_stream(
            ServiceManager.get_instance().get_resources_manager().get_songs_path(
                song_info_with_timings['file_location']))

        self.content = StretchedContainer(key="content",
                                          size=(AUTO, AUTO),
                                          display=Display.GRID,
                                          grid_template_columns=[2 * 48 * PT, 2 * 48 * PT, 2 * 48 * PT],
                                          grid_template_rows=[2 * 48 * PT, 2 * 48 * PT, 2 * 48 * PT],
                                          gap=4 * 9 * PT,
                                          )

        self.countdown = StretchedText(key="countdown",
                                       text="Game Starting in...",
                                       align_self=AlignSelf.CENTER,
                                       justify_self=JustifySelf.CENTER)

        self.dialog = StretchedContainer(key="dialog",
                                         size=(100 * PCT, 100 * PCT),
                                         display=Display.FLEX,
                                         justify_content=JustifyContent.CENTER,
                                         align_items=AlignItems.CENTER,
                                         position=Position.ABSOLUTE)
        self.dialog.add(
            self.countdown
        )
        self.add_stretched_object(
            StretchedContainer(
                size=(100 * PCT, 100 * PCT),
                display=Display.FLEX,
                padding=48 * PT,
                appearance=StretchedContainerAppearance(backgroundColor=pr.Color(200, 20, 50, 255))
            ).add(
                StretchedContainer(
                    # size=(1 * FR, 1 * FR),
                    display=Display.GRID,
                    flex_grow=1,
                    grid_template_rows=[10 * PCT, 90 * PCT],
                    # align_self=AlignSelf.STRETCH,
                    # justify_self=JustifySelf.STRETCH,
                    grid_template_columns=[50 * PCT, 50 * PCT]
                ).add(
                    StretchedText(
                        text=f"{song_info_with_timings['artist']} - {song_info_with_timings['name']}",
                        align_self=AlignSelf.STRETCH,
                        padding=2 * PCT,
                        appearance=StretchedTextAppearance(fontColor=pr.Color(255, 255, 255, 255))
                    ),
                    self.scoreText,
                    StretchedContainer(
                        display=Display.FLEX,
                        justify_content=JustifyContent.CENTER,
                        align_items=AlignItems.CENTER,
                        grid_row=GridPlacement.from_inline("2"),
                        grid_column=GridPlacement.from_inline("1/3"),
                        align_self=AlignSelf.STRETCH,
                        justify_self=JustifySelf.STRETCH,
                    ).add(
                        self.content
                    )
                )
            )
        )
        self.add_stretched_object(self.dialog)

        self.currentScore = 0
        self.music_timeline = Timeline()
        self.countdown_timeline = Timeline()

        self.button_presses = []

    def score(self, score: int):
        self.currentScore += score
        self.scoreText.text = f"Score: {self.currentScore}"

    def construct(self):
        indicator_window = 1.5
        press_window_start = .25
        press_window_end = .2
        song_begin_offset = 5
        num_of_keys = len(self.timings.keys())
        for (k, i, c) in zip(self.timings.keys(),
                             [pr.KeyboardKey.KEY_Q, pr.KeyboardKey.KEY_W, pr.KeyboardKey.KEY_E, pr.KeyboardKey.KEY_A,
                              pr.KeyboardKey.KEY_S, pr.KeyboardKey.KEY_D, pr.KeyboardKey.KEY_Z, pr.KeyboardKey.KEY_X,
                              pr.KeyboardKey.KEY_C][0:num_of_keys],
                             [pr.BLACK, pr.BEIGE, pr.MAROON, pr.GREEN, pr.LIME, pr.DARKGREEN, pr.ORANGE, pr.BLUE,
                              pr.YELLOW, ][0:num_of_keys]):

            # timings = sorted(random.choices(range(2, 20), k=5))
            button = StretchedDMButton(key=f'button-{i}', size=(4 * 28 * PT, 4 * 28 * PT),
                                       db_key=k,
                                       pressed_func=self.dm_button_pressed, keyboard_key=i,
                                       display=Display.FLEX)
            button.add(StretchedText(
                text=chr(i),
                align_self=AlignSelf.CENTER,
                justify_self=JustifySelf.CENTER,
                padding=2 * PCT
            ))
            for timing in self.timings.get(k):
                t = timing
                # Create IndicatorEvent with the correct button type
                if i == pr.KeyboardKey.KEY_Q:
                    button_type = 'Q'  # Left
                elif i == pr.KeyboardKey.KEY_W:
                    button_type = 'W'  # Top
                elif i == pr.KeyboardKey.KEY_E:
                    button_type = 'E'  # Right
                elif i == pr.KeyboardKey.KEY_A:
                    button_type = 'A'  # Right    
                elif i == pr.KeyboardKey.KEY_S:
                    button_type = 'S'  # Right   
                elif i == pr.KeyboardKey.KEY_D:
                    button_type = 'D'  # Right   
                elif i == pr.KeyboardKey.KEY_Z:
                    button_type = 'Z'  # Right  
                elif i == pr.KeyboardKey.KEY_X:
                    button_type = 'X'  # Right   
                elif i == pr.KeyboardKey.KEY_C:
                    button_type = 'C'  # Right     
                else:
                    button_type = 'UNKNOWN'  # Handle other keys if necessary

                self.music_timeline.add_event(
                    IndicatorEvent(t - indicator_window, t + press_window_end, t, button, color=c, button_type=button_type))
                self.music_timeline.add_event(
                    ButtonPressEvent(t - press_window_start, t + press_window_end, i, perfect_time=t))
            self.content.add(button)

                      

        self.root.compute_layout(available_space=(pr.get_screen_width(), pr.get_screen_height()))
        print(self.dialog.get_box())

        self.music_timeline.add_event(
            Event.from_functions(20 - 1.,
                                 20 + 2., None, None,
                                 lambda: self.end_game()))

        def update_countdown_text(cd_text: str) -> None:
            self.countdown.text = cd_text
            self.countdown.mark_dirty()
            self.root.compute_layout(available_space=(pr.get_screen_width(), pr.get_screen_height()))

        def start_run() -> None:
            self.dialog.remove(self.countdown)
            self.root.compute_layout(available_space=(pr.get_screen_width(), pr.get_screen_height()))
            self.countdown_ready = True
            self.countdown_timeline.stop()
            self.music_timeline.start()

        for i in range(1, song_begin_offset):
            countdown_number = song_begin_offset - i
            self.countdown_timeline.add_event(
                Event.from_functions(i,
                                     i + 1,
                                     lambda cd_text=f"{song_begin_offset - i - 1}...": update_countdown_text(cd_text))
            )

        self.countdown_timeline.add_event(
            Event.from_functions(song_begin_offset - 1,
                                 song_begin_offset, lambda: update_countdown_text("GO!"))
        )

        self.countdown_timeline.add_event(
            Event.from_functions(0,
                                 song_begin_offset, None, None,
                                 lambda: start_run()))

        self.countdown_timeline.start()

        super().construct()

    def draw(self):
        if not pr.is_music_valid(self.music_stream):
            return
        if not self.countdown_ready:
            self.countdown_timeline.update(pr.get_frame_time())
        if not self.started and self.countdown_ready:
            pr.play_music_stream(self.music_stream)
            self.started = True
        pr.update_music_stream(self.music_stream)
        self.music_timeline.update(pr.get_music_time_played(self.music_stream) - self.last_frame_played_time)
        self.last_frame_played_time = pr.get_music_time_played(self.music_stream)

    def dm_button_pressed(self, button: StretchedDMButton):
        success = False
        for event in self.music_timeline.get_current_events():
            if isinstance(event, ButtonPressEvent) and not event.has_pressed and event.key == button.keyboard_key:
                distance = event.button_pressed(button.keyboard_key, self.music_timeline.current_time)
                if distance < .1:
                    self.score(10)
                    button.perfect_hit()
                else:
                    self.score(5)
                    button.hit()
                success = True
        self.button_presses.append(
            {
                'key_id': button.db_key,
                'timing': self.music_timeline.current_time,
                'accuracy_level': 'Hit' if success else 'Miss',
            })
        if not success:
            button.miss()
            self.score(-10)

    def end_game(self):
        self.music_timeline.stop()
        pr.stop_music_stream(self.music_stream)
        run_id = ServiceManager.get_instance().get_data_manager().save_run_stats(self.song_id, self.button_presses)
        ServiceManager.get_instance().get_scene_manager().set_current_scene(
            scene_map.END_GAME_SCENE(run_id))