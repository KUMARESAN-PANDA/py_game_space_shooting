# py_game_space_shooting

A simple space shooting game built using Python and Pygame where the player avoids falling stars. The game keeps track of the elapsed time and ends when the player gets hit by a star.


## Introduction

In this game, the player controls a red rectangle that can move left or right at the bottom of the screen. Yellow "stars" fall from the top, and the goal is to avoid them for as long as possible. The game ends when a star collides with the player, and the final time survived is displayed.

## Requirements

- Python 3.x
- Pygame library

## How to Play

1. Use the **left** and **right arrow keys** to move your player (a red rectangle) across the screen.
2. Avoid the falling stars (yellow rectangles) for as long as you can.
3. The game ends when a star collides with your player.
4. Your time survived will be displayed after the game ends.

## Installation

1. Clone the repository or download the code:
    ```bash
    git clone https://github.com/KUMARESAN-PANDA/py_game_shooting.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Game
    ```

3. Install the required libraries using pip:
    ```bash
    pip install pygame
    ```

4. Ensure you have a `bg.jpg` background image in the same directory as the game script. You can use any image of your choice.

5. Run the game:
    ```bash
    python main.py
    ```

## Game Mechanics

- The player starts at the bottom of the screen and can move left and right using the arrow keys.
- Stars fall from the top at random positions and speeds. More stars are added over time to increase difficulty.
- If a star collides with the player, the game ends, and the total time survived is displayed.
- The game uses Pygame's `pygame.Rect` for the player and star objects, and the background is an image that scales to the window size.



