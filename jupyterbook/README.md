# Matplotlib for Storytellers - Jupyter Book

This is the online Jupyter Book edition of *Matplotlib for Storytellers*.

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
- `_toc.yml` - Complete table of contents
- `intro.md` - Welcome page
- `chapter1/` through `chapter16/` - Chapter content
- `images/` - Web-ready figures from the print book

## Notes

- Code blocks are standard markdown with Python syntax highlighting
- Images have been converted to PNG format for better web display  
- The content follows the original LaTeX version while using MyST Markdown for web navigation, code listings, figures, links, and equations
- Note: Some code examples assume previous imports (e.g., `import matplotlib.pyplot as plt`, `import numpy as np`, `import pandas as pd`)
