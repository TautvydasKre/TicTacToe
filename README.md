# Tic Tac Toe Game (Python Pygame)

A classic Tic Tac Toe game built using `pygame`, where you can play against another player or an AI with basic minimax logic. 

## Features
- **Two Game Modes**: 
  - VS Player (play against a friend)
  - VS Computer (play against an AI)
- **Score Keeping**: Tracks the score between Player X and Player O.
- **Draw Handling**: After five consecutive draws, a special secret feature is unlocked in the main menu.
- **Roast Mechanism**: The AI roasts you when it wins, with over 200 custom roast messages.
- **Responsive Graphics**: The game board and figures are drawn dynamically, ensuring smooth gameplay.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tic-tac-toe-pygame.git
    ```
2. Navigate into the project directory:
    ```bash
    cd tic-tac-toe-pygame
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Play

1. Run the game:
    ```bash
    python tic-tac-toe.py
    ```
2. In the main menu, choose between:
   - **VS Player**: Play against a friend
   - **VS Computer**: Play against an AI
   - **Exit**: Quit the game
   
3. The first player to get 3 marks in a row (vertically, horizontally, or diagonally) wins the game.

4. After five consecutive draws, a secret button will appear in the main menu!

## Files and Structure

- `tic-tac-toe.py`: Main game file that runs the game loop and handles game logic.
- `modules/`: Contains different modules:
  - `draw.py`: Functions to handle drawing of the board and figures.
  - `game_logic.py`: Game logic for checking wins, draws, and resetting the board.
  - `menu.py`: Handles the main menu navigation.
  - `messages.py`: Handles display messages like win/draw screens and roasts.
  - `computer_logic.py`: AI logic for the computer opponent using the minimax algorithm.
  - `roasts.py`: Contains a list of roast messages used by the AI when it wins.
  - `roasts_logic.py`: Logic for displaying all roast messages in a scrollable view.
- `requirements.txt`: Lists the required Python libraries (pygame).

## Controls
- **Mouse Click**: Select squares and interact with menus.
- **Arrow Keys/Mouse Scroll**: Scroll through long lists, such as the roast list.
- **Escape**: Return to the main menu.

## AI Behavior
The AI uses the **minimax algorithm** to determine the best move. It tries to maximize its score while minimizing the player's score, making it a formidable opponent.

## Upcoming Features
- Add different difficulty levels for the AI.
- Add multiplayer over a network.

## License
This project is licensed under the MIT License.

## Credits
- Developed by [Tautvydas Kreivys](https://github.com/TautvydasKre)
- Roasts curated by [Tautvydas Kreivys] 
- Thanks to the [Pygame](https://www.pygame.org) community for their amazing resources!
