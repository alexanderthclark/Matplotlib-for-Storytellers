# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the repository for "Matplotlib for Storytellers", a Python data visualization book that teaches frustrated matplotlib users how to craft good data visuals. The project contains:

- LaTeX source files for the book (main.tex and supporting files in tex/)
- Python scripts generating matplotlib figures (python/)
- Generated figure outputs (figures/)
- Demo Jupyter notebooks (Demos/)
- Data files for examples (Data/)

## Key Commands

### Building the Book
```bash
# Compile the LaTeX book
pdflatex main.tex
# Run multiple times if needed for references/TOC
```

### Running Python Scripts
```bash
# Generate figures - scripts save to figures/ directory
cd python/
python <script-name>.py
```

### Common Dependencies
The project uses these Python libraries:
- matplotlib
- numpy
- pandas
- scipy
- scikit-learn (sklearn)
- ternary (optional, for ternary plots)

## Architecture Notes

1. **Figure Generation**: Python scripts in `python/` generate PDF figures saved to `figures/` subdirectories (mathplots/, poetryplots/, proseplots/, specialplots/)

2. **Book Structure**: The main LaTeX file `main.tex` includes chapters from `tex/` subdirectories:
   - prose/ - Core matplotlib concepts
   - poetry/ - Advanced visualizations
   - math/ - Mathematical interlude
   - special/ - Special topics (MDS, stats, ternary plots)

3. **Style Files**: 
   - Custom matplotlib styles in `stylelib/`
   - LaTeX style definitions in `tex/customcolors.sty` and `tex/mplstyle.sty`

4. **Helper Functions**: Some scripts use helper modules like `nyt-helper-data.py`, `rps-br-helper.py`, and `speedo-functions.py`

## Working with Figures

When modifying or creating figures:
1. Python scripts should save outputs to the appropriate `figures/` subdirectory
2. Use consistent naming between .py files and their .pdf outputs
3. Many scripts demonstrate specific matplotlib techniques mentioned in the book text

## Jupyter Book Conversion Guidelines

When converting LaTeX content to Jupyter Book format:

1. **Content Fidelity**: Keep the Jupyter Book content as close as possible to the LaTeX content. The primary goal is preserving the original text, code examples, and educational material.

2. **Acceptable Changes**:
   - Convert LaTeX syntax to Markdown (equations, formatting, etc.)
   - Adjust image paths and convert PDF figures to PNG format
   - Use Markdown-specific features for better web readability
   - Convert LaTeX cross-references to Markdown links
   
3. **Do NOT**:
   - Abbreviate or summarize content
   - Remove code examples or explanations
   - Change the pedagogical flow or structure
   - Add new content not present in the original LaTeX

4. **Figure Conversion**: Convert all PDF figures to PNG at 300 DPI for web compatibility while maintaining visual quality.