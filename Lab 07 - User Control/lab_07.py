import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius, self.
                                  color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()


        arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.DARK_GREEN)

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

        # Luna
        arcade.draw_circle_filled(750, 550, 40, arcade.color.RED_BROWN)

        # Bosque

        arcade.draw_rectangle_filled(100, 230, 20, 60, arcade.csscolor.SIENNA)

        arcade.draw_polygon_filled(((100, 300),
                                    (80, 260),
                                    (70, 220),
                                    (130, 220),
                                    (120, 260)
                                    ),
                                   arcade.csscolor.DARK_GREEN)

        self.ball.draw()



    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()