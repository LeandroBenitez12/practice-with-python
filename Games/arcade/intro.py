# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Arcade"
x_rec = 100
y_rec = 100


# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.CADET_BLUE)

# Clear the screen and start drawing
arcade.start_render()

# Draw a grid
# Draw vertical lines every 120 pixels
for x in range(0, 601, 200):
    arcade.draw_line(x, 0, x, 600, arcade.color.WHITE, 2)

# Draw horizontal lines every 200 pixels
for y in range(0, 601, 200):
    arcade.draw_line(0, y, 600, y, arcade.color.WHITE, 2)

# # Draw a blue rectangle
# arcade.draw_rectangle_outline(
#     SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, x_rec, y_rec, arcade.color.BLUE
# )

# # Draw a yellow rectangle
# arcade.draw_rectangle_outline(
#     600, SCREEN_HEIGHT / 2, x_rec, y_rec, arcade.color.YELLOW
# )

# Finish drawing
arcade.finish_render()

# muestra ventana
arcade.run()