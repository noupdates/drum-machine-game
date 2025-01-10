from typing import Self

from game.core.data_manager import DataManager
from game.core.resources_manager import ResourcesManager
from game.core.scene_manager import SceneManager


class ServiceManager:
    # Static instance variable to hold the single instance
    _instance = None

    def __init__(self):
        # Initialize instance-specific managers
        self._resources_manager = ResourcesManager(resources_dir='./res')
        self._scene_manager = SceneManager()
        self._data_manager = DataManager(migrations_folder=self._resources_manager.get_migrations_path())

    @classmethod
    def initialize_services(cls):
        # Check if an instance already exists, if not, create one
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def get_instance(cls) -> Self:
        # Return the existing instance
        return cls._instance

    # Getter for ResourcesManager
    def get_resources_manager(self):
        return self._resources_manager

    # Getter for SceneManager
    def get_scene_manager(self):
        return self._scene_manager

    # Getter for DataManager
    def get_data_manager(self):
        return self._data_manager
