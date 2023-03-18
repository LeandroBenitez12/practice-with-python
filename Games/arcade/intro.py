# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to Arcade"
x = 100
y = 100

# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.BLACK)

# Clear the screen and start drawing
arcade.start_render()

# Draw a blue rectangle
arcade.draw_rectangle_outline(
    SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, x, y, arcade.color.BLUE
)

# Draw a yellow rectangle
arcade.draw_rectangle_outline(
    600, SCREEN_HEIGHT / 2, x, y, arcade.color.YELLOW
)

# Finish drawing
arcade.finish_render()

# muestra ventana
arcade.run()