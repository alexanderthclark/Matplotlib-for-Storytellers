# Matplotlib for Storytellers - Jupyter Book

This is the Jupyter Book version of Chapter 1: The Object-oriented Interface from "Matplotlib for Storytellers".

## Building the Book

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Build the book:
```bash
jupyter-book build .
```

3. View the book:
```bash
open _build/html/index.html
```

## Structure

- `_config.yml` - Book configuration
- `_toc.yml` - Table of contents  
- `intro.md` - Welcome page
- `chapter1/` - Chapter 1 content
  - `index.md` - The Object-oriented Interface chapter
  - `images/` - Figure PDFs from the original book

## Notes

- Code blocks are standard markdown with Python syntax highlighting
- Images have been converted to PNG format for better web display  
- The content faithfully follows the original LaTeX version
- Note: Some code examples assume previous imports (e.g., `import matplotlib.pyplot as plt`, `import numpy as np`, `import pandas as pd`)