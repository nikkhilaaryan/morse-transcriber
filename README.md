
# morse-transcriber

# Overview
**morse-transcriber** is a command-line interface (CLI) application developed in Python for the bidirectional conversion between alphanumeric text and International Morse code. 

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/nikkhilaaryan/morse-transcriber/blob/main/LICENSE)
![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Cross-Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

---
**Disclaimer**: This software is in active development and may undergo significant architectural or functional changes. Features, APIs, and documentation are subject to modification without prior notice.
** Documentation:** [morse-transcriber full documentation](https://nikkhilaaryan.github.io/morse-transcriber/) 

## Features:
- **Bidirectional Conversion**:  
  - Text to Morse code  
  - Morse code to text  
- **Strict Input Validation**:  
  Ensures compliance with supported character sets prior to conversion.  
- **Clipboard Support**:  
  Automatically copies conversion results to the system clipboard (requires `pyperclip`).  
- **Interactive and One-Shot Modes**:  
  - Interactive menu-driven mode for sequential operations.  
  - Argument-based mode for single-operation execution without prompts.

## System Requirements
- **Python Version**: Python 3.8 or higher  
- **Supported Operating Systems**:  
  - Microsoft Windows 10/11 (PowerShell, Command Prompt, or compatible terminal emulator)  
  - macOS (Terminal)  
  - Linux distributions (Bash-compatible shell)  
- **Required Python Packages**:  
  - `pyperclip >= 1.8.0` (automatically installed via project dependencies)  
---
## Installation

### From Source (Development Mode)
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-organization>/morse-transcriber.git
   cd morse-transcriber
   ```

2. Install in editable mode:
    ```bash
    pip install -e .
    ```

## Usage

Morse Transcriber can be executed in two primary modes:

---

### 1. Interactive Mode
In this mode, the application launches an interactive menu system for repeated conversions.  
This is recommended for users performing multiple conversions in one session.

**Command:**
```bash
morse-transcriber
```
Example
```
morse-transcriber CLI
1. Text to Morse
2. Morse to Text
3. morse-transcriber terminated
Enter choice (1/2/3): 1
Enter text: SOS
Morse-Code: ... --- ...
```
### 2. One-Shot Argument Mode
Convert Text to Morse Code
Command:
```bash
morse-transcriber --text "SOS"
```
```
Expected Output: ... --- ...
```
Convert Morse Code to Text
Command:
```bash
morse-transcriber --morse "... --- ..."
```
```
Expected Output: SOS
```
## Development Guidelines
- Maintain compliance with PEP 8 style conventions.

- Ensure all dictionary mappings in morse_map.py are authoritative and unique.

- Implement automated unit tests before committing functional changes.

- All contributions must pass linting, static type checks, and existing test suites.

## License
This project is distributed under the MIT License.
See the LICENSE file for full terms.

## Contact
For technical inquiries, please contact:

Project Maintainer: **ARYAN RAJ** 

Email: **nikhilaryan0928@gmail.com**




