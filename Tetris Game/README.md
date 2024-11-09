This is a Python implementation of a classic Tetris game using the pygame library. Here’s an overview of how it works:

Overview of Code Structure

Game Constants:
shapes and shapeColors define the block shapes and their corresponding colors.
Window dimensions, game area dimensions, and block size are also defined for easy customization.

Block Class:
Represents individual Tetris blocks with properties like position, type, color, and rotation.

Methods:
image(): Retrieves the current shape of the block.
rotate(): Rotates the block.

Tetris Game Class:
Initializes the game board, generates new blocks, manages block movements, and handles row clearing.

Methods:
new_block(), next_block(): Create current and next blocks.
intersects(): Checks if a block collides with the board boundaries or other blocks.
break_lines(): Clears full lines and increments the score.
freeze(): Fixes blocks in place once they reach the bottom or stack on top of others.
go_down(), moveBottom(), moveDown(), moveHoriz(), rotate(): Handle block movement and rotation.
draw_next_block(): Displays the upcoming block on the screen.

Game Loop (startGame):
Manages frame updates, block movements, and player input.
Draws the game board, blocks, and score in real time.

Main Menu:
Shows a "Press any key to begin!" screen before starting the game.

Game Controls
Arrow Keys: Control block movement and rotation:
UP: Rotate
DOWN: Move Down
LEFT: Move Left
RIGHT: Move Right
Space: Drop block to the bottom
ESC: Reset the game when it's over
Key Features
Scoring: Increases when lines are cleared, and is displayed at the top.

Next Block Preview: Shows the shape of the upcoming block.
Game Over Screen: When blocks stack to the top, the game ends with a "Game Over" message and prompt to press ESC to restart.


This code provides a foundational Tetris game that’s enjoyable and modifiable, using essential techniques for managing graphics and game mechanics in pygame.
