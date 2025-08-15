# Contributing Guidelines

We welcome contributions to **morse-transcriber**!  
Whether you are fixing bugs, adding features, improving documentation, or suggesting ideas — your efforts are appreciated.

---

## Code of Conduct
By participating in this project, you agree to follow our **Code of Conduct**.  
This ensures a respectful and collaborative environment for all contributors.

---

##  Development Setup

### 1. Fork & Clone
1. Fork the repository on GitHub and clone it to your local machine:
    ```bash
    git clone https://github.com/<your-username>/morse-transcriber.git
    cd morse-transcriber
    ```
2. Create a Virtual Environment
    It’s best to work inside an isolated Python environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows
    ```
3. Install in Editable Mode
    ```bash
    pip install -e .[dev]
    ```
This allows you to run the CLI directly while making changes to the source code.

## Project Structure
## Coding Standards

- Follow PEP 8 for Python code style.
- Write clear docstrings for all public functions and classes.
- Ensure dictionary mappings in morse_map.py are authoritative and unique.
- Avoid hardcoding values; use constants or configuration where possible.

## Testing
Run the test suite before committing changes:
    ```bash
    pytest
    ```
All pull requests must pass the test suite and maintain at least the current coverage level.

## Git Workflow
1. Create a branch for your work:
    ```bash
    git checkout -b feature/new-command
    ```
2. Commit changes with clear messages:
    ```bash
    git commit -m "Add new command for batch processing"
    ```
3. Push your branch:
    ```bash
    git push origin feature/new-command
    ```
4. Open a Pull Request to the master branch.

## Changelog Updates
Every user-facing change should be documented in CHANGELOG.md.
Use the Keep a Changelog format and Semantic Versioning (SemVer).

## Communication

- For bug reports and feature requests, open a GitHub Issue.
- For large features, please start a discussion before implementing.
- PR reviews may request changes for code style, clarity, or maintainability.

## Recognition
Contributors will be credited in release notes and the project documentation.

**Thank you for making morse-transcriber better!**



