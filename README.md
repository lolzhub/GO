# Bodvar - the go to GO bot!

Bodvar is a simple Go bot implemented in Python, designed to play the ancient board game of Go. It's specifically developed to interface with the Sabaki GUI, providing a playable opponent for Go enthusiasts. This bot utilizes a combination of random moves and simple strategies to play the game.

## Features

### Advanced Gameplay Strategies
Bodvar is equipped with a repertoire of advanced gameplay strategies, enabling it to engage in dynamic and strategic gameplay. These strategies include:

#### 1. Stone Capture
Bodvar possesses the ability to identify vulnerable groups of opponent's stones and execute strategic moves to capture them. By surrounding opponent's stones with its own, Bodvar effectively eliminates them from the board, gaining a tactical advantage in the game.

#### 2. Stone Preservation
Recognizing the importance of preserving its own groups of stones, Bodvar employs defensive maneuvers to ensure their safety. By creating liberties within its stone formations, Bodvar fortifies its positions and prevents them from being captured by the opponent.

#### 3. Group Extension
In addition to defense, Bodvar focuses on expanding its influence on the board by extending its own stone groups. By occupying adjacent empty spaces and strategically placing stones, Bodvar increases its territory and strengthens its position, setting the stage for future strategic maneuvers.

#### 4. Strategic Analysis through Pattern Matching
Bodvar utilizes pattern matching techniques to analyze the current board configuration and identify strategic opportunities. By recognizing recurring patterns and formations, Bodvar is able to anticipate the opponent's moves and formulate effective counter-strategies, maximizing its chances of success on the board.

### Seamless Integration with Sabaki GUI
Bodvar seamlessly integrates with the Sabaki GUI, providing users with a convenient and user-friendly platform to play the game of Go. By leveraging the features of the Sabaki interface, users can enjoy a smooth and immersive gaming experience while facing off against Bodvar in challenging matches.

### Customizable Gameplay Experience
Bodvar offers a customizable gameplay experience, allowing users to tailor the game settings according to their preferences. Whether adjusting the board size, setting the komi value, or configuring other game parameters, users have the flexibility to customize their gameplay experience to suit their individual preferences and skill levels.

### Open-Source and Community-Driven Development
Bodvar is an open-source project. Contributions, feedback, and suggestions from the community play a crucial role in the ongoing development and improvement of Bodvar.

## Requirements

- Python 3.x
- Sabaki GUI

## How to Download and Install Sabaki

Sabaki is a popular open-source Go board GUI that provides a user-friendly interface for playing Go and analyzing games. Follow these steps to download and install Sabaki on your computer:

### For Windows:

1. **Download:**
   - Visit the [Sabaki Releases](https://github.com/SabakiHQ/Sabaki/releases) page on GitHub.
   - Scroll down to the latest release section.
   - Download the `.exe` installer file for the latest version. (e.g., `sabaki-setup-0.53.1.exe`)

2. **Install:**
   - Once the download is complete, double-click the installer file to start the installation process.
   - Follow the on-screen instructions to complete the installation.
   - Sabaki will be installed on your system and ready to use.

### For macOS:

1. **Download:**
   - Visit the [Sabaki Releases](https://github.com/SabakiHQ/Sabaki/releases) page on GitHub.
   - Scroll down to the latest release section.
   - Download the `.dmg` disk image file for the latest version. (e.g., `Sabaki-0.53.1.dmg`)

2. **Install:**
   - Open the downloaded `.dmg` file.
   - Drag the Sabaki application icon to the Applications folder to install it.
   - Sabaki will be installed on your Mac and ready to use.

### For Linux:

1. **Download:**
   - Visit the [Sabaki Releases](https://github.com/SabakiHQ/Sabaki/releases) page on GitHub.
   - Scroll down to the latest release section.
   - Download the `.AppImage` file for the latest version. (e.g., `sabaki-0.53.1-x86_64.AppImage`)

2. **Make Executable:**
   - Open a terminal window.
   - Navigate to the directory where you downloaded the `.AppImage` file.
   - Run the following command to make the file executable:
     ```bash
     chmod +x sabaki-0.53.1-x86_64.AppImage
     ```

3. **Run Sabaki:**
   - Double-click the `.AppImage` file to start Sabaki.
   - Alternatively, you can run Sabaki from the terminal:
     ```bash
     ./sabaki-0.53.1-x86_64.AppImage
     ```

### Additional Information:

- **Dependencies:**
  - Sabaki does not require any additional dependencies to run on Windows, macOS, or most Linux distributions.
- **System Requirements:**
  - Sabaki should run on most modern computers without issue.
- **Contribution:**
  - Sabaki is an open-source project, and contributions are welcome. Visit the [Sabaki GitHub repository](https://github.com/SabakiHQ/Sabaki) to learn more.


## Installation and Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/lolzhub/GO.git
    ```

2. Navigate to the cloned directory and verify `bodvar14.py` is present:

    ```bash
    cd GO
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
