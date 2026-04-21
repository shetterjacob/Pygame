# Danger Noodle

Danger Noodle is a Pygame Zero snake-style arcade game with three difficulty modes and obstacle mechanics.

## Project Files
- `danger_noodle.py` - main game script.
- `source_code.py` - starter code imported from the Pygame Zero snake example.
- `images/` - sprite assets used by the game.
- `music/` - background music assets.
- `sounds/` - sound effect assets.

## Game Overview
Danger Noodle is a snake-like game where the player controls a moving snake with the arrow keys.
The player selects a difficulty mode, then tries to grow the snake while avoiding collisions.

Difficulty modes:
- **Easy:** classic snake gameplay with no obstacles.
- **Medium:** adds static obstacles that end the game if touched.
- **Hard:** adds moving obstacles and a bullet boss that the snake must avoid.

Powerups appear in medium and hard modes and provide temporary invulnerability.

## How to Run
1. Install Python 3.
2. Install Pygame Zero:
   ```bash
   pip install pgzero
   ```
3. Run the game from the project root:
   ```bash
   python danger_noodle.py
   ```
   or:
   ```bash
   pgzrun danger_noodle.py
   ```
4. Use the mouse to click `EASY`, `MEDIUM`, or `HARD` to start.
5. Use the arrow keys to move the snake.
6. Close the window to quit.

## Controls
- Mouse click to select difficulty.
- Arrow keys to move the snake.
- Closing the window exits the game.

## Requirements
- Python 3.x
- `pgzero` package
- Standard library modules: `random`, `enum`, `collections`, `itertools`

## Output
- The game does not create any output files.
- All assets are loaded from the repository folders.

## Notes
- This game uses the Pygame Zero game loop and `pgzrun.go()` in `danger_noodle.py`.
- `source_code.py` is a reference starter file used during development.

## Citations
- Pope, Daniel. "pgzero -> examples -> snake". GitHub. 2017. https://github.com/lordmauve/pgzero/tree/master/examples/snake
- "Platformer Art: Extended Enemies". Kenny. 2020. https://kenney.nl/assets/platformer-art-extended-enemies
- "Bullet Bill". YAWD. 2020. https://ya-webdesign.com/explore/vector-bullet-bill/
- "Green Shell". Fandom. 2020. https://supersmashbros.fandom.com/wiki/Green_Shell
- "Star". Clipart. 2020. https://www.clipartkey.com/view/TTwwmR_super-mario-fire-power/
