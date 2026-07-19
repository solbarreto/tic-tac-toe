# CLI Tic-Tac-Toe 🎮
A simple and interactive Command Line Interface (CLI) implementation of the classic Tic-Tac-Toe game, written entirely in Python. 

---

## Features
* Local multiplayer: Playable locally by two users taking turns as 'X' and 'O'.
* Robust input validation
* Automatic win detection 

## How to Run
Since it is a terminal-based game, you just need Python installed on your system.

1. Clone this repository or download the script.
2. Open your terminal.
3. Run the script using Python:
   ```bash
   python3 tic-tac_toe.py

## How to Play
The board is mapped to numbers from 1 to 9, corresponding to the grid below:
```text
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

During your turn, simply type the number of the position where you want to place your mark ('X' or 'O') and press Enter. The first player to get 3 of their marks in a row (up, down, across, or diagonally) wins!

## Code Structure
The game logic is divided into modular functions to keep the code clean and readable:

* **mostrar_tabuleiro(tab):** Renders the current state of the 3x3 grid in the terminal.
* **verificar_vitoria(tab, jogador):** Evaluates the board array to determine if the current player has met any of the winning conditions.
   
---
