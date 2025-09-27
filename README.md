PVC Production Calculator (Web)

This project is a web conversion of a Tkinter-based PVC production calculator.

What I changed
- Rewrote the calculation logic as a Flask web app in `clculationsheet.py`.
- Added a responsive HTML/CSS frontend in `templates/index.html` and `static/styles.css`.
- Added `requirements.txt` with Flask and MarkupSafe.

How to run (Windows, cmd.exe)

1. Create and activate a virtual environment (recommended):

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```cmd
pip install -r requirements.txt
```

3. Run the app:

```cmd
python clculationsheet.py
```

4. Open your browser to http://127.0.0.1:5000

Notes
- The app uses the same formulas as the original script. Default inputs are provided for convenience.
- If you want a standalone executable later, I can add packaging instructions (PyInstaller).
 - The UI now runs as a single-page app (SPA) with live client-side calculations. If JavaScript is disabled, the server-side form still works as a fallback.
