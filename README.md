# Escacs ♔ ♚

An interactive, single-file web application for playing chess against an AI. Powered by Stockfish for expert-level play and a custom minimax algorithm for easier difficulties. Built entirely with HTML, CSS, and JavaScript—no server required. Enjoy a modern, responsive interface optimized for mobile and desktop.

## Description

Escacs (Catalan for "chess") lets you challenge a sophisticated AI in a sleek, dark-themed environment. Choose your side (white or black), adjust difficulty from beginner to grandmaster, and explore features like move navigation, PGN file handling, and annotated historical games. The app supports touch interactions for mobile play and includes bilingual (Catalan/English) instructions.

Key highlights:
- AI levels 1-5 use an optimized minimax with alpha-beta pruning and quiescence search.
- Level 6 integrates Stockfish (v10) via Web Worker for world-class strength.
- Fully offline-capable after loading (Stockfish fetched from CDN).

## Features

- **AI Opponent**: 6 difficulty levels (1-5: Custom JS AI; 6: Full Stockfish engine).
- **Game Controls**: Flip board, undo moves, start new game, save/load PGN files.
- **Move Navigation**: Jump to start/previous/next/end; displays move number and SAN notation.
- **Pawn Promotion**: Interactive modal to choose Queen, Rook, Bishop, or Knight.
- **Historical Demo**: Load the "Immortal Game" (Anderssen vs. Kieseritzky, 1851) with step-by-step comments.
- **Status Updates**: Real-time feedback on check, checkmate, draw, or thinking status.
- **Engine Indicator**: Shows active engine (Stockfish or local minimax).
- **Responsive UI**: Touch-friendly for mobile; adapts to screen size/orientation.
- **Info Modal**: Bilingual guide (Catalan/English) on controls and features.
- **No Dependencies**: Runs in any modern browser; Stockfish loaded dynamically.

## Installation

1. Download the single `stockfish/index.html` file from this repository.
2. Open it directly in your web browser (e.g., Chrome, Firefox) via `file://` or host it locally for full functionality (e.g., using `python3 -m http.server` to avoid CORS issues with Stockfish CDN).
3. Play instantly—no installation or servers needed!

## Usage

- Open the previous file and name it `escacs.html` in a browser.
- Select side (♔ White / ♚ Black) and difficulty (1-6).
- Drag pieces to move (touch on mobile).
- Use top buttons: Info (ℹ️), Flip (↻), Undo (↶), New Game (↺).
- Bottom controls: Save (💾), Load (📂), Immortal Game (★), Navigation (⏮ ◀ ▶ ⏭).
- For level 6, ensure internet for initial Stockfish load (caches afterward).

## Credits

- [chess.js](https://github.com/jhlywa/chess.js) for game logic.
- [chessboard.js](https://chessboardjs.com) for board rendering.
- [Stockfish.js](https://github.com/nmrugg/stockfish.js) for AI engine.
- Inspired by open-source chess projects.

## License

MIT License. Free to use, modify, and distribute. See [LICENSE](LICENSE) for details.
