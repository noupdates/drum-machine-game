import raylib as rl
import pyray as pr
from stretchable import Box


def set_shader_values(shader, values_dict):
    """Sets multiple shader values from a dictionary."""
    for name, value in values_dict.items():
        update_shader_value(shader, name, value)


def update_shader_value(shader, name, value):
    """Updates a single shader value."""
    # Get the shader location for the uniform name
    location = rl.GetShaderLocation(shader, name.encode('utf-8'))

    if isinstance(value, bool):
        # Convert boolean to integer (1 for True, 0 for False) and set as int
        int_value = rl.ffi.new("int *", int(value))
        rl.SetShaderValue(shader, location, int_value, rl.SHADER_UNIFORM_INT)

    elif isinstance(value, (float, int)):
        # If the value is a single float or int, convert it to a float pointer
        float_value = rl.ffi.new("float *", float(value))
        rl.SetShaderValue(shader, location, float_value, rl.SHADER_UNIFORM_FLOAT)

    elif isinstance(value, (list, tuple)) and len(value) == 2:
        # If the value is a 2D vector (e.g., screen size), convert to a Vector2
        vector2 = rl.ffi.new("struct Vector2 *", [float(value[0]), float(value[1])])
        rl.SetShaderValue(shader, location, vector2, rl.SHADER_UNIFORM_VEC2)

    elif isinstance(value, (list, tuple)) and len(value) == 4:
        # If the value is a 4D vector (e.g., colors), convert to a Vector4
        vector4 = rl.ffi.new("struct Vector4 *", [float(v) for v in value])
        rl.SetShaderValue(shader, location, vector4, rl.SHADER_UNIFORM_VEC4)

    elif hasattr(value, 'r') and hasattr(value, 'g') and hasattr(value, 'b') and hasattr(value, 'a'):
        # Assume this is a color-like object with r, g, b, a attributes
        vector4 = rl.ffi.new("struct Vector4 *", [
            value.r / 255.0,
            value.g / 255.0,
            value.b / 255.0,
            value.a / 255.0
        ])
        rl.SetShaderValue(shader, location, vector4, rl.SHADER_UNIFORM_VEC4)

    else:
        # Add other types or raise an error for unsupported types
        print(f"Unsupported shader value type for {name}: {type(value)}")


def pr_to_glsl_color(color: pr.Color):
    return [
        color.r / 255.0,
        color.g / 255.0,
        color.b / 255.0,
        color.a / 255.0
    ]


def stretchable_box_to_rect(box: Box):
    return pr.Rectangle(
        int(box.x),
        int(box.y),
        int(box.width),
        int(box.height)
    )
