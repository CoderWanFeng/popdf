---
name: "pdf2word"
description: "Converts PDF files to Word documents using the popdf library. Invoke when user needs to convert PDF files to Word format."
---

# PDF to Word Converter Skill

This skill provides PDF to Word conversion functionality using the popdf library. It supports both single file and batch conversion options.

## Features

- **Single File Conversion**: Convert individual PDF files to Word
- **Batch Conversion**: Convert multiple PDF files at once
- **CLI Interface**: Command-line tool for quick conversions
- **GUI Interface**: Graphical user interface for easy operation

## Usage

### CLI Usage

```bash
# Convert single PDF
pdf2word -i input.pdf -o output.docx

# Help
pdf2word --help
```

### Python API

```python
import popdf

# Convert single PDF
popdf.pdf2docx(
    input_file='input.pdf',
    output_file='output.docx'
)

# Batch conversion
popdf.pdf2docx(
    input_path='/path/to/pdf/folder/',
    output_path='/path/to/output/folder/'
)
```

### GUI Usage

Run the GUI application:

```bash
python temp/case/gui/pdf_converter.py
```

## Dependencies

- popdf
- PySide6 (for GUI)
- click (for CLI)

## Installation

```bash
# Install from source
cd /path/to/popdf
pip install -e .

# Install CLI tool
cd temp/case/cli
pip install -e .
```

## Files Included

- `cli/pdf2word.py` - Command-line interface
- `code/pdf2word.py` - Basic Python implementation
- `gui/pdf_converter.py` - Graphical user interface

## Examples

### Single File Conversion

```bash
pdf2word -i document.pdf -o document.docx
```

### Batch Conversion

```python
import popdf

popdf.pdf2docx(
    input_path='/documents/pdfs/',
    output_path='/documents/word/'
)
```

## Troubleshooting

- **Error: No module named 'pymupdf'** - Create symlink: `ln -sf fitz pymupdf` in site-packages
- **Error: 'Rect' object has no attribute 'get_area'** - Use compatible PyMuPDF version (1.24.0 recommended)
- **Conversion fails** - Ensure PDF is not password-protected and is not a scanned document