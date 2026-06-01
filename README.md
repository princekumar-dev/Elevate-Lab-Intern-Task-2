
# Titanic Dataset Analysis

What I did:
- Added `analysis.py` which generates summary CSVs, plots, and a markdown report into `outputs/`.
- Added `analysis_console.py` which runs interactively: prints summary statistics and shows plots without writing files.

Files and outputs:
- `analysis.py` — writes outputs to `outputs/` (CSV, PNG, markdown report).
- `analysis_console.py` — interactive; prints stats and displays histograms, boxplots, a pairplot, and correlation heatmap without saving files.

Run (interactive, preferred when you don't want files):

Windows PowerShell (activate your env first):

```powershell
python analysis_console.py
```

Run (save outputs):

```powershell
python analysis.py
```

Dependencies:
- `pandas`, `seaborn`, `matplotlib`, `numpy` — install into your env if needed.

Notes:
- `analysis_console.py` will display plots with `matplotlib` interactive windows; close them to continue.
- `analysis.py` will create an `outputs/` directory and save files there.
