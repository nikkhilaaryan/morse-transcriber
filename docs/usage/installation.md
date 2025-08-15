# Installation Guide

This guide explains how to install **morse-transcriber** on your system.  
The tool supports **Python 3.8+** and works on **Windows**, **macOS**, and **Linux**.

---

##  Installing from PyPI (Recommended)

The easiest way to install is via **pip**:

```bash
pip install morse-transcriber
```
Once installed, you can run the CLI directly:
```bash
morse-transcriber --help
```

## Installing from Source (Development Mode)
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-organization>/morse-transcriber.git
   cd morse-transcriber
   ```
2. Create a virtual environment (recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate     # macOS/Linux
    .venv\Scripts\activate        # Windows
    ```

3. Install in editable mode:
    ```bash
    pip install -e .
    ```
## Verifying Installation
    ```bash
    morse-transcriber --version
    ```

## Troubleshooting

- Command not found:
    Ensure your Python Scripts (Windows) or bin (Linux/macOS) directory is in your PATH.

- Permission errors:
    Use --user with pip or install inside a virtual environment.


 