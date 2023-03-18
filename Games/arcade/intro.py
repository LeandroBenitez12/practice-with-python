# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Welcome to Arcade"
x = 200
y = 200
# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.BLACK)

# Clear the screen and start drawing
arcade.start_render()

# Draw a blue circle
arcade.draw_rectangle_filled(
    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, x, y, arcade.color.BLUE
)

# Finish drawing
arcade.finish_render()

# Display everything
arcade.run()