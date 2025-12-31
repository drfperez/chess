# Chess - Simple Chess Game in a Single HTML Page

A fully functional **chess game** for browsers (mobile and desktop), written in a single HTML file (lozza.html) with pure JavaScript. No server or installation required.

**Try this powerful online chess experience here:** [https://drfperez.github.io/lozza](https://drfperez.github.io/lozza)  
*(Or simply save the provided code as `index.html` and open it locally)*

## Features

- **Interactive board** with drag-and-drop pieces (powered by [chessboard.js](https://chessboardjs.com/))
- **Built-in AI engine** with 4 difficulty levels (minimax algorithm with alpha-beta pruning)
- **Play as white or black**
- **Flip the board** to view from the opponent's side
- **Move navigation** through game history (forward/backward, start/end)
- **Load and save games** in PGN format
- **Famous example game**: The legendary "Immortal Game" by Anderssen (1851) with move-by-move comments in Catalan
- **Responsive and mobile-optimized design** (full-screen, large touch-friendly buttons)
- **Minimal external dependencies** (loaded from CDNs: jQuery, chess.js, chessboard.js)

## How to Use

1. Copy the provided HTML code
2. Paste it into a new file named `index.html`
3. Open the file in any modern browser

That's it!

## Screenshots

![Chess board with mobile controls](https://github.com/drfperez/chess/raw/main/captura1.jpg)
*Compact and touch-friendly interface*

![Immortal Game with comment](https://github.com/drfperez/chess/raw/main/capture2.jpg)  
*Move-by-move comments for the famous Immortal Game*

## Technologies Used

- [chess.js](https://github.com/jhlywa/chess.js) – Chess rules engine
- [chessboard.js](https://chessboardjs.com/) – Visual board rendering
- jQuery (for chessboard.js compatibility)
- HTML5 + CSS3 + Vanilla JavaScript

## Contributions

Feel free to improve it:

- Add deeper AI (e.g., integrate Stockfish via WebAssembly)
- Translate comments to other languages
- Enhance position evaluation (piece-square tables, etc.)
- Add local two-player mode

Fork the repo, open issues, or send pull requests!

## License

This project is open source under the **MIT License**. Use, modify, and distribute freely.
# Lozza: A UCI JavaScript Chess Engine with NNUE

**Lozza** is a fully **UCI-compliant chess engine** implemented entirely in **JavaScript**.

## Core Design
*   Primarily designed for **browser execution** via Web Workers.
*   Also supports **Node.js** for use with desktop GUIs (e.g., Banksia, Winboard, Arena, CuteChess).
*   **Single-file** structure (`lozza.js`) uses code folding markers (`/*{{{ */` and `/*}}}*/`) for readability.

## Search & Evaluation
The engine drives an **alpha-beta search** enhanced with:
*   Transposition tables
*   Killer and history heuristics
*   Internal iterative deepening
*   Quiescence search with static exchange evaluation (SEE) pruning

Its core strength is a **modern NNUE-based evaluation**, featuring:
*   A **quantized compact neural network**
*   **Inlined hex-encoded weights** for efficient incremental updates during move make/unmake.
*   This NNUE replaced an earlier hand-crafted evaluation derived from Fruit 2.1.

## Release Process
Release preparation involves:
1.  Disabling development artifacts (e.g., evaluation randomization, strict mode).
2.  Setting flags like `NET_LOCAL=1` and inlining network data.
3.  Ensuring determinism via benchmarks and SPRT validation.
4.  The `BUILD` constant (e.g., "8") marks production versions.

## Project Status (as of December 2025)
| Latest Release | Lozza 8 (September 2025) |
| :--- | :--- |
| Maintenance | Latest commit November 2025 |
| GitHub Stats | 52 stars, over 1,270 commits |

This pure-JS approach prioritizes **portability** over raw speed, delivering solid performance for browser-based analysis and casual play.
---
Enjoy the game! ♔ ♚# chess
Recorded Chess Player is an online chess player using chess.js and chessboard.js libraries capable to play full previously hard coded chess games with controls. See an online working example at my website: https://pompeu.neocities.org/chess/

Python chess game codes are making use of simple AI, allowing first legal move, random legal move or priorizing capturing moves.

https://pompeu.neocities.org/chess/random

![Tauler d'escacs](https://github.com/drfperez/chess/raw/main/chess.jpg)
