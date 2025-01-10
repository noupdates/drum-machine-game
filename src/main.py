import pyray as pr
from raylib import FLAG_WINDOW_RESIZABLE

from game import config
from game.core.game_services import ServiceManager
from stretchedui import utils
from stretchedui.components.button import StretchedButtonAppearance

from stretchedui.components.container import StretchedContainerAppearance
from stretchedui.components.text import StretchedTextAppearance

pr.set_config_flags(FLAG_WINDOW_RESIZABLE)
pr.set_target_fps(60)

pr.init_window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, "Drum Machine")

ServiceManager.initialize_services()

resource_manager = ServiceManager.get_instance().get_resources_manager()

default_font = pr.load_font_ex(
    resource_manager.get_fonts_path("Orbitron-ExtraBold.ttf"), 128, None, 0)
pr.set_texture_filter(default_font.texture, 1)

StretchedButtonAppearance.set_default_options({
    "foregroundColor": pr.Color(238, 196, 97, 255),
    "hoverColor": pr.Color(238, 240, 125, 255),
    "actionColor": pr.Color(238, 196, 97, 255),
    "shader": resource_manager.get_shaders_path(
        "default_button.fs"),
    "font": default_font,
    "fontSize": 128
})

StretchedTextAppearance.set_default_options({
    "foregroundColor": pr.Color(195, 222, 247, 255),
    "shader": resource_manager.get_shaders_path(
        "default_ui.fs"),
    "font": default_font,
    "fontSize": 128,
})

StretchedContainerAppearance.set_default_options({
    "backgroundShader": resource_manager.get_shaders_path(
        "default_ui.fs"),
    "backgroundTexture": pr.load_texture(
        resource_manager.get_imgs_path("default_ui.png")),
    "backgroundColor": pr.Color(0, 0, 0, 0),
    "foregroundColor": pr.Color(0, 0, 0, 0),
})

main_menu_background_shader = pr.load_shader("",
                                             resource_manager.get_shaders_path(
                                                 "main_menu_background.fs")
                                             )
utils.set_shader_values(main_menu_background_shader, {
    "boundingBox": (pr.get_screen_width(), pr.get_screen_height()),
    "time": 0
})

from game.scenes import scene_map

pr.init_audio_device()

scene_manager = ServiceManager.get_instance().get_scene_manager()
scene_manager.set_current_scene(scene_map.MAIN_MENU_SCENE_CLASS())

ui_texture_target = pr.load_render_texture(pr.get_screen_width(), pr.get_screen_height())

one_x_one_texture = pr.load_texture(resource_manager.get_imgs_path("onexone.png"))
one_x_one_source_rect = pr.Rectangle(0, 0, 1, 1)
screen_target_rect = pr.Rectangle(0, 0, pr.get_screen_width(), pr.get_screen_height())

while not pr.window_should_close():
    if pr.is_window_resized():
        ui_texture_target = pr.load_render_texture(pr.get_screen_width(), pr.get_screen_height())
        screen_target_rect = pr.Rectangle(0, 0, pr.get_screen_width(), pr.get_screen_height())

    scene_manager.get_current_scene().update()
    utils.update_shader_value(main_menu_background_shader, "time", pr.get_time())

    pr.begin_texture_mode(ui_texture_target)
    pr.clear_background(pr.BLANK)
    scene_manager.get_current_scene().draw_ui()
    pr.end_texture_mode()

    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    pr.begin_shader_mode(main_menu_background_shader)
    pr.draw_texture_pro(one_x_one_texture, one_x_one_source_rect, screen_target_rect, pr.Vector2(0, 0), 0, pr.WHITE)
    pr.end_shader_mode()

    pr.draw_texture_rec(ui_texture_target.texture, pr.Rectangle(0, 0, float(ui_texture_target.texture.width),
                                                                - float(ui_texture_target.texture.height)),
                        pr.Vector2(0, 0),
                        pr.WHITE)
    scene_manager.get_current_scene().draw()

    pr.end_drawing()
pr.close_window()
