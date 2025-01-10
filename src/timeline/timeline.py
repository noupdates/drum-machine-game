from typing import Callable, Optional


class Event:
    def __init__(
            self,
            start_time: float,
            end_time: float,
            on_start: Optional[Callable[[], None]] = None,
            on_update: Optional[Callable[[float, float], None]] = None,
            on_end: Optional[Callable[[], None]] = None
    ) -> None:
        self.start_time: float = start_time
        self.end_time: float = end_time
        self.is_active: bool = False

        # Default to no-op functions if not provided
        self.on_start: Callable[[], None] = on_start if on_start else lambda: None
        self.on_update: Callable[[float, float], None] = on_update if on_update else lambda c, t: None
        self.on_end: Callable[[], None] = on_end if on_end else lambda: None

    def update(self, current_time: float) -> None:
        """This method gets called when the event is active."""
        if self.start_time <= current_time <= self.end_time:
            if not self.is_active:
                self.on_start()
                self.is_active = True
            time_since_start = current_time - self.start_time
            self.on_update(current_time, time_since_start)
        elif self.is_active and current_time > self.end_time:
            self.on_end()
            self.is_active = False

    @staticmethod
    def from_functions(
            start_time: float,
            end_time: float,
            on_start: Optional[Callable[[], None]] = None,
            on_update: Optional[Callable[[float, float], None]] = None,
            on_end: Optional[Callable[[], None]] = None
    ) -> 'Event':
        """Static method to create an event from lambda functions."""
        return Event(
            start_time=start_time,
            end_time=end_time,
            on_start=on_start,
            on_update=on_update,
            on_end=on_end
        )


class Timeline:
    def __init__(self) -> None:
        self.events: list[Event] = []
        self.current_time: float = 0.0
        self.is_running: bool = False
        self.is_paused: bool = False
        self.pause_time: Optional[float] = None  # The time at which the timeline was paused
        self.start_time: Optional[float] = None  # The time the timeline was started

    def add_event(self, event: Event) -> None:
        """Adds an event to the timeline."""
        self.events.append(event)

    def get_current_events(self) -> list[Event]:
        """Returns a list of currently active events."""
        return [event for event in self.events if event.start_time <= self.current_time <= event.end_time]

    def start(self) -> None:
        """Start the timeline."""
        if not self.is_running:
            self.is_running = True
            self.is_paused = False
            self.start_time = self.current_time  # Start from the current time
            print(f"Timeline started at time {self.current_time}")

    def stop(self) -> None:
        """Stop the timeline."""
        self.is_running = False
        self.is_paused = False
        self.current_time = 0.0  # Reset the time
        self.pause_time = None
        print("Timeline stopped.")

    def pause(self) -> None:
        """Pause the timeline."""
        if self.is_running and not self.is_paused:
            self.is_paused = True
            self.pause_time = self.current_time
            print(f"Timeline paused at time {self.current_time}")

    def resume(self) -> None:
        """Resume the timeline from where it was paused."""
        if self.is_paused:
            self.is_paused = False
            print(f"Timeline resumed at time {self.current_time}")

    def set_time(self, new_time: float) -> None:
        """Manually set the current time of the timeline."""
        self.current_time = new_time
        print(f"Timeline time set to {self.current_time}")
        self.update(0.0)  # Update events without advancing time

    def update(self, delta_time: float) -> None:
        """Update the timeline's current time and propagate updates to events."""
        if self.is_running and not self.is_paused:
            self.current_time += delta_time  # Move time forward by delta
            for event in self.events:
                event.update(self.current_time)
