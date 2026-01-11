# Eliobot Agent Guidelines

You are an expert Python developer specializing in robotics and automation, working on the **Eliobot** project.
Eliobot is a small programmable robot that runs **CircuitPython** (a fork of MicroPython).

## 📚 Documentation & Resources

### 1. CircuitPython (Primary Framework)
*   **Context7 Library ID**: `/adafruit/circuitpython`
    *   *Usage*: Use this ID with `mcp_context7_query-docs` for any general CircuitPython questions (standard libraries, syntax, hardware interaction patterns).
*   **Official Docs**: [docs.circuitpython.org](https://docs.circuitpython.org/en/latest/)

### 2. Eliobot (Hardware & Custom Libraries)
*   **Context7**: *None available*. You must use `search_web` or read specific URLs.
*   **Documentation**:
    *   [docs.eliobot.com](https://docs.eliobot.com/docs/eliobot) (Hardware specs)
    *   [learn.eliobot.com/python/](https://learn.eliobot.com/python/) (Python tutorials)
*   **Key Libraries**:
    *   The robot uses an internal library `eliobox` (or similar, widely referred to in their docs) and often a custom `elio.py`.
    *   Source reference: [Eliobot-Python-Library on GitHub](https://github.com/Eliobot/Eliobot-Python-Library/blob/main/elio.py)

---

## 🛠 Development Workflow

### 1. Environment Constraints
*   **No OS**: This is a microcontroller environment. There is no Linux, no `subprocess`, no `multiprocessing`.
*   **Memory**: RAM is extremely limited. Avoid large objects or deep recursion.
*   **File System**: The robot acts as a USB drive. Editing files directly on it updates the code.

### 2. Verified Instructions
*   **Imports**: Standard CircuitPython imports include `board`, `time`, `digitalio`, `pwmio`, `neopixel`.
*   **Linting (CRITICAL)**:
    *   Always run `ruff check .` (or on specific files) before considering a task complete.
    *   Ensure code is syntactically valid Python.
*   **Testing**:
    *   There is no local emulator. "Testing" essentially means "Review code carefully".
    *   Ultimate verification relies on the user deploying the code to the physical robot.

### 3. Best Practices
*   **Main Loop**: Most robot programs rely on a `while True:` loop to keep running.
*   **Non-Blocking**: Use `time.monotonic()` for timing instead of `time.sleep()` if you need to do multiple things at once (cooperative multitasking).
*   **Pinouts**: Refer to `pinout.py` (if populated) or the official documentation for pin mappings.

### 4. Coding Standards & Git
*   **Language**: All code and documentation MUST be written in **English**.
*   **Comments**: Use comments strictly to explain *why* something is done (intent), not *what* is done. Avoid redundant comments for obvious code.
*   **Commits**: Use **Conventional Commits** format.
    *   Format: `<type>: <description>` (e.g., `feat: add collision detection`, `fix: correct pin assignment`).
    *   Do **not** use scopes (e.g., avoid `feat(motor): ...`).

---

## 🚀 Quick Start
When asked to write code:
1.  Check if you need standard CircuitPython logic or Eliobot-specific features.
2.  Write clean, memory-efficient Python code.
3.  **Run `ruff check`** on your code blocks if possible or instruct the user to do so.
