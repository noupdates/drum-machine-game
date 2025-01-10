import os

class ResourcesManager:
    def __init__(self, resources_dir='resources'):
        self.base_path = resources_dir

    def get_resource_path(self, subfolder, relative_path=None):
        """Returns the full path to a resource within the given subfolder."""
        base_folder = os.path.join(self.base_path, subfolder)
        return os.path.join(base_folder, relative_path) if relative_path else base_folder

    def get_migrations_path(self, relative_path=None):
        """Returns the full path to the migrations folder or a specific file within it."""
        return self.get_resource_path('migrations', relative_path)

    def get_songs_path(self, relative_path=None):
        """Returns the full path to the songs folder or a specific file within it."""
        return self.get_resource_path('songs', relative_path)

    def get_shaders_path(self, relative_path=None):
        """Returns the full path to the shaders folder or a specific file within it."""
        return self.get_resource_path('shaders', relative_path)

    def get_imgs_path(self, relative_path=None):
        """Returns the full path to the shaders folder or a specific file within it."""
        return self.get_resource_path('imgs', relative_path)

    def get_fonts_path(self, relative_path=None):
        """Returns the full path to the shaders folder or a specific file within it."""
        return self.get_resource_path('fonts', relative_path)


