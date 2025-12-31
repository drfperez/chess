# ♟️ Chess — Simple Chess Game & Lozza JavaScript Engine

A collection of **browser-based chess projects** built with **pure JavaScript**, ranging from a **single-file playable chess game** to **Lozza**, a fully **UCI-compliant JavaScript chess engine with NNUE evaluation**.

All projects run **client-side**, require **no server**, and are designed for **maximum portability**.

---

## 🔹 Simple Chess Game (Single HTML File)

A fully functional **chess game for browsers** (desktop & mobile), implemented in **one HTML file** using vanilla JavaScript.

📍 **Live demo**  
👉 https://drfperez.github.io/lozza  

📁 Or simply save the file as `index.html`, add `lozza.js`,  and then open it locally.

### ✨ Features

- Interactive chessboard with **drag & drop**
- **Built-in AI opponent** with 4 difficulty levels  
  *(minimax + alpha-beta pruning)*
- Play as **White or Black**
- **Board flip** support
- Full **move navigation** (start, end, forward, backward)
- **PGN load & save**
- Includes the legendary **Immortal Game (Anderssen, 1851)**  
  with **move-by-move comments in Catalan**
- **Mobile-optimized**, full-screen layout
- Minimal external dependencies (via CDN):
  - `chess.js`
  - `chessboard.js`
  - `jQuery`
    

---

### 🚀 How to Use

1. Copy the provided HTML source: `lozza.html` and do not forget to copy also `lozza.js`
2. Save it as `index.html`
3. Open it in any modern web browser

That’s it — no installation required.

---

### 📸 Screenshots

![Chess board with mobile controls](https://github.com/drfperez/chess/raw/main/captura1.jpg)  
*Compact, touch-friendly interface*

![Immortal Game with comments](https://github.com/drfperez/chess/raw/main/capture2.jpg)  
*Annotated historical game*

---

### 🛠 Technologies Used

- [chess.js](https://github.com/jhlywa/chess.js) — Chess rules & legality
- [chessboard.js](https://chessboardjs.com/) — Board rendering
- jQuery — Required for chessboard.js
- HTML5, CSS3, Vanilla JavaScript

---

## 🔹 Lozza — JavaScript UCI Chess Engine with NNUE

**Lozza** is a fully **UCI-compliant chess engine** written entirely in **JavaScript**.

### 🧠 Core Design

- Designed primarily for **browser execution** using **Web Workers**
- Also runs under **Node.js**
- Compatible with desktop GUIs:
  - Arena
  - CuteChess
  - WinBoard
  - Banksia
- **Single-file engine** (`lozza.js`)
- Uses code-folding markers for readability

---

### 🔍 Search & Evaluation

Lozza features a modern **alpha-beta search** enhanced with:

- Transposition tables
- Killer & history heuristics
- Internal iterative deepening
- Quiescence search
- Static Exchange Evaluation (SEE) pruning

#### 🧠 NNUE Evaluation

- Quantized **NNUE neural network**
- Compact architecture with **hex-encoded inlined weights**
- Incremental evaluation updates on make/unmake
- Replaced an earlier handcrafted evaluation (Fruit 2.1-based)

---

### 🏗 Release Process

Production builds include:

1. Disabled development features (randomization, strict checks)
2. Inlined neural network (`NET_LOCAL=1`)
3. Deterministic benchmarking & SPRT validation
4. Version tagging via `BUILD` constant (e.g. `"8"`)

---

### 📊 Project Status (December 2025)

| Category | Status |
|------|------|
| Latest Release | **Lozza 8** (September 2025) |
| Last Commit | November 2025 |
| GitHub Activity | 1,270+ commits |
| GitHub Stars | ⭐ 52 |

> Lozza prioritizes **portability and clarity** over raw speed, making it ideal for browser analysis and casual play.

---

## 🔹 Recorded Chess Player

An **online chess player** capable of replaying **pre-recorded chess games** with full controls.

- Built using `chess.js` and `chessboard.js`
- Designed for educational and historical game playback

🌐 **Live demo**  
👉 https://pompeu.neocities.org/chess/

---

## 🔹 Python Chess Experiments

A collection of **simple Python chess programs** demonstrating basic AI strategies:

- First legal move
- Random legal move
- Capture-prioritized moves

🌐 **Demo**  
👉 https://pompeu.neocities.org/chess/random

---

### 📷 Screenshot

![Chess board](https://github.com/drfperez/chess/raw/main/chess.jpg)

---

## 🤝 Contributions

Contributions are welcome! Ideas include:

- Integrating **Stockfish (WASM)**
- Improving NNUE networks
- Adding multiplayer or local two-player mode
- Translating annotations
- Enhancing evaluation heuristics

Feel free to fork, open issues, or submit pull requests.

---

## 📄 License

This project is released under the **MIT License**.

You are free to **use, modify, and distribute** this software.

---

♔ Enjoy the game and the engine! ♚
