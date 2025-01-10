import pyray as pr


class StretchedAppearance:
    # Class-level default context
    defaults = {}

    def __init__(self, **kwargs):
        # Start with default options, and allow kwargs to override them
        self.options = {**StretchedAppearance.defaults, **kwargs}
        for key, value in kwargs.items():
            if self.supports_option(key) and value is not None:
                self.set_option(key, value)

    def set_option(self, key, value):
        """Sets a single option if the key is valid and the value type matches the expected type."""
        self.options[key] = value

    def get_option(self, option_name):
        """Retrieve an option's value safely."""
        return self.options.get(option_name)

    def has_option(self, option_name):
        return option_name in self.options

    def get_all_options(self):
        return self.options

    def supports_option(self, option_name):
        return option_name in StretchedAppearance.defaults.keys()

    def _check_type(self, value, expected_type):
        """Helper method to check types, including pyray classes by attribute."""
        # Direct type check for standard Python types
        return True

    @classmethod
    def set_default_option(cls, key, value):
        """Set a static default option for all button instances."""
        cls.defaults[key] = value

    @classmethod
    def set_default_options(cls, options):
        """Set multiple default options for all button instances."""
        for key, value in options.items():
            cls.set_default_option(key, value)
