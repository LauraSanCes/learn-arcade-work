"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)

arcade.open_window(800, 600, "Drawing Example")

def bosque(x, y):

    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_rectangle_filled(100 + x, 230 + y, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(((100 + x, 300 + y),
                                (80 + x, 260 + y),
                                (70 + x, 220 + y),
                                (130 + x, 220 + y),
                                (120 + x, 260 + y)
                                ),
                               arcade.csscolor.DARK_GREEN)

def ovni():


    # --- Dibujo ovni ---
    arcade.draw_lrtb_rectangle_filled(400, 600, 210, 170, arcade.color.GRAY)
    arcade.draw_lrtb_rectangle_filled(300, 700, 350, 250, arcade.color.GRAY)
    arcade.draw_circle_filled(500, 290, 65, arcade.color.DARK_SLATE_BLUE)
    arcade.draw_lrtb_rectangle_filled(250, 750, 250, 210, arcade.color.BLUE_GRAY)
    arcade.draw_circle_filled(300, 230, 20, arcade.color.DARK_YELLOW)
    arcade.draw_circle_filled(370, 230, 20, arcade.color.DARK_YELLOW)
    arcade.draw_circle_filled(440, 230, 20, arcade.color.DARK_YELLOW)
    arcade.draw_circle_filled(510, 230, 20, arcade.color.DARK_YELLOW)
    arcade.draw_circle_filled(580, 230, 20, arcade.color.DARK_YELLOW)
    arcade.draw_circle_filled(650, 230, 20, arcade.color.DARK_YELLOW)
    arcade.draw_circle_filled(720, 230, 20, arcade.color.DARK_YELLOW)

def luna():
    # Luna
    arcade.draw_circle_filled(750, 550, 40, arcade.color.RED_BROWN)


def main():
            # Set the background color
            arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
            # Get ready to draw
            arcade.start_render()
            # Draw the grass
            arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.DARK_GREEN)

            ovni()
            luna()
            bosque(50,50)


            # --- Finish drawing ---
            arcade.finish_render()
            # Keep the window up until someone closes it.
            arcade.run()


main()