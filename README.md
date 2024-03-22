# Bodvar - Go Bot for Sabaki GUI

Bodvar is a simple Go bot implemented in Python, designed to play the ancient board game of Go. It's specifically developed to interface with the Sabaki GUI, providing a playable opponent for Go enthusiasts. This bot utilizes a combination of random moves and simple strategies to play the game.

## Features

- **Random Moves:** Bodvar can generate random moves on the Go board, providing a basic level of gameplay.
- **Simple Strategies:** It employs basic strategies such as:
  - Capturing opponent's stones by surrounding them.
  - Saving its own groups of stones by creating liberties.
  - Defending its groups to prevent capture.
  - Surrounding opponent's groups to limit their options.
  - Extending its own stone groups by occupying adjacent empty spaces.
  - Pattern matching to identify strategic opportunities based on board configurations.
- **Interface with Sabaki GUI:** Bodvar is compatible with the Sabaki GUI, allowing users to play against it within the Sabaki environment.

## Requirements

- Python 3.x
- Sabaki GUI

## Installation and Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/bodvar-go-bot.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd bodvar-go-bot
    ```

3. Ensure you have Python installed on your system.

4. Open the Sabaki GUI and set up a new game with Bodvar as one of the players.

## Configuration with Sabaki GUI

1. **Open Sabaki GUI:** Launch the Sabaki GUI application on your computer.

2. **Set Up a New Game:**
   - Click on "File" in the menu bar.
   - Select "New Game" from the dropdown menu.

3. **Configure Players:**
   - In the new game window, you will see options to configure players.
   - For Bodvar as one of the players, you'll typically set it up as the AI opponent.
   - Choose "AI" or "Engine" as the player type for Bodvar.

4. **Select Bodvar:**
   - After choosing AI or Engine, you'll have an option to select the engine.
   - Navigate to the location where you have Bodvar installed.
   - Select the `bodvar.py` script.

5. **Configure Settings (Optional):**
   - Depending on your preferences, you can configure various settings such as board size, komi, etc.
   - Adjust these settings according to your desired gameplay experience.

6. **Start the Game:**
   - Once everything is configured, click on "Start" or "OK" to begin the game.
   - Sabaki will initialize the game with Bodvar as one of the players, and you can start playing against it.

7. **Play Against Bodvar:**
   - Sabaki will handle the communication between you and Bodvar.
   - Make your moves on the Go board through the Sabaki interface, and Bodvar will respond accordingly.

8. **Enjoy the Game!:**
   - Have fun playing against Bodvar in Sabaki GUI!


2. Follow the prompts from the Sabaki GUI to start and play the game against Bodvar.

## Commands

Bodvar understands a subset of GTP (Go Text Protocol) commands for communication with the Sabaki GUI. These commands include:

- `protocol_version`: Responds with the GTP protocol version.
- `name`: Responds with the name of the bot.
- `version`: Responds with the version of the bot.
- `list_commands`: Lists the supported GTP commands.
- `boardsize`: Sets the size of the Go board.
- `clear_board`: Clears the Go board.
- `showboard`: Displays the current state of the Go board.
- `play`: Makes a move on the Go board.
- `genmove`: Generates a move for the bot.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
