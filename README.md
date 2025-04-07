# Conway's Game of Life 🦕

Welcome to the Conway's Game of Life implementation! This is a cellular automaton devised by John Conway, which simulates the lives and interactions of cells in a grid-like universe.

## Features 🎮
- **Vibrant Pixel Art**: Enjoy a colorful and lively pixel art interface.
- **Customizable Gameplay**: Change cell colors, background, and speed to your liking.
- **Control Your Universe**: Save and load game states, or randomize the board to start a new.
- **Interactivity**: Use your mouse to add or remove cells in real-time.
- **Preloaded Configurations**: Explore complex structures with preloaded boards such as glider, gosper glider gun, and pulsar.

## Controls 🕹️
- `C`: Change cell color
- `B`: Change background color
- `W`: Reset colors to default
- `S`: Save game state
- `L`: Load game state
- `UP ARROW`: Increase speed
- `DOWN ARROW`: Decrease speed
- `R`: Randomize board
- `P`: Pause or resume the game
- `1`, `2`, `3`: Load specific board configurations
- `ESCAPE`: Return to the previous screen
- `LEFT MOUSE`: Add cell
- `RIGHT MOUSE`: Remove cell

You can also refer to the included `key_commands.png` for the list of keyboard and mouse controls in the form of table.

## Quick Start 💾
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the game: `python main.py`

## Credits and Acknowledgments 🌟
- Background art designed by AI provided in `background_image_1.png`.
- Custom pixel font utilized from `pixel_font.ttf`.
- Game logic and UI handled by `game.py` and `gui_helpers.py`.
- Preconfigured boards and game settings can be loaded with `board_loader.py`.
