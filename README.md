♟️ Chess Game

A modern, feature-rich chess game built with HTML5, CSS3, and JavaScript. Play against an AI opponent with adjustable difficulty, or replay famous historical games. Supports both Standard Chess and Fischer Random (Chess960).

🎮 Live Demo

Play Now: https://drfperez.github.io/chess/stockfish/

✨ Features

🏆 Game Variants

· Standard Chess - Traditional chess with classical opening theory
· Fischer Random (Chess960) - Random starting positions with 960 possible arrangements

🤖 AI Opponent

· 6 Difficulty Levels - From beginner to expert
· Levels 1-5 - Optimized minimax algorithm with alpha-beta pruning
· Level 6 - Full Stockfish integration (world's strongest chess engine)

🎯 Game Features

· Interactive Board - Drag and drop pieces
· Smart Promotion - Choose promotion piece when pawn reaches the end
· Move History - Navigate through game history
· Save/Load Games - PGN file support
· Board Orientation - Flip board perspective
· Responsive Design - Works on desktop, tablet, and mobile

📊 Game Information

· Live Status Display - Shows current game state
· Move Counter - Tracks move numbers
· Check/Checkmate Detection - Visual and text indicators
· Draw Recognition - Automatically detects stalemate and other draws

🎮 How to Play

Quick Start

1. Choose your side (White or Black)
2. Select difficulty level (1-6)
3. Choose game variant (Standard or Fischer Random)
4. Drag pieces to make moves
5. When pawn reaches the end, select promotion piece

Controls

Top Controls:

· ℹ️ Game information and instructions
· ♔/♚ Choose your side (White/Black)
· 1-6 Difficulty level selector
· S/F Game variant selector (Standard/Fischer Random)
· ↻ Flip board orientation
· ↶ Undo last move
· ↺ Start new game

Bottom Controls:

· 💾 Save game as PGN file
· 📂 Load saved PGN game
· ★ Load the "Immortal Game" with commentary
· ⏮◀▶⏭ Navigate through move history

🔧 Technical Details

Built With

· HTML5 - Semantic markup and structure
· CSS3 - Responsive design with Flexbox/Grid
· JavaScript (ES6+) - Game logic and interactivity
· chess.js - Chess move generation and validation
· chessboard.js - Interactive chess board UI
· Stockfish.js - World-class chess engine integration

Chess960 (Fischer Random) Rules

The game implements proper Chess960 rules:

1. Two bishops must be on opposite-colored squares
2. The king must be between the two rooks
3. 960 possible starting positions
4. Castling rules adapt to the random setup
5. All standard chess rules apply after setup

Performance Features

· Optimized minimax algorithm with alpha-beta pruning
· Quiescence search for stable positions
· Move ordering for better pruning
· Responsive design for all screen sizes
· Touch-friendly interface for mobile devices

📁 Installation & Local Setup

Option 1: Direct Browser

Simply open the index.html file in any modern web browser.

Option 2: Local Server

For better performance:

```bash
# Using Python
python -m http.server 8000

# Using Node.js with http-server
npx http-server

# Using PHP
php -S localhost:8000
```

Then visit http://localhost:8000 in your browser.

🌐 Browser Compatibility

Browser Version Status
Chrome 60+ Full Support
Firefox 55+ Full Support
Safari 11+ Full Support
Edge 80+ Full Support
Opera 50+ Full Support

Mobile Support: Works on iOS Safari 11+, Android Chrome 60+

🔗 Dependencies

All dependencies are loaded from CDN:

```html
<!-- CSS -->
<link rel="stylesheet" href="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css">

<!-- JavaScript -->
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.12.0/chess.min.js"></script>
<script src="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"></script>
```

⚠️ Known Issues & Limitations

1. Stockfish Worker: The Stockfish engine loads from CDN and may be blocked by some ad blockers
2. Offline Play: AI levels 1-5 work offline; level 6 requires internet for Stockfish
3. File Saving: PGN files are saved as downloads; ensure browser allows downloads
4. Large Games: Games with 1000+ moves may experience performance issues

🚀 Future Enhancements

· Add time controls (bullet, blitz, classical)
· Implement PGN game database
· Add opening book and position analysis
· Create multiplayer (PvP) mode
· Add move hints and suggestions
· Implement position evaluation graphs
· Add chess puzzles and training mode

🙏 Acknowledgements

· chess.js - Chess logic library by Jeff Hlywa
· chessboard.js - Chess board UI library by Chris Oakman
· Stockfish - Open-source chess engine by the Stockfish team
· The Immortal Game - Historical game between Adolf Anderssen and Lionel Kieseritzky (1851)
· Bobby Fischer - For inventing Fischer Random Chess (Chess960)

📄 License

This project is licensed under the MIT License.
