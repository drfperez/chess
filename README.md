# ♟️ Chess — Browser-Based Chess Game with JavaScript AI

A **fully featured chess game for the browser**, built with **HTML, CSS, and pure JavaScript**, running **100% client-side** with **no server required**.

The project is designed to work seamlessly on **desktop and mobile devices** and includes a built-in **AI opponent**, **PGN support**, and a fully annotated version of the **Immortal Game (1851)**.

---

## 🚀 Features

- ♞ **Play against the AI**
  - Configurable difficulty levels (1–5)
  - Minimax algorithm with alpha-beta pruning
- 📱 **Responsive design**
  - Optimized for touch screens
  - Mobile-first controls
- 🔄 **Board controls**
  - Flip board orientation
  - Undo moves
  - Navigate through the entire game
- 💾 **Game management**
  - Save games in PGN format
  - Load external PGN files
- ⭐ **Immortal Game included**
  - Anderssen vs Kieseritzky (London, 1851)
  - Move-by-move commentary
- ♕ **Pawn promotion UI**
  - Visual selection of promotion piece

---

## 🧠 Artificial Intelligence

The AI is implemented entirely in JavaScript and includes:

- **Minimax search**
- **Alpha-beta pruning**
- **Quiescence search** to reduce tactical blunders
- Move ordering (captures first)
- Evaluation based on:
  - Material balance
  - Piece mobility
  - Check, checkmate, and draw detection

> ⚠️ This engine is intended for **learning and casual play**, not for tournament-level competition.

---

## 🎮 Game Controls

### Main Panel

| Control | Description |
|------|-----------|
| ♔ / ♚ | Select player side |
| 1–5 | AI difficulty level |
| ↔️ | Flip board |
| ↶ | Undo move |
| ↺ | New game |
| 💾 | Save PGN |
| 📂 | Load PGN |
| ★ | Load the Immortal Game |

### Navigation Panel

| Control | Action |
|------|------|
| ⏮ | Go to start |
| ◀ | Previous move |
| ▶ | Next move |
| ⏭ | Go to end |

---

## 📂 Project Structure

The entire project can run as a **single HTML file**:

